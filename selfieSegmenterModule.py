import cv2 as cv
import numpy as np
import mediapipe as mp

class Selfie_segmentation():

    def __init__(self,model = 1): # model represents the technique General(0) & Landscape(1)
        self.model = model
        self.mpDraw = mp.solutions.drawing_utils

        # Calling the selfie_segmentation Ml model
        self.mp_selfie_Segmentation = mp.solutions.selfie_segmentation

        # Setting parameters Ml model
        self.Selfie_Segmentation = self.mp_selfie_Segmentation.SelfieSegmentation(self.model)

    """"
        Frame = (Input Frame)
        BGimg = (Background-Frame) Default = (WHITE)
        threshold = (Ml-model parameter)
    """
    def Bg_Remover(self, frame, BGimg = (255,255,255), threshold = 0.1, blur=(7,7), invisible = False, frametemp = None):
        'Convert color and flip frame'
        frame = cv.cvtColor( cv.flip(frame,1), cv.COLOR_BGR2RGB)

        'Improve performance: frame as not writeable'
        frame.flags.writeable = False

        'Pass through Ml-model'
        results = self.Selfie_Segmentation.process(frame)

        'frame as Writeable'
        frame.flags.writeable = True
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        condition = np.stack((results.segmentation_mask, ) * 3, axis=-1) > threshold

        'BGimg  passed as color(tuple) => (255,255,255)'
        if isinstance(BGimg, tuple):
            bg_frame = np.zeros(frame.shape, dtype=np.uint8)
            bg_frame[:] = BGimg
            output_frame = np.where(condition, frame, bg_frame)
            return output_frame

        # Make yourself invisible
        elif invisible == True:
            try:
                frametemp = cv.GaussianBlur(cv.flip(frametemp,1),blur,0)
                BGimg = frame
                output_frame = np.where(condition, frametemp, BGimg)
            except:
                print("No Background Frame Given\n"
                      "pass a still backgrounds i.e first frame, \n "
                      "your body will be replaced with this frame")

        # BGimg as a image
        else:
            BGimg = cv.GaussianBlur(BGimg,blur,0)
            output_frame = np.where(condition, frame, BGimg)

        return output_frame

