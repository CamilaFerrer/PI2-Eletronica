import os as OS
from gps import gps
from time import *
import time
import threading

gpsd = None

OS.system('clear')

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd
    gpsd = gps(mode=1)
    self.current_value = None
    self.running = True

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next()

if __name__ == '__main__':
  gpsp = GpsPoller()
  try:
    gpsp.start()
    while True:

      OS.system('clear')

      print('Leitura do GPS')
      print('----------------------------------------')
      print('Latitude: ' , gpsd.fix.latitude)
      print('Longitude: ' , gpsd.fix.longitude)
      print('Fuso horario (UTC): ' , gpsd.utc,' + ', gpsd.fix.time)
      print('Altitude (m): ' , gpsd.fix.altitude)
      print('----------------------------------------')
      print('Erros com 95% de confianca')
      print('Estimativa de velocidade (m/s): ' , gpsd.fix.eps)
      print('Longitude (m):' , gpsd.fix.epx)
      print('Altitude (m):' , gpsd.fix.epv)
      print('Fuso horario (UTC): ' , gpsd.fix.ept)
      print('----------------------------------------')
      print('Velocidade (m/s): ' , gpsd.fix.speed)
      print('Subindo/Descendo: ' , gpsd.fix.climb)
      print('Angulo com o norte verdadeiro: ' , gpsd.fix.track)
      print('Modo: ' , gpsd.fix.mode)
      print('Lista de Satelites: ' , gpsd.satellites)
      print('----------------------------------------')

      time.sleep(1)

  except(KeyboardInterrupt, SystemExit):
    print('Desligando GPS...')
