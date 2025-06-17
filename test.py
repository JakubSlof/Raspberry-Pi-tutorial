import cv2
import numpy as np

img = cv2.imread("test.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# maska na šedou barvu
lower_gray = np.array([0, 0, 50])
upper_gray = np.array([180, 50, 200])
mask = cv2.inRange(hsv, lower_gray, upper_gray)

# najdi kontury
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w * h > 500:  # jednoduchý filtr velikosti
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

