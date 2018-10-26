import RPi.GPIO as GPIO
import time
import sys

pin_out = 38
frequency = 1000
duty_cycle = float(sys.argv[1])
sleep_time = float(sys.argv[2])

# Configuração para não mostrar warnings na hora de rodar programa
GPIO.setwarnings(False)
 
# Configurando GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_out,GPIO.OUT)
 
# Configurando o PWM
PWM = GPIO.PWM(pin_out,frequency)
PWM.start(duty_cycle)

PWM.ChangeDutyCycle(duty_cycle)
time.sleep(sleep_time)

GPIO.cleanup()

