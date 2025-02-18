
# Se importan las funciones necesarias de los otros módulos .py
from camera_connection import establecer_conexion, streaming
from angle_mapping import map_angle_to_temperature

# Bloque principal donde se establecen las acciones del script
# La siguiente línea se emplea en Python para indicar que el código debajo de ella solo debe ejecutarse cuando el script
# se ejecuta directamente y no cuando se importa como un módulo en otro script
def main():
    # Asignación de URL de la cámara que apunta al medidor de Temperatura a la que se conectará el script
    # IP dada en red de casa
    # url_cam_2 = "http://192.168.1.138"
    # IP dada en red de movil
    # url_cam_2 = "http://192.168.237.73"
    # Nueva IP dada en red movil
    url_cam_2 = "http://192.168.255.73"

    # Establecimiento de conexión con la cámara de la Temperatura (CAM2)
    # Se crea un objeto VideoCapture para capturar el flujo de vídeo de la cámara.
    # La URL se compone de la dirección IP del ESP32 y el puerto :81/stream que es donde normalmente se transmite el vídeo en estos dispositivos.
    video_cam_2 = establecer_conexion(url_cam_2)

    # Comienzo de video streaming con CAM1:
    # Si la variable video_capture recibe información de captura de vídeo lo sigue haciendo en bucle:
    if video_cam_2 is not None:
        # Si la conexión se establece correctamente, comenzar a capturar el vídeo
        streaming(video_cam_2, map_angle_to_temperature, "temperature")
        # Le pasamos parámetros adicionales para manejar el caso específico de la temperatura.
    else:
        print("Error: No se pudo establecer la conexión con la cámara 2.")


if __name__ == '__main__':
    main()