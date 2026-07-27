import time
import board

from ideaboard import IdeaBoard

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC


ib = IdeaBoard()


# -----------------------
# BLE
# -----------------------

ble = BLERadio()

ble.name = "Sumobot"

uart = UARTService()

advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)



# -----------------------
# GIROSCOPIO
# -----------------------

i2c = board.I2C()

gyro = LSM6DS3TRC(i2c,0x6b)


comando = "STOP"


# -----------------------
# MOVIMIENTOS
# -----------------------

def stop():

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

    ib.pixel = (0,0,0)



def avanzar():

    ib.motor_1.throttle = 0.3
    ib.motor_2.throttle = 0.3



def derecha():

    ib.motor_1.throttle = 0.2
    ib.motor_2.throttle = -0.2



def izquierda():

    ib.motor_1.throttle = -0.2
    ib.motor_2.throttle = 0.2



# -----------------------
# LOOP
# -----------------------

while True:


    # recibir BLE

    if ble.connected:

        if uart.in_waiting:

            data = uart.readline()

            if data:

                comando = data.decode().strip()

                print(comando)



    # ejecutar comando


    if comando == "STOP":

        stop()


    elif comando == "AVANZAR":

        avanzar()


    elif comando == "DERECHA":

        derecha()


    elif comando == "IZQUIERDA":

        izquierda()


    time.sleep(0.02)
