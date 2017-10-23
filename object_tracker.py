import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Webcam Capture

onlyOnce = False
alreadyDetected = [False,False,False,False,False]

while (True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in range(1,2):
        template = cv2.imread('images/pic'+str(i)+'.png', 0)
        w, h = template.shape[::-1]

        if alreadyDetected[i] is False :

            res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.6

            loc = np.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                top_left = pt
                bottom_right = (top_left[0] + w, top_left[1] + h)
                demo = cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 3)
                if i is 1 :
                    cv2.putText(frame, 'Mobile' , (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_PLAIN,1.4, (255, 255, 255))

                if demo is not None :
                    if onlyOnce is True :
                        alreadyDetected[i] = True
                    print('Object Found')
                break


    cv2.imshow('Object Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()