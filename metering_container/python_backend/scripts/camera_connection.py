import cv2

try:
    import cv2
except ImportError:
    # Manejo de la importación fallida de cv2
    pass

# Se importan las funciones necesarias de los otros módulos .py
from image_processing import detect_needle, select_roi

def establecer_conexion(url_cam):
    cap = cv2.VideoCapture(url_cam + ":81/stream")
    if not cap.isOpened():
        print("Error al conectar con la cámara IP. Verifica la conexión y la dirección URL.")
    return cap

def streaming(video_capture, mapping_function, mapping_type):
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error al recibir frame (capturar la imagen) de la cámara.")
            break

        # PROCESAMIENTO DE LA IMAGEN CON OPENCV

        # PROCESAR FRAME
        # Definir una región de interés (ROI)
        frame_with_roi, roi = select_roi(frame)
        # Mostrar la ROI sobre copia de la original y recortada, para calibrar captura de aguja
        cv2.imshow('Streaming con ROI', frame_with_roi)

        # Esperar 1 milisegundo
        # cv2.waitKey(1)

        # Esperar a que el usuario presione la tecla 'Enter' para procesar la región de interés
        if cv2.waitKey(1) & 0xFF == 13:  # 13 es el código ASCII para la tecla 'Enter'
            # ROI capturada, aquí 'roi' es una imagen estática ya
            # cv2.imshow('ROI capturada', roi)

            # Esperar a que el usuario presione cualquier tecla para continuar
            # cv2.waitKey(0)

            # DETECTAR AGUJA Y VALOR DE INTERÉS
            # Detección del contorno de la aguja en la ROI
            line_needle, angle_deg = detect_needle(roi)
            # Mostrar el dibujo de la línea sobre la aguja
            cv2.imshow('Dibujo de linea sobre aguja detectada', line_needle)

            # Mapeo del ángulo obtenido al valor de interés correspondiente (se lo pasamos en argumento)
            value = mapping_function(angle_deg)
            # print("Ángulo con el eje horizontal:", angle_deg, "grados")

            if mapping_type == "temperature":
                print("Temperatura asociada:", value, "grados Celsius")
                # print(value)
            elif mapping_type == "current":
                print("Corriente asociada:", value, "mA")
                # print(value)
            # value es el valor que tenemos que pasarle a Node-RED

            cv2.waitKey(0)

            # Verificar si se ha encontrado el valor de interés
            if value is not None:
                break  # Salir del bucle si se ha encontrado el valor de interés

    # Liberar recursos
    video_capture.release()
    cv2.destroyAllWindows()
