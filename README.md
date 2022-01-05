# Zoom-Virtial Background / Remover
Zoom and MsTeams like background changer/remover. Now you can remove and change your image or video background for free. Also added support for  custom videos as background
# Prerequisite/libraries 
OpenCv 
Python 
Numpy 
MediaPipe
Os

# Input
Video Stream
# Output
 New Video Stream with Virtual Background 

# How it Works
Selfie Segmentation segments the prominent humans in the scene. It can run in real-time on laptops. The intended use cases include selfie effects and video conferencing, where the person is close (< 2m) to the camera.

Read in the live frame 
Read in the replacement frame(background) 
pass the Frame through machine learning model 
Dilate the thresholded frame 
find Contoues in the dilated frame 
optimize/process the contours 
Draw(fill) the contour => this will be the foreground roi 
separate the foreground from Background (cv.bitwize_and)
remove the foreground Roi from the New Background (cv.bitwize_and(inverseRoi, NewBackground) 
Combine the New Background Roi and foreground Roi (cv.bitwize_or(NewBackground, Foreground)

# Output 
![image](https://user-images.githubusercontent.com/83566027/148195931-b5f047f5-e71c-4136-925b-44c002749cab.png)
https://user-images.githubusercontent.com/83566027/148197075-22605773-2615-491a-bb13-e15d91c6fb5e.mp4
