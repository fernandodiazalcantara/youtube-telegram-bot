import requests
import time
from flask import Flask
from threading import Thread

API_KEY = "AIzaSyCs5ZDe7esZjfRYZySCMVMg33a5a79EYSI"
VIDEO_ID = "41tQYEA9Kas"
TELEGRAM_TOKEN = "8443868184:AAGPPRBNqqr8HrBoucCylpOwqWrbjJ9XtSI"
TELEGRAM_CHAT_ID = "6193435608"
UMBRAL_VISTAS = 650000
app = Flask('')

@app.route('/')
def home():
    return "Bot activo"

def run():
    app.run(host='0.0.0.0', port=3000)

def mantener_vivo():
    t = Thread(target=run)
    t.start()

mantener_vivo()

def obtener_vistas():
    url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={VIDEO_ID}&key={API_KEY}'
    r = requests.get(url)
    data = r.json()
    vistas = int(data['items'][0]['statistics']['viewCount'])
    return vistas

def enviar_mensaje(mensaje):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': mensaje}
    requests.post(url, data=payload)

# ✅ Control de vistas anteriores para evitar duplicados
vistas_anteriores = None

while True:
    vistas = obtener_vistas()
    print(f'Vistas actuales: {vistas}')
    
    # Solo envía si las vistas cambiaron
    if vistas != vistas_anteriores:
        enviar_mensaje(f'Vistas actuales: {vistas}')
        if vistas >= UMBRAL_VISTAS:
            enviar_mensaje(f'avanzó')
        vistas_anteriores = vistas  # ✅ Actualiza el estado

    time.sleep(1600)





