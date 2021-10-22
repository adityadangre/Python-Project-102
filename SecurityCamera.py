#Computer vision detecting packege 
import cv2
import winsound

#Open webcam to capture video 
cam = cv2.VideoCapture(0)

#Define while loop to turn camera on till we don't quit it
while cam.isOpened():

   #Read camera in two frame so that we can comapre two frame 
   ret, frame1 = cam.read()
   ret, frame2 = cam.read()

   #Finding absolute difference between frame 1 & frame 2
   diff = cv2.absdiff(frame1, frame2)

   #Convert colour differance into gray color
   gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

   #Convert gray color to blur image
   blur = cv2.GaussianBlur(gray, (5, 5), 0)

   #Create threshold image
   _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

   #Do dilation from thresh image to wanted image
   dilated = cv2.dilate(thresh, None, iterations = 3)

   #Get contours to find moving outline
   contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
   for c in contours :
       #if movement is less than 5000 then no buzzer
       if cv2.contourArea(c) < 5000:
           continue

       #Draw rectangle for moving part
       x, y, w, h = cv2.boundingRect(c)
       cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

       #If movement happen, then play beep sound
       winsound.Beep(500, 200)

   #When user press q, the screen recording will stop
   if(cv2.waitKey(10) == ord('q')):
       break

   #Show camera on screen
   cv2.imshow('MyCam', frame1)