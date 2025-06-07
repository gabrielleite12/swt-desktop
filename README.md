
# YouTube MP3 Downloader com Auto-Atualização

Este projeto usa PyUpdater para baixar MP3 do YouTube e verificar atualizações automaticamente a partir deste repositório.

## Requisitos

- Python 3.9+
- yt_dlp
- pyupdater
- ffmpeg

## Como usar

1. Instale dependências: `pip install -r requirements.txt`
2. Gere as chaves: `pyupdater keys -c`
3. Copie a chave pública nos arquivos `client_config.py` e `.pyupdater/config.py`
4. Gere o executável: `pyinstaller main.spec`
5. Empacote: `pyupdater pkg -p dist/main.exe -n YoutubeMP3App -v 1.0.0`
6. Publique: `pyupdater build && pyupdater sign` e envie a pasta `deploy/updates` para o GitHub
