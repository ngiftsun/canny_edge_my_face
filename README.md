# canny_edge_my_face

This simple package allows you to apply canny edge filters to the moving images from your camera.

### Prerequisites

Install cv_camera and opencv package 
```
sudo apt-get install ros-indigo-cv-camera
sudo apt-get install ros-indigo-opencv3
```
### How to check?
Run cv_camera node
```
rosparam set cv_camera/device_id 0
rosrun cv_camera cv_camera_node
```
Run src/cannyEdgeMyFace.py 
```
ipython -i src/cannyEdgeMyFace.py 
```
![Alt text](canny_edge.png?raw=true "Example Result")







