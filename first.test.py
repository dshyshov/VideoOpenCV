import numpy as np
import cv2

cap = cv2.VideoCapture(0)
font = cv2.FONT_ITALIC

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)


    cv2.line(gray,(360,263),(360,313),(255,255,255),1)
    cv2.line(gray,(335,288),(385,288),(255,255,255),1)

    gray_bord = cv2.copyMakeBorder(gray,0,0,304,0,cv2.BORDER_CONSTANT,dst=None,value=(0,0,0))
    cv2.putText(gray_bord,'UAV Position',(30,55), font, 0.5,(0,0,255),1,cv2.CV_AA)
    cv2.putText(gray_bord,'LON 43.54565',(30,75), font, 0.5,(255,255,255),1,cv2.CV_AA)
    cv2.rectangle(gray_bord,(20,35),(200,95),(255,255,255),1)

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
