from camera_connection import establecer_conexion, streaming
from angle_mapping import create_current_mapping

def main():
    # Asignación de URL de la cámara que apunta al medidor de Corriente (mA)
    # url_cam_1 = "http://192.168.1.138"
    # IP dada en red de movil
    # url_cam_1 = "http://192.168.237.108"
    # Nueva IP dada en red movil
    url_cam_1 = "http://192.168.255.108"

    # Establecimiento de conexión con la cámara de la Corriente (CAM1)
    video_cam_1 = establecer_conexion(url_cam_1)

    # Comienzo de video streaming con CAM1:
    if video_cam_1 is not None:
        streaming(video_cam_1, create_current_mapping, "current")
    else:
        print("Error: No se pudo establecer la conexión con la cámara 1.")


if __name__ == '__main__':
    main()
