import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Webcam Capture

while (True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in range(1,3):
        template = cv2.imread('images/pic'+str(i)+'.png', 0)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(gray, template, cv2.TM_SQDIFF)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        '''top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(frame, top_left, bottom_right, (0,0,255), 3)
            cv2.putText(frame, 'Detected Pic : ' + str(i), (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255))
        '''

        threshold = 0.5
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255 , 0 , 0 ), 2)
            cv2.putText(frame, 'Detected Pic : ' + str(i), (pt[0], pt[1] - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255))


    cv2.imshow('Object Tracker', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()