
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\shlok\\Downloads\\clashroyalebot\\test imgs\\TEST0.png", cv2.IMREAD_GRAYSCALE)
# change TEST0 to TESTx where x is the testing elixir digit from 0-9

# test images: 8 5 6 7 9 0 2 3 4 1
# templates: 0 5 6 7 8 9

#print(type(img))
#print(img.shape)
#img = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
#height=50, width=30
img = img[2455:2525, 337:380]

#img = img[(int)(0.8*1680): (int)(0.8*1730), (int)(0.8*230):(int)(0.8*260)]


_, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
#gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

#_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

best_match = None
best_score = -1

for i in range(0, 10):
    template = cv2.imread(f"C:\\Users\\shlok\\Downloads\\clashroyalebot\\test imgs\\{i}elixir.png", cv2.IMREAD_GRAYSCALE)
    template = cv2.resize(template, (img.shape[1], img.shape[0]))
    _, template = cv2.threshold(template, 150, 255, cv2.THRESH_BINARY)

    
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    score = res.max()
    
    if score > best_score:
        best_score = score
        best_match = i

print("Detected digit:", best_match)


#cv2.namedWindow("window", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("window", 600, 700)
cv2.imshow("elixir number", img)
cv2.waitKey(0)
cv2.destroyAllWindows()