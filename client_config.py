
from pyupdater.client import Client

def get_client():
    return Client({
        'APP_NAME': 'YoutubeMP3App',
        'APP_VERSION': '1.0.0',
        'UPDATE_URLS': ['https://raw.githubusercontent.com/gabrielleite12/swt-desktop/main/updates/'],
        'PUBLIC_KEY': 'INSIRA_SUA_CHAVE_PUBLICA_AQUI'
    })
