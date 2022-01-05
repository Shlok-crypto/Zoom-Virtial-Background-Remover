import cv2 as cv
import datetime
# Saving VIDEO(Mp4) File

# Call this Funtion outside the While loop
# *name* is the name of the file to save as
class VideoFileSaving():                      #H   #W
    def __init__(self,name,fourcc=-1,Winsize=(640, 480)):
        time_stamp = datetime.datetime.now().strftime('%y-%m-%d-%H-%M')

        name = f'{name}-{time_stamp}'
        self.Videofile = cv.VideoWriter(f'{name}.mp4', fourcc, 20.0, Winsize)

        print("Video Saving initialized")
        print(f"{name = }.mp4")

# Call this Function inside the While loop outvideo.videoSaver
# *outVideo* is RETURN OF the videoFileSaving function
# *frame* is the frame(s) to be saved
    def videoSaver(self,frame):
        self.Videofile.write(frame)