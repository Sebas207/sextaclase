from threading import *
import requests 
from datetime import datetime
import time
class Bot:

    def observadorRelog(self):
        while(True):
            time.sleep(1)
            now = datetime.now()
            horaActual = now.strftime('%H:%M:%S')

            if horaActual == '12:03:00':
                self.llamarSuperHerore("batman")
            if horaActual == '12:03:30':
                self.llamarSuperHerore("superman")
        
    def llamarSuperHerore(self, superheroe):
        url = str("http://localhost:4000/saludo/{}").format(superheroe)
        r = request.get(url)
        if r.status_code == 200:
            print(r.text)
    
    def iniciar(self):
        t = Timer(3.0, self.observadorRelog)
        t.start()


if __name__ =='__main__':
    try:
        b = Bot()
        b.iniciar()

    except KeyboardInterrupt:
        print("saliendo")
        exit()