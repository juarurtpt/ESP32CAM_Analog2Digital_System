# Comprueba si Docker Desktop ya está instalado
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "Docker Desktop ya esta instalado en este sistema."
} else {
    # Descarga Docker Desktop desde la URL oficial
    $dockerInstallerUrl = "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe"
    $installerPath = "$env:TEMP\DockerDesktopInstaller.exe"
    Invoke-WebRequest -Uri $dockerInstallerUrl -OutFile $installerPath

    # Instala Docker Desktop
    Write-Host "Instalando Docker Desktop..."
    Start-Process -FilePath $installerPath -Wait

    # Limpia el archivo de instalación después de la instalación
    Remove-Item -Path $installerPath
}

# Comprueba si Docker Compose ya está instalado
if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    Write-Host "Docker Compose ya esta instalado en este sistema."
} else {
    # Descarga la última versión de Docker Compose
    $dockerComposeUrl = "https://github.com/docker/compose/releases/latest/download/docker-compose-Windows-x86_64.exe"
    $dockerComposePath = "$env:ProgramFiles\Docker\docker-compose.exe"
    Invoke-WebRequest -Uri $dockerComposeUrl -OutFile $dockerComposePath

    # Agrega Docker Compose al PATH del sistema
    $env:Path += ";$env:ProgramFiles\Docker"

    Write-Host "Docker Compose se ha instalado correctamente."
}

Write-Host "La instalacion de Docker Desktop y Docker Compose se ha completado."
