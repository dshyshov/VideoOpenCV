import numpy as np
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_ITALIC

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    #HUD
    cv2.line(gray, (360, 263), (360, 313), (255, 255, 255), 1)
    cv2.line(gray, (335, 288), (385, 288), (255, 255, 255), 1)
    cv2.rectangle(gray,(20,278),(80,298),(255,255,255),1)
    cv2.putText(gray,'AS',(20,268), font, 0.5,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray,'0000',(30,293), font, 0.5,(255,255,255),1,cv2.CV_AA)
    cv2.rectangle(gray,(640,278),(700,298),(255,255,255),1)
    cv2.putText(gray,'ALT',(640,268), font, 0.5,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray,'0000',(650,293), font, 0.5,(255,255,255),1,cv2.CV_AA)

    gray_bord = cv2.copyMakeBorder(gray, 0, 0, 304, 0, cv2.BORDER_CONSTANT, dst=None, value=(0,0,0))

    #Target text Block
    cv2.putText(gray_bord,'Target',(25,55), font, 0.4,(0,125,250),1,cv2.CV_AA)
    cv2.putText(gray_bord,'WGS84 LON 43.54565 LAT 34.12345',(25,75), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord, 'SK42  LON 43.54m56s LAT 34.12m45s',(25,95), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.line(gray_bord,(25,110),(290,110),(255,255,255),1)
    #GPS Status text Block
    cv2.putText(gray_bord,'GPS Status',(25,130), font, 0.4,(0,125,250),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Satelites:0 Lock:No',(25,150), font, 0.4,(0,0,255),1,cv2.CV_AA)
    cv2.line(gray_bord,(25,165),(290,165),(255,255,255),1)
    #UAV Status text Block
    cv2.putText(gray_bord,'UAV Status',(25,185), font, 0.4,(0,125,250),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Airspeed: --- m/s',(25,205), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Ground Speed: --- m/s',(25,225), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Wind: --- deg --- m/s',(25,245), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Flight time: --- ',(25,265), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Est. time to return: --- ',(25,285), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'AS MAG INS TERR',(25,305), font, 0.4,(0,0,255),1,cv2.CV_AA)
    cv2.line(gray_bord,(25,320),(290,320),(255,255,255),1)
    #Radio Status Text Block
    cv2.putText(gray_bord,'Data Link Status',(25,340), font, 0.4,(0,125,250),1,cv2.CV_AA)
    cv2.putText(gray_bord,'GS: ---dB/---dB',(25,360), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'UAV: ---dB/---dB',(25,380), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.line(gray_bord,(25,395),(290,395),(255,255,255),1)
    #Route text block
    cv2.putText(gray_bord,'Route Status',(25,415), font, 0.4,(0,125,250),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Fly to WP# -',(25,435), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Distance to WP: ------',(25,455), font, 0.4,(255,255,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'Distance to home: ------',(25,475), font, 0.4,(255,255,255),1,cv2.CV_AA)


    # Display the resulting frame
    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow("test",gray_bord)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
