#Visualising same video Tiger.mp4 one in colour(variable=frame) and another(variable=gray)
import numpy as np
import cv2
video = cv2.VideoCapture('Tiger.mp4')

while True:
    ret, frame = video.read()
   
    #defining grayscale the frame captured from video whichis a cv2 object
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('The Frame', frame)
    cv2.imshow('Gray View', gray)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video.release()
cv2.destroyAllWindows()
#Multiple videos of different contents can also be used as a source of different video frames to create Group AR effects.
#Similarly one or multiple images can be used for Group AR effects while making videocalling on facebook.The code is below
img = cv.imread('C:\Python\SD PROJECT\FINANCIAL MARKET WORKSPACE\SD WORKSPACE\GUI App Desktop\.venv\Assets\Photo or Images\SDCOOL.jpg', -1)
cv2.imshow('Image of FB', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Next line of code is to connect a web camera as a source and a video file named tiger.
#For AR Group effects the speed of the frame modified by following line of codes and one web camera is also used as a video source.The code is below:
import numpy as np
import cv2
import sys
#For web camera
video = cv2.VideoCapture(0)
#The video file where tiger is approaching in slow motion
bgvideo = cv2.VideoCapture('Tiger.mp4')#width 1280 height 720
#Rehsaping the video

sucess, ref_img = video.read()
flag = 0

while True:
    
    sucess, img = video.read()
    if img is not None:
        img = cv2.resize(img , (1500, 850), interpolation= cv2.INTER_AREA)
        ref_img = cv2.resize(ref_img , (1500, 850), interpolation= cv2.INTER_AREA)
        
        img = cv2.flip(img, 1)

        sucess, bg = bgvideo.read()
        bg = cv2.resize(bg , (1500, 850), interpolation= cv2.INTER_AREA)
        
        if flag == 0:
            ref_img = img
        
        diff1 = cv2.subtract(img,ref_img)
        diff2 = cv2.subtract(ref_img,img)
        
        diff = diff1 + diff2

        diff[abs(diff) < 25] = 0

        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) <10] = 0

        fgmask = gray.astype(np.uint8)

        fgmask[fgmask > 0 ] = 255

        fgmask_inv = cv2.bitwise_not(fgmask)

        fgimg = cv2.bitwise_and(img, img, mask= fgmask)
        bgimg = cv2.bitwise_and(bg, bg, mask= fgmask_inv)

        dst = cv2.add(bgimg, fgimg)
        cv2.imshow('Background removal', dst)

        key = cv2.waitKey(5) & 0xFF

        if ord('q') == key:
            break
        elif ord('d') == key:
            flag = 1
            print("background captured")
        elif ord('r') == key:
            flag = 0
            print("ready to capture a new background")

cv2.destroyAllWindows()
video.release()