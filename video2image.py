import cv2
import os
 
# Use VideoCapture para capturar video, aquí usamos video local
cap = cv2.VideoCapture("robot.mp4")
 # Crea un archivo para guardar el fotograma del video
save_path = os.makedirs("imagenes")
 
 # Si abrir el video correctamente
flag = 0
if cap.isOpened():
    flag = 1
else:
    flag = 0
 
 # Número total de fotogramas de video
i = 0
 # Nombra la captura de pantalla de la imagen
imgPath = ""
 
if flag == 1:
    while True:
        ret, frame = cap.read()
                 # Leer fotograma de video
        if ret == False:
                         # Determine si la lectura es exitosa
            break
        i += 1
                 # Usa i para nombrar la imagen
        imgPath = "imagenes/%s.jpg" % str(i)
                 # Almacene el fotograma de video extraído en imgPath
        cv2.imwrite(imgPath, frame)
 
print ("Finalizado!") # La extracción ha terminado, finaliza la impresión