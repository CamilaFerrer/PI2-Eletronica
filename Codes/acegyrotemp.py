# -*- coding: utf-8 -*-

from mpu6050 import mpu6050

sensor = mpu6050(0x68)

acce = sensor.get_accel_data()
gyro = sensor.get_gyro_data()
temp = sensor.get_temp()


print("Ax: {a_x} m/s²".format(a_x=round(accel['x'],1)))
print("Ay: {a_y} m/s²".format(a_y=round(accel['y'],1)))
print("Gx: {g_x} °".format(g_x=round(gyro['x'],0)))
print("Gy: {g_y} °".format(g_y=round(gyro['y'],0)))
print("Temperatira: {temp} °C".format(temp=round(temp,1)))

