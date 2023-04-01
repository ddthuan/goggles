# goggles

<h1>Samples</h1>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/01.jpg?raw=true" />
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/02.jpg?raw=true" />
<br><br>
<h1>Image Acquistion</h1>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/08.jpg?raw=true" />
<br>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/09.jpg?raw=true" />
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/system4.png?raw=true" />
<br>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/07.jpg?raw=true" />

<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/light.jpg?raw=true" />


<h3>Capture image and ROI</h3>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/11.jpg?raw=true" />
<a href="https://github.com/ddthuan/goggles/blob/master/Capture_Image/get_image_roi.py">Script</a>

<h3>Defect Type</h3>
<table>
  <tr>
    <th>Scratch</th>
    <th>Watermark</th>
    <th>Spotlight</th>
    <th>Stain</th>
    <th>Dust-line</th>
    <th>Dust-spot</th>

  </tr>
  <tr>    
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/scratch.png?raw=true" /></td>
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/watermark.png?raw=true" /></td>
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/spotlight.png?raw=true" /></td>
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/stain.png?raw=true" /></td>
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/dust_line.png?raw=true" /></td>
    <td><img src="https://github.com/ddthuan/goggles/blob/master/show_img/defect_type/dust_spot.png?raw=true" /></td>
  </tr>
</table>

<br>
<br>

<h1>Dataset</h1>
<h2>Labeling the initial dataset by Labelme </h2>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/13.jpg?raw=true" />
<h4>The statistics of the number of defects in the initial dataset</h4>
<table>
  <tr>
    <td><b>Defect Type</b></td>
    <th>Scratch</th>
    <th>Watermark</th>
    <th>Spotlight</th>
    <th>Stain</th>
    <th>Dust-line</th>
    <th>Dust-spot</th>

  </tr>
  
  <tr>
    <td><b>Number</b></td>
    <td>1972</td>
    <td>120</td>
    <td>229</td>
    <td>281</td>
    <td>7292</td>
    <td>1898</td>    
  </tr>
  </tr>
    <td><b>Total</b></td>
    <td colspan="6">11792</td>
  </tr>
</table>
<br>

<h2> The synthetic Data</h2>
<h5>The idea comes from <a href="https://github.com/LinkedAi/flip">Flip</a>. The rare defects like Spotlight, Stain, Watermark will generated more. </h5>
<h5>The small batch of the <b>Spotlight</b> objects</h5>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/spotlight.png?raw=true" />
<h5>The small batch of the <b>Stain</b> objects</h5>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/stain_1.png?raw=true" />
<h5>The small batch of the Watermark objects</h5>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/watermark.png?raw=true" />
<br>
<h5>The synthetic image</h5>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/axonv2_108.jpeg?raw=true" />
<h5>Labeling the synthetic data by Labelme tool</h5>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/1_label.png?raw=true" />

<h4>The statistics of the number of defects in the <b>synthenic</b> dataset</h4>
<table>
  <tr>
    <td><b>Defect Type</b></td>
    <th>Scratch</th>
    <th>Watermark</th>
    <th>Spotlight</th>
    <th>Stain</th>
    <th>Dust-line</th>
    <th>Dust-spot</th>

  </tr>
  
  <tr>
    <td><b>Number</b></td>
    <td>0</td>
    <td>973</td>
    <td>1093</td>
    <td>1328</td>
    <td>0</td>
    <td>0</td>    
  </tr>
  </tr>
    <td><b>Total</b></td>
    <td colspan="6">3394</td>
  </tr>
</table>

<h4>The statistics of the number of defects in the combined dataset</h4>
<table>
  <tr>
    <td><b>Defect Type</b></td>
    <th>Scratch</th>
    <th>Watermark</th>
    <th>Spotlight</th>
    <th>Stain</th>
    <th>Dust-line</th>
    <th>Dust-spot</th>

  </tr>
  
  <tr>
    <td><b>Number</b></td>
    <td>1972</td>
    <td>1093</td>
    <td>1322</td>
    <td>1609</td>
    <td>7292</td>
    <td>1898</td>    
  </tr>
  </tr>
    <td><b>Total</b></td>
    <td colspan="6">15186</td>
  </tr>
</table>
<br>
<br>
<h1>Methodology</h1>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/05.jpg?raw=true" />
<br>
<img src="https://github.com/ddthuan/goggles/blob/master/show_img/img_select/15.jpg?raw=true" />

<p>
Combining Faster R-CNN, Feature Pyramid Network (FPN), and MobileNetV3 in object detection results in a lightweight, efficient, and accurate model that can perform well on various tasks. By integrating these three components, the model can leverage their strengths to achieve fast and precise object detection.
</p?
<p>
<ul>
  <li>Faster R-CNN: Faster R-CNN is a state-of-the-art object detection model that utilizes a two-stage approach for detection. The first stage, called the Region Proposal Network (RPN), generates object proposals, while the second stage refines these proposals by classifying objects and regressing bounding boxes. Faster R-CNN is known for its high accuracy but can be computationally expensive.</li>
  <li>Feature Pyramid Network (FPN): FPN is an architecture that addresses the challenge of detecting objects at varying scales in an image. FPN constructs a multi-scale feature pyramid by combining high-level semantic features from deep layers with low-level spatial features from shallow layers. This process improves detection performance across a range of object sizes and reduces false negatives.</li>
  <li>MobileNetV3: MobileNetV3 is a computationally efficient CNN architecture designed for mobile and edge devices. It uses depthwise separable convolutions and inverted residual blocks to reduce computation while maintaining performance. MobileNetV3 is lightweight and fast, making it suitable for real-time applications.</li>
</ul>
</p>

<p>
Combining Faster R-CNN, FPN, and MobileNetV3 in object detection involves the following steps:
</p>
<p>
<ul>
  <li>Replace the backbone network: Substitute the default backbone network (e.g., VGG or ResNet) in Faster R-CNN with MobileNetV3. This change will reduce the model's computational requirements while maintaining its ability to extract high-level features.</li>
  <li>ntegrate FPN: Incorporate the FPN architecture into the modified Faster R-CNN model. Connect the MobileNetV3 backbone to the FPN, enabling the model to generate multi-scale feature maps that improve detection performance across various object scales.</li>
  <li>Train and fine-tune: Train the combined model on an object detection dataset. Fine-tune the model to adapt it to the specific task and dataset.</li>
</ul>
</p>
<p>
The resulting model, which combines Faster R-CNN, FPN, and MobileNetV3, will offer a balance between accuracy and computational efficiency. It will be suitable for object detection tasks that require real-time performance, particularly on devices with limited computational resources, such as mobile phones and edge devices.
</p>
