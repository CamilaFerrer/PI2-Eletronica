# -*- coding: utf-8 -*-

from mpu6050 import mpu6050
from hx711 import HX711
import RPi.GPIO as GPIO
from gps3 import gps3
import threading
import time
import math
import sys
import os

gps_sensor = None
running = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

START = 1
RUNNING = 3
STATUS = START

class bcolors:
	HEADER		= '\033[95m'
	OKBLUE		= '\033[94m'
	OKGREEN		= '\033[92m'
	WARNING		= '\033[93m'
	FAIL		= '\033[91m'
	ENDC		= '\033[0m'
	BOLD		= '\033[1m'
	UNDERLINE	= '\033[4m'

class SensorPeso(threading.Thread):
	def __init__(self, PIN_OUT=29, PIN_SCK=31):
		threading.Thread.__init__(self)
		self.daemon = True
		self.HX711_SENSOR = HX711(PIN_OUT, PIN_SCK)
		data = self.HX711_SENSOR.get_raw_data_mean(times=1)
		result = self.HX711_SENSOR.zero(times=10)
		data = self.HX711_SENSOR.get_data_mean(times=10)
		self.done_setting = False
	
	def finish_setting(self):
		return self.done_setting
	
	def set(self, peso=None):

		data = self.HX711_SENSOR.get_data_mean(times=10)

		if(peso != None):
			raw_input('Coloque um peso conhecido e pressione ENTER')

		if data != False:
			if(peso != None):
				tara = float(raw_input('Escreva a quantidade de gramas e pressione ENTER: '))
			else:
				tara = peso
			ratio = data / tara
			self.HX711_SENSOR.set_scale_ratio(scale_ratio=ratio)
		else:
			raise ValueError('Não foi possível calcular a tara da balanca')
		self.done_setting = True
		
		
	def run(self):
		try:
			peso_pen = int(self.HX711_SENSOR.get_weight_mean(6))
			
			if peso_pen < 0:
				peso_pen = 0

			peso_ult = int(self.HX711_SENSOR.get_weight_mean(6))
			if peso_ult < 0:
				peso_ult = 0

			while running:
				peso_atual = int(self.HX711_SENSOR.get_weight_mean(6))
				
				if peso_atual < 0:
					peso_atual = 0

				if peso_ult > 0:
					prop1 = abs(peso_pen / peso_ult)
				else:
					prop1 = 0

				if peso_atual > 0:
					prop2 = abs(peso_ult / peso_atual)
				else:
					prop2 = 0

				if 0.80 < max(prop1, prop2) < 1.20:
					print('Peso: {peso}g'.format(peso=peso_atual))
					
				peso_pen = peso_ult
				peso_ult = peso_atual

				time.sleep(2)
		except (KeyboardInterrupt, SystemExit):
			pass

class SensorVolume(threading.Thread):
	def __init__(self,  TRIGGER = 16, ECHO = 18):
		threading.Thread.__init__(self)
		self.daemon = True
		self.TRIGGER = TRIGGER
		self.ECHO = ECHO
		GPIO.setup(self.TRIGGER, GPIO.OUT)
		GPIO.setup(self.ECHO, GPIO.IN)
	
	def distance(self):
		GPIO.output(self.TRIGGER, True)
	 
		time.sleep(0.1)
		GPIO.output(self.TRIGGER, False)
	 
		StartTime = time.time()
		StopTime = StartTime
	 
		while GPIO.input(self.ECHO) == 0:
			StartTime = time.time()
			time.sleep(0.5)
	 
		while GPIO.input(self.ECHO) == 1:
			StopTime = time.time()
			time.sleep(0.5)
	 
		TimeElapsed = StopTime - StartTime
		distance = (TimeElapsed * 34300) / 2
	 
		return round(distance, 1)

	def run(self):
		try:
			dist_pen = self.distance()
			dist_ult = self.distance()

			while running:
				dist_atual = self.distance()
				if dist_atual < 40:
					prop1 = abs(dist_pen / dist_ult)
					prop2 = abs(dist_ult / dist_atual)

					if 0.95 < max(prop1, prop2) < 1.05:
						volume_percent = (dist_atual * 100) / 40
						print ("Volume livre: {vol}% | Distancia: {dist} cm".format(vol=round(volume_percent,1),dist=dist_atual))
						
						if volume_percent < 40:
							print bcolors.BOLD + bcolors.WARNING + "LIXO CHEIO!\n" + bcolors.ENDC
							
				time.sleep(2)

				dist_pen = dist_ult
				dist_ult = dist_atual

		except (KeyboardInterrupt, SystemExit):
			pass

class SensorGPS(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True
		self.gps_socket = gps3.GPSDSocket()
		self.data_stream = gps3.DataStream()

	def run(self):
		self.gps_socket.connect()
		self.gps_socket.watch()

		for new_data in self.gps_socket:
			if new_data:
				self.data_stream.unpack(new_data)
				print('Longitude = {lon} °'.format(lon=self.data_stream.TPV['lon']))
				print('Latitude = {lat} °'.format(lat=self.data_stream.TPV['lat']))
			time.sleep(0.2)

class SensorMPU6050(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True
		self.sensor = mpu6050(0x68)

	def run(self):
		while running:
			temp = round(self.sensor.get_temp(),1)
			print("Temperatura: {temp} °C".format(temp=temp) )
			accel = self.sensor.get_accel_data()
			x = round(accel['x'],2)
			y = round(accel['y'],2)
			print("Ax: {valor} m/s²".format(valor=x) )
			print("Ay: {valor} m/s²".format(valor=y) )

			time.sleep(1)


# inicializando Sensores
peso = SensorPeso()
volume = SensorVolume()
acegyrotemp = SensorMPU6050()
sensor_gps = SensorGPS()

try:
	while True:
		if STATUS == START:
			running = True
			
			peso.start()
			volume.start()
			acegyrotemp.start()
			sensor_gps.start()
			
			STATUS = RUNNING

		time.sleep(0.1)

except(KeyboardInterrupt, SystemExit):
	running = False
	GPIO.cleanup()
