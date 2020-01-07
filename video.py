#reproduccion de videos desde almacenamiento rapido
import cv2

#declaramos la varible de captura del video
cap = cv2.VideoCapture("videos/adicto.mp4")

#declaramos el while para reproduccir el video
while(cap.isOpened()):
    #declaramos la varibles para ejecutar el video
    ret, frame = cap.read()
    #convertimos el video a escala de grisis
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #mostramos el video en una ventana
    cv2.imshow("video adicto", frame)
    #declaramos las varibles de cierre del video
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

#Liberaos el espacio en memoria para dejar el software y hadware libre
cap.release()
cv2.destroyAllWindows()