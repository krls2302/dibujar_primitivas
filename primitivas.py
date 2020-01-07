#importamos libreria
import numpy as np      #con as cambiamos el nombre de la libreria
import cv2

#creamos nuestro array y la ventana
img = np.zeros((512,512,3), np.uint8)
#creamos una linea en la ventana
#para los colores es bgr(blue,green,red)
img = cv2.line(img, (10,10), (500,500),(255,0,0), 10)


#declaramos la ventana de presentacion
#cv2.namedWindow("formas", cv2.WINDOW_NORMAL)
#creamos la ventana a mostrar
cv2.imshow('primeras formas', img)
#Declaramos una tecla para finalizar transmicion de video
cv2.waitKey(0)

#liberamos el video y cerramos todo
cv2.destroyAllWindows()