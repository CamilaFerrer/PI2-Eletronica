import RPi.GPIO as GPIO
import time
import sys

pin_out = int(sys.argv[1]) # 38
frequency = float(sys.argv[2])
duty_cycle = float(sys.argv[3])
sleep_time = float(sys.argv[4])
direction_port = int(sys.argv[5]) # 36
direction = float(sys.argv[6]) # 1 ou 0

GPIO.setwarnings(False)
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_out,GPIO.OUT)
GPIO.setup(direction_port,GPIO.OUT)

if direction:
    GPIO.output(direction_port, True)
else:
    GPIO.output(direction_port, False)


PWM = GPIO.PWM(pin_out,frequency)
PWM.start(duty_cycle)

if duty_cycle > 50:
	duty_cycle = 10
else:
	duty_cycle = 90

PWM.ChangeDutyCycle(duty_cycle)
time.sleep(sleep_time)


GPIO.cleanup()

