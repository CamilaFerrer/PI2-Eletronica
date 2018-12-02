#!/usr/bin/env python
from hx711 import HX711
import RPi.GPIO as GPIO
import time

try:
	hx = HX711(dout_pin=5, pd_sck_pin=6)
	data = hx.get_raw_data_mean(times=1)
	result = hx.zero(times=10)
	data = hx.get_data_mean(times=10)

	input('Coloque um peso conhecido e pressione ENTER')
	data = hx.get_data_mean(times=10)
	hx.set_scale_ratio(scale_ratio=-160)
	if data != False:
		known_weight_grams = float(input('Escreva quantas gramas são e pressione ENTER: '))
		ratio = data / known_weight_grams
		hx.set_scale_ratio(scale_ratio=ratio)
	else:
		raise ValueError('Não foi possível calcular a tara da balança')

	try:
		while True:
			peso = round(hx.get_weight_mean(6), 2)
			if peso < 0:
				peso = 0
			print('Peso: ' + str(peso) + ' g')
			time.sleep(0.5)
	except (KeyboardInterrupt, SystemExit):
		pass
	
	
except (KeyboardInterrupt, SystemExit):
	print('Finalizando peso...')
	
finally:
	GPIO.cleanup()

