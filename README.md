## **README\_SETUP**
**ESP32CAM_Analog2Digital_System** by juarurtpt

## Índice

1. [Descripción general](#descripción-general)
2. [Prerrequisitos](#prerrequisitos)
3. [Configuración de WSL y virtualización](#configuración-de-wsl-y-virtualización)
4. [Habilitar la ejecución de scripts (PowerShell)](#habilitar-la-ejecución-de-scripts-powershell)
5. [Clonar el repositorio](#clonar-el-repositorio)
6. [Instalación de Docker y Docker Compose](#instalación-de-docker-y-docker-compose)
7. [Verificar la instalación de Docker](#verificar-la-instalación-de-docker)
8. [Instalación de XLaunch (Servidor X para Windows)](#instalación-de-xlaunch-servidor-x-para-windows)
9. [Revertir la política de ejecución](#revertir-la-política-de-ejecución)
10. [Despliegue del contenedor (Python-OpenCV-Node.js-Node-RED-DashboardUI)](#despliegue-del-contenedor-python-nodejs-node-red)
11. [Acceso al dashboard de Node-RED](#acceso-al-dashboard-de-node-red)
12. [Notas y Recomendaciones Finales](#notas-y-recomendaciones-finales)

---

## Descripción general

Este documento describe los pasos necesarios para la instalación y despliegue del sistema de "Digitalización de lecturas analógicas mediante visión computacional a través del módulo ESP32-CAM WiFi y contenerización para visualización remota en Node-RED" realizado como mi Trabajo Fin de Estudios en la UPCT, proyecto el cual utiliza un contenedor Docker (Python, OpenCV, Node.js, Node-RED, etc.) en un entorno Windows. Siguiendo estas instrucciones, podrás:

- Habilitar WSL (Windows Subsystem for Linux) y la virtualización en tu BIOS.
- Configurar la política de ejecución de scripts en PowerShell para permitir la instalación automatizada.
- Instalar Docker Desktop y Docker Compose.
- Instalar XLaunch para gestionar entornos gráficos de Linux en Windows.
- Desplegar el contenedor y acceder al dashboard de Node-RED en tu navegador.

---

## Prerrequisitos

- **Windows 10/11** con soporte de WSL.
- **Virtualización habilitada en la BIOS** (por ejemplo, Intel VT-x o AMD-V).
- **Conexión a Internet** durante la instalación.
- **Permisos de administrador** en Windows (PowerShell ejecutado como administrador).

---

## Configuración de WSL y virtualización

1. **Habilitar WSL en Windows**\
   Abre la PowerShell como administrador y ejecuta:
   ```powershell
    > dism.exe /online /enable-feature /featurename\:Microsoft-Windows-Subsystem-Linux /all /norestart
   ````
2. **Reiniciar el sistema** para completar los cambios.
3. **Habilitar la virtualización en la BIOS**  
- Durante el arranque del equipo, accede a la BIOS (tecla F10, ESC u otra dependiendo del fabricante).
- Asegúrate de que la opción **Virtualization Technology** esté activada.
- Guarda los cambios antes de salir de la BIOS.
4. **Actualizar WSL**  
Una vez reiniciado el sistema, vuelve a PowerShell como administrador y ejecuta:
    ```powershell
    > wsl --update --web-download
    ````

---

## Habilitar la ejecución de scripts (PowerShell)

1. Abre **Windows PowerShell** como administrador.
2. Ejecuta el siguiente comando:
   ```powershell
   > Set-ExecutionPolicy RemoteSigned
   ```
3. Acepta los cambios pulsando la tecla **S** cuando se te solicite.

> **Nota:** Este paso es temporal para permitir la ejecución de los scripts de instalación. Más adelante revertiremos la política de ejecución.

---

## Clonar el repositorio del proyecto

1. **Instala Git** (si todavía no lo tienes).
2. Abre la terminal o PowerShell en la ubicación deseada.
3. Clona tu repositorio (ajusta la URL según tu caso):
   ```bash
    > git clone [https://github.com/juarurtpt/ESP32CAM_Analog2Digital_System.git](https://github.com/juarurtpt/ESP32CAM_Analog2Digital_System.git)
    ````

---

## Instalación de Docker y Docker Compose
1. Navega al directorio donde se encuentra el script de instalación de Docker:
    ```powershell
    > cd C:\Users\tu_usuario\..\ESP32CAM_Analog2Digital_System\metering_container
    ````

2. Ejecuta el script de instalación:
   ```powershell
   > .\setup_docker.ps1
   ```
   - **Tiempo estimado:** 7 minutos.
   - El script te pedirá presionar **INTRO** para comenzar con la instalación.
   - Al finalizar, se recomienda **reiniciar el PC**.

---

## Verificar la instalación de Docker

Ejecuta los siguientes comandos en PowerShell para comprobar la instalación:
    
```powershell
   > docker --version
   > docker-compose --version
   ```
    
---

## Instalación y ejecución de XLaunch (Servidor X para Windows)

Ejecuta el script para instalar e iniciar el Servidor X en segundo plano
   ```powershell
   .\setup_xserver.ps1
   ```
- Indeferentemente de que esté instalado, ejecutar script cada vez que se quiera lanzar servidor X.

---

## Revertir la política de ejecución

Ejecuta en PowerShell:

```powershell
> Set-ExecutionPolicy Default
```

---

## Despliegue del contenedor (Python-OpenCV-Node-RED)

1. Navega al directorio donde está el archivo `docker-compose.yml`:
   ```powershell
   > cd C:\Users\tu_usuario\..\ESP32CAM_Analog2Digital_System\metering_container
   ```
2. Ejecuta:
   ```powershell
   > docker-compose build --no-cache; docker-compose up -d
   ```

---

## Acceso al dashboard de Node-RED

Una vez el contenedor esté corriendo, accede desde el navegador a la siguiente URL: 
## http://localhost:1880/ui


---

## Notas y recomendaciones Finales

- Verifica que el motor de Docker y el servidor X estén corriendo antes de desplegar el contenedor.
- Para detener el contenedor, ejecuta:
  ```powershell
  > docker-compose down
  ```
- En caso de problemas con los puertos, revisa que no estén en uso.

**© 2025 juarurtpt. GITE-UPCT.**\
TFE: *Digitalización de lecturas analógicas mediante visión computacional a través del módulo ESP32-CAM WiFi y contenerización para visualización remota en Node-RED* 
