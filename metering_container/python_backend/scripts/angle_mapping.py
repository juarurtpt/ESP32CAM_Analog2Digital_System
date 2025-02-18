
import numpy as np

# FUNCIÓN MAPEO ÁNGULO(º) -> TEMPERATURA(Cº)
def map_angle_to_temperature(angle_deg):
    try:
        # Verificar que el ángulo esté dentro del rango permitido
        if angle_deg < 25.0 or angle_deg > 140.0:
            print("El ángulo debe estar entre 43.0 y 137.0 grados.")
            return 0

        # Calcular el valor de temperatura correspondiente
        if angle_deg >= 137.0:
            temperature = 0  # Temperatura de 0 grados Celsius para ángulos mayores o iguales a 137.0
        elif angle_deg <= 43.0:
            temperature = 500  # Temperatura de 500 grados Celsius para ángulos menores o iguales a 43.0
        else:
            # Calcular la temperatura aproximada según la lógica proporcionada
            # En nuestro medidor, la temperatura aumenta en 10 grados Celsius por cada dos grados aprox. que se disminuye el ángulo desde 140 hasta llegar a 45,
            # donde la temperatura sería de 500 grados Celsius.
            temperature = round(max(0, (137.0 - angle_deg) * 10 / 1.875))
            # Aumenta 10 grados por cada 1.82 grados de disminución del ángulo
            # También redondea para dar valor de temperatura entero
        return temperature

    except Exception as e:
        print("Error en la creación del mapeo de temperatura:", e)
        return {}

# FUNCIÓN MAPEO ÁNGULO(º) -> CORRIENTE(mA)
def create_current_mapping(angle_deg):
    try:
        # Verificar que el ángulo esté dentro del rango posible de la aguja en el medidor
        # En Aguja 1 de PRESIÓN-CORRIENTE, con ayuda del transportador vemos que su rango valido min-max es 47-130:
        if angle_deg < 47.0 or angle_deg > 130.0:
            print("El ángulo debe estar entre 47 y 130 grados.")
            return 0

        # Calcular el valor de corriente correspondiente
        if angle_deg >= 128.0:
            current = 0.0  # Para ángulos mayores a 128 grados, corriente de 0 mA0
        elif angle_deg <= 50.0:
            current = 10.0  # Para ángulos menores a 50 grados, corriente de 10 mA
        else:
            # Para ángulos entre 50 y 130 grados, calculamos la corriente de manera aproximada según la lógica descubierta:
            # En nuestro medidor, aprox. la corrriente aumenta 1 mA por cada 8.15 grados de disminución de ángulo,
            # desde 130 a 49, donde la corriente sería de 10 mA.
            current = round(max(0, (130.0 - angle_deg) * 1 / 8.05), 1)
            # Aumento de 1 mA por cada 8.15 grados de disminución del ángulo
            # Redondeo a un decimal para ajustar precision
        return current

    except Exception as e:
        print("Error en la creación del mapeo de corriente:", e)
        return {}


# CÁLCULO DEL ÁNGULO DE LA AGUJA
def angle_with_horizontal(vx, vy):
    try:
        # Si vy es negativo, invertimos la dirección del vector
        #if vy < 0:
        #    vx = -vx
        #    vy = -vy

        # Calcula el ángulo que la línea de la aguja forma con el eje horizontal
        angle_rad = np.arctan2(vy, vx)  # Ángulo en radianes
        angle_deg = np.degrees(angle_rad)  # Ángulo en grados

        # Redondea el ángulo a las centésimas y obtén su valor absoluto
        ## angle_rounded = round(angle_deg, 1) # Redondeamos a las décimas, 1 decimal
        ## angle_abs = abs(angle_rounded)  # Valor absoluto

        ## return angle_abs

        # Normalizar el ángulo para que siempre esté entre 0 y 180°
        if angle_deg < 0:
            angle_deg += 180  # Ajuste para que todos los ángulos estén en el rango [0, 180]

        # Ajuste para que el ángulo se mida correctamente en el contexto del reloj
        corrected_angle = angle_deg - 180

        angle_abs = abs(corrected_angle)  # Valor absoluto

        # Redondeamos a 1 decimal
        return round(angle_abs, 1)

    except Exception as e:
        print("Error en el cálculo del ángulo con el eje horizontal:", e)
        return None