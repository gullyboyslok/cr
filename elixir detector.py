
import cv2
import numpy as np

img = cv2.imread("\\test imgs\\TEST0.png", cv2.IMREAD_GRAYSCALE)
# when adding path use double backslash
# change TEST0 to TESTx where x is the testing elixir digit from 0-9. u choose what screenshot to test basically

img = img[2455:2525, 337:380]

_, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

best_match = None
best_score = -1

for i in range(0, 10):
    template = cv2.imread(f"\\test imgs\\{i}elixir.png", cv2.IMREAD_GRAYSCALE)
    #when adding path use double backslash
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
