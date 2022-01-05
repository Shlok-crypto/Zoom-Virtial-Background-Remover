import cv2 as cv
import imutils
import os
from selfieSegmenterModule import Selfie_segmentation
import VideoSaving as vs

capture = cv.VideoCapture(0)
#capture = cv.VideoCapture('Yoga.Ai_Live_Frame-21-08-02-08-12.mp4')

"Object of VideoSaving(i.e saving the output as mp4 file)"
outvideo = vs.VideoFileSaving('SelfieSegmentation')

"""
    Create a list of backgrounds images 
"""
dir = "Background"
backgrounds = []
for i in os.listdir(dir):
    backgrounds.append(cv.imread(dir + '/' + i))

"Initialize the First background "
background = backgrounds[0]

"""
    Still Frame
"""
_,tempFrame = capture.read()

"local Varibles"
i = 0
Flag = False

"""
    Initialize Object of SelfieSegmentaingd
"""
virtualBG = Selfie_segmentation()

while True:
    _,frame = capture.read()
    frame = cv.GaussianBlur(frame,(3,3),0)
    try:
        if Flag == False:
            outframe = virtualBG.Bg_Remover(frame, BGimg=background, threshold=0.8, blur=(3, 3))
            cv.imshow("New Background", outframe)
    # Invisibility
        else:
            outframe = virtualBG.Bg_Remover(frame, BGimg=background, threshold=0.8, blur=(3, 3), invisible=True, frametemp=background)
            cv.imshow("New Background", outframe)
        outvideo.videoSaver(outframe)
    except ValueError:
        print("Images not same size")
        print(ValueError)
        break
    except:
        print("Something else went WRONG!!")
        break

    key = cv.waitKey(20)

    """
        Change to next Background
    """
    if key == ord('d'):
        if i < len(backgrounds)-1:
            i += 1
            print(F"{i = }")
            Flag = False
            background = backgrounds[i]
    elif key == ord('a'):
        if i > 0:
            i -= 1
            print(F"{i = }")
            Flag = False
            background = backgrounds[i]

    # Invisibility Option
    elif key == ord('s'):
        background = tempFrame
        Flag = True

    elif key == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
