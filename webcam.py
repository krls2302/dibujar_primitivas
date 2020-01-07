#Abrir camara web y mostrar transmicion
import cv2

#declaramos variable y iniciamos la funcion de video
cap = cv2.VideoCapture(0)

#Iniciamos un bucle para siempre ver la imagen
while(True):
    #Variable para leer la funcion de ver la camara
    ret, frame = cap.read()

    #pasamos la imagen a escala de grices
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #mostramos el video de la camara
    cv2.imshow("video en vivo", frame)

    #Declaramos una tecla para finalizar transmicion de video
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

#liberamos el video y cerramos todo
cap.release()
cv2.destroyAllWindows()
