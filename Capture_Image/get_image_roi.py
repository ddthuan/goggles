import torch
import torchvision

import numpy as np
import os
import platform

from torchvision.utils import save_image
from torchvision import transforms as T
from torchvision.ops import roi_align
from torchvision.transforms.functional import to_tensor, to_pil_image 

os.environ["PYLON_CAMEMU"] = "3"

from pypylon import genicam
from pypylon import pylon
import sys

countOfImagesToGrab = 5

maxCamerasToUse = 5

# The exit code of the sample application.
exitCode = 0

camera_id = {
    0:"cam1",
    1:"cam2",
    2:"cam3",
    3:"cam4",
    4:"cam5"
}

sample_name = sys.argv[1]
sample_side = int(sys.argv[2])

roi = torch.tensor(
[[
  [0., 512, 750, 3072,3000], #camera 1
  [0, 820, 750,3750,3000],, #camera 2
  [0, 750, 800, 3500, 3000], #camera 3
  [0, 500, 700, 3600, 3000], #camera 4
  [0, 1400, 290, 3650, 3000] #camera 5
  ],
 [
  [0, 500, 30, 2900, 3000], #camera 1
  [0, 900, 0, 3730, 3000], #camera 2
  [0, 750, 0, 3510, 3000], #camera 3
  [0, 430, 0, 3060, 3000], #camera 4
  [0, 1100, 0, 3750, 2780] #camera 5
  ]
 ], 
)


# ROI
def pre_roi(img_name, img_ts, img_side, cam_id):
    box = roi[img_side-1, cam_id]
    W, H = int(box[3]-box[1]), int(box[4]-box[2])
    img_roi = roi_align(img_ts[None], box[None], (H, W))
    save_image(img_roi[0], "roi\{}".format(img_name))

try:
    # Get the transport layer factory.
    tlFactory = pylon.TlFactory.GetInstance()

    # Get all attached devices and exit application if no device is found.
    devices = tlFactory.EnumerateDevices()
    
    # chi dinh camera capture anh
    devices = (devices[1], devices[2], devices[3], devices[4], devices[5])

    if len(devices) == 0:
        raise pylon.RuntimeException("No camera present.")

    # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

    l = cameras.GetSize()

    # Create and attach all Pylon Devices.
    for i, cam in enumerate(cameras):
        cam.Attach(tlFactory.CreateDevice(devices[i]))

        # Print the model name of the camera.
        print("Using device ", cam.GetDeviceInfo().GetModelName())

    # Starts grabbing for all cameras starting with index 0. The grabbing
    # is started for one camera after the other. That's why the images of all
    # cameras are not taken at the same time.
    # However, a hardware trigger setup can be used to cause all cameras to grab images synchronously.
    # According to their default configuration, the cameras are
    # set up for free-running continuous acquisition.
    cameras.StartGrabbing()

    # Grab c_countOfImagesToGrab from the cameras.
    img = pylon.PylonImage()

    for i in range(countOfImagesToGrab):
        if not cameras.IsGrabbing():
            break

        grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        #print(grabResult)
        camera_name = camera_id[i%maxCamerasToUse]
        
        img_name = "{}_{}_{}.jpeg".format(sample_name, sample_side, camera_name)
        
        # chuyen doi dinh dang
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_RGB8packed
        converted = converter.Convert(grabResult)
        img_rgb = converted.GetArray()
        img_ts = to_tensor(img_rgb)
        pre_roi(img_name, img_ts, sample_side, i)
        
               
        # Luu anh chup tu camera
        img.AttachGrabResultBuffer(grabResult)
        if platform.system() == 'Windows':
            ipo = pylon.ImagePersistenceOptions()
            #quality = 250 - i * 50
            quality = int(np.random.randint(99,100, 1))
            ipo.SetQuality(quality)            
            #filename = "saved_pypylon_img_%d.jpeg" % quality
            #filename = "{}\{}_{}_{}_{}.jpeg".format(preprocessing_path, sample_name, camera_name, i, quality, )
            filename = "raw\{}_{}_{}.jpeg".format(sample_name, sample_side, camera_name)
            #print(save_path, img_name)
            print(filename)
            img.Save(pylon.ImageFileFormat_Jpeg, filename, ipo)
            
        print("=============== Finish ==================")
        # When the cameras in the array are created the camera context value
        # is set to the index of the camera in the array.
        # The camera context is a user settable value.
        # This value is attached to each grab result and can be used
        # to determine the camera that produced the grab result.
        cameraContextValue = grabResult.GetCameraContext()

except genicam.GenericException as e:
    # Error handling
    print("An exception occurred.", e.GetDescription())
    exitCode = 1

# Comment the following two lines to disable waiting on exit.
sys.exit(exitCode)