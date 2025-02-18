# Ruta predeterminada del ejecutable de VcXsrv
$vcxsrvPath = "C:\Program Files\VcXsrv\vcxsrv.exe"

# Ruta al instalador en el mismo directorio que el script
$installer = Join-Path -Path (Get-Location) -ChildPath "vcxsrv-64.1.20.14.0.installer.exe"

# Parámetros para ejecutar VcXsrv
$arguments = ":0 -multiwindow -clipboard -wgl -ac"

# Función para ejecutar VcXsrv
function Start-VcXsrv {
    Write-Host "Ejecutando VcXsrv con los parametros especificados..."
    Start-Process -FilePath $vcxsrvPath -ArgumentList $arguments -NoNewWindow -PassThru
    Write-Host "VcXsrv esta ejecutandose en segundo plano."
}

# Verificar si VcXsrv ya está instalado
if (Test-Path $vcxsrvPath) {
    Write-Host "VcXsrv ya esta instalado."
    Start-VcXsrv
} else {
    Write-Host "VcXsrv no esta instalado. Verificando instalador..."

    # Comprobar si el instalador existe en el directorio actual
    if (Test-Path $installer) {
        Write-Host "Instalador encontrado. Procediendo con la instalacion..."

        # Ejecutar el instalador en modo silencioso
        Start-Process -FilePath $installer -ArgumentList "/silent", "/verysilent" -NoNewWindow -Wait

        Write-Host "Instalacion de VcXsrv completada."

        # Verificar si el ejecutable ahora está disponible
        if (Test-Path $vcxsrvPath) {
            Start-VcXsrv
        } else {
            Write-Host "La instalacion fallo o no se encontró el ejecutable de VcXsrv. Verifica el instalador."
        }
    } else {
        Write-Host "No se encontro el instalador en el directorio actual. Asegurese de que el archivo 'vcxsrv-64.1.20.14.0.installer.exe' este en el mismo directorio que este script."
    }
}
