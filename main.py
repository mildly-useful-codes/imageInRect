import cv2

img1 = cv2.imread('img.png')  # image with rectangle
img2 = cv2.imread('picture.jpg')  # image to place

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

binary = cv2.bitwise_not(gray)

(_, contours, _) = cv2.findContours(binary, cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_NONE)

list_of_cont = []

for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    img2 = cv2.resize(img2, (w, h))
    img1[y:y + h, x:x + w] = img2

cv2.imwrite('output.jpg', img1)
