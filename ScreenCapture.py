#Application to record screen
from PIL import ImageGrab
#NumPy is a Python library used for working with arrays
import numpy as np
#Package use to capture image & display
import cv2

#importing our system Metrics
from win32api import GetSystemMetrics
import datetime

#Get Height and Width of your system 
width = GetSystemMetrics(0) # if pass 0, then we get width
height = GetSystemMetrics(1) # if pass 1, then we get height

#We use time_stamp to give different file name
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

#We give 4 charachter for encoding & decoding of our video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name,fourcc, 20.0, (width, height))

#Open webcam to capture video
webcam = cv2.VideoCapture(0)

#Define while loop to run recording continously until stoped by user
while True:

    #Use to grab image with declares boundry box
    img = ImageGrab.grab(bbox=(0, 0, width, height))

    #Convert image into numpy array so that we will give it to open CV
    img_np = np.array(img)

    #Color convertion of image in COLOR_BGR2RGB
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    #Read frame from webcam
    _ , frame = webcam.read()

    #Find height & width of our webcam video
    fr_height, fr_width, _ = frame.shape

    #Overlay one webcam image on our screen 
    img_final[0:fr_height, 0:fr_width, : ] = frame[0:fr_height ,0:fr_width, :]

    #Show image on screen
    cv2.imshow('ScreenCapture', img_final)

    #Write video on system
    captured_video.write(img_final)

    #When user press q, the screen recording will stop
    if cv2.waitKey(10) == ord('q'):
        break