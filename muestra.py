import numpy
import cv2

imagen = cv2.imread("imges/00003.png")
cv2.imshow("Primera Imagen", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()