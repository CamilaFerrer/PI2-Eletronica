import RPi.GPIO as GPIO
import time
import os
import integrate_api
import datetime

TRIGGER = 23
ECHO = 24

def distance():
    GPIO.output(TRIGGER, True)
 
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
 
    StartTime = time.time()
    StopTime = StartTime
 
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return round(distance, 1)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print "Leitura do volume iniciando... "

dist_pen = distance()
dist_ult = distance()

try:
	while True:
		dist_atu = distance()

		prop1 = abs(dist_pen / dist_ult)
		prop2 = abs(dist_ult / dist_atu)

		if 0.95 < max(prop1, prop2) < 1.05:
			if 0 < dist_atu and dist_atu < 50:
				print ("Distancia: " + str(dist_atu) + " cm")
				if dist_atu < 10:
					print("LIXO CHEIO!!")
		time.sleep(0.5)

		dist_pen = dist_ult
		dist_ult = dist_atu
except (KeyboardInterrupt, SystemExit):
	GPIO.cleanup()

