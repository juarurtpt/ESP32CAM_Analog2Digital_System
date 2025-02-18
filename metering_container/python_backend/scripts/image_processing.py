import cv2

try:
    import cv2
except ImportError:
    # Manejo de la importación fallida de cv2
    pass

from angle_mapping import angle_with_horizontal

# PROCESAMIENTO DE LA IMAGEN
def detect_needle(image):
    try:
        # 1. Convertimos la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('1. Escala de grises', gray)

        # 2. Aplicamos un filtro de suavizado para reducir el ruido
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        # cv2.imshow('2. Suavizado', blurred)

        # 3. Aplicamos umbralización para segmentar la imagen en objetos de interés (aguja)
        _, thresh = cv2.threshold(blurred, 190, 255, cv2.THRESH_BINARY_INV)
        # cv2.imshow('3. Umbralizacion', thresh)

        # 4. Detección de bordes utilizando el algoritmo de Canny
        edges = cv2.Canny(thresh, 200, 255)
        # cv2.imshow('4. Deteccion de bordes con Canny', edges)

        # 5. Detección de contornos
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 6. Encontrar el contorno más pequeño (para corriente)
        # largest_contour = max(contours, key=cv2.contourArea)
        smallest_contour = min(contours, key=cv2.contourArea)

        # 7. Ajuste de una línea al contorno más pequeño
        # [vx, vy, x, y] = cv2.fitLine(largest_contour, cv2.DIST_L2, 0, 0.01, 0.01)
        [vx, vy, x, y] = cv2.fitLine(smallest_contour, cv2.DIST_L2, 0, 0.01, 0.01)

        # Extraer los elementos individuales del vector (para corregir error y poder hacer operaciones aritméticas sobre el vector)
        x = x[0]
        y = y[0]
        vx = vx[0]
        vy = vy[0]

        # Calculamos dos puntos extremos de la línea para dibujarla
        x1 = int(x - 1000 * vx)
        y1 = int(y - 1000 * vy)
        x2 = int(x + 1000 * vx)
        y2 = int(y + 1000 * vy)

        # 8. Dibujar la línea sobre una copia de la imagen original
        result = cv2.line(image.copy(), (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Calcula el ángulo con el eje horizontal
        angle_deg = angle_with_horizontal(vx, vy)

        return result, angle_deg

    except Exception as e:
        print("Error en la detección de la aguja:", e)
        return None, None

# RECORTE DE LA REGIÓN DE INTERÉS (ROI)
def select_roi(frame):
    try:
        # Definir una región de interés (ROI)
        height, width, _ = frame.shape
        roi_top_left = (int(width * 0.20), int(height * 0.56)) # Ajusta la posicion superior-inzquierda
        roi_bottom_right = (int(width * 0.75), int(height * 0.63))   # Ajusta la posición inferior-derecha
        # Si with de arriba lo reduzco y el de abajo lo aumento, se aumenta en anchura el rectangulo
        # Si height de arriba la acerco a la height de abajo se disminuye altura.
        # Si height de arriba lo disminuyo y el de abajo lo mantengo, se hace más alta hacia arriba
        # Recorte de la ROI sobre imagen original para no coger contorno del rectángulo
        roi = frame[roi_top_left[1]:roi_bottom_right[1], roi_top_left[0]:roi_bottom_right[0]]

        # Haz una copia del frame original para no modificarlo directamente
        frame_with_roi = frame.copy()
        # Dibujar un rectángulo que muestra la ROI en la copia de imagen original
        cv2.rectangle(frame_with_roi, roi_top_left, roi_bottom_right, (255, 0, 0), 2)

        return frame_with_roi, roi

    except Exception as e:
        print("Error en la selección de ROI:", e)
        return None, None