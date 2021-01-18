import cv2
import numpy as np


circles = np.zeros((4, 2), np.int)
counter = 0


def mousePoints(events, x, y, flags, params):
    global counter
    if events == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)


url = 'http://192.168.43.1:8080/video'
cam = cv2.VideoCapture(url)

while True:
    ret, frame = cam.read()
    frame=cv2.resize(frame, (640, 360))
    if frame is not None:
        cv2.imshow('frame', frame)


#img = cv2.imread('1.jpg')
#if img.shape[0] > img.shape[1]:
#    img = cv2.resize(img, (600, 800))
#elif img.shape[0] < img.shape[1]:
#    img = cv2.resize(img, (800, 600))
#else:
#    img = cv2.resize(img, (800, 800))
#
#while True:
        if counter == 4:
            width, height = frame.shape[1], frame.shape[0]
            pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgOutput = cv2.warpPerspective(frame, matrix, (width, height))
            cv2.imshow('Output', imgOutput)

        for x in range(0, 4):
            cv2.circle(frame, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv2.FILLED)

        cv2.imshow('Original', frame)
        cv2.setMouseCallback('Original', mousePoints)
        q = cv2.waitKey(1)
        if q == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()