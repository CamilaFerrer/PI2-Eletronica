from mpu6050 import mpu6050

sensor = mpu6050(0x68)

acce = sensor.get_accel_data()
gyro = sensor.get_gyro_data()
temp = sensor.get_temp()


print("Ax: {a_x} m/s² | Ay: {a_y} m/s² |Az: {a_z} m/s²".format(a_x=round(accel[0],1),a_y=round(accel[1],1), a_z=round(accel[2],1))
print("Gx: {g_x} º    | Gy: {g_y} º    |Gz: {g_z} º".format(g_x=round(gyro[0],0),g_y=round(gyro[1],0), g_z=round(gyro[2],0))
print("Temperatira: {temp} ºC".format(temp=round(temp,1)))

