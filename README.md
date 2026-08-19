# 🎙️ Transcritor de Áudio para Texto (Whisper + uv)

Este repositório contém uma solução simples e eficiente para transcrição automática de arquivos de áudio e vídeo em texto (formatos como `.mp3`, `.wav`, `.m4a`, `.mp4`, `.mkv`, etc.), utilizando o modelo **OpenAI Whisper** para processamento local e o **uv** para gerenciamento ultrarrápido de pacotes Python.

---


### Instalando o FFmpeg

O **FFmpeg** é essencial para que o Whisper consiga ler, manipular e converter diferentes formatos de áudio e vídeo.

####  Windows
Abra o **PowerShell** ou **Prompt de Comando** como **Administrador** e rode:

```bash
winget install FFmpeg
```

#### 🐧 Linux
No Linux, utilize o gerenciador de pacotes padrão da sua distribuição:

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install -y ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

### Sincronizando Dependências
Para sincronizar as dependências utilizadas nesse projeto execute o comando no terminal, no diretório do seu projeto:

```bash
uv sync
```