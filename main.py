import cv2
import numpy as np
import os
import HandTrackingModule as htm

# Brush and eraser thickness
brushThickness = 15
eraserThickness = 100

# Folder path for header images
folderPath = r"C:\Users\Lenovo\Desktop\AirCanvas\Header"
overlayList = [cv2.imread(os.path.join(folderPath, imPath)) for imPath in os.listdir(folderPath)]
header = overlayList[0]
drawColor = (0, 0, 255)

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htm.HandTracker(detection_confidence=0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)

    if lmList:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        fingers = detector.fingersUp()

        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlayList[0]
                    drawColor = (0, 0, 255)
                elif 550 < x1 < 750:
                    header = overlayList[1]
                    drawColor = (255, 0, 100)
                elif 800 < x1 < 950:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)
                cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        if fingers[1] and not fingers[2]:
            cv2.circle(img, (x1, y1), brushThickness, drawColor, cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            thickness = eraserThickness if drawColor == (0, 0, 0) else brushThickness
            cv2.line(img, (xp, yp), (x1, y1), drawColor, thickness)
            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, thickness)
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:125, 0:1280] = header
    cv2.imshow("Image Canvas", img)
    cv2.imshow("Black Canvas", imgInv)
    cv2.imshow('White Canvas',imgCanvas)

    # Handle keyboard input for changing brush thickness
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('i'):  # Increase brush thickness
        brushThickness += 5
    elif key == ord('d'):  # Decrease brush thickness
        brushThickness -= 5
        if brushThickness < 5:  # Ensure minimum thickness
            brushThickness = 5

cap.release()
cv2.destroyAllWindows()
