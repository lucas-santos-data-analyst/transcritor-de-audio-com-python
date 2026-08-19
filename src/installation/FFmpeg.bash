#!/bin/bash

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    echo "Detectado ambiente Windows. Instalando via winget..."
    winget install FFmpeg
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detectado Linux. Instalando via apt..."
    sudo apt update && sudo apt install -y ffmpeg
else
    echo "Sistema operacional não suportado: $OSTYPE"
fi