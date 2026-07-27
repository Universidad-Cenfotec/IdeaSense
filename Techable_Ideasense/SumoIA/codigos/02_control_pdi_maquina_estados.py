import time
import board

from ideaboard import IdeaBoard

from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

from statemachine import StateMachine



# =====================================================
# HARDWARE
# =====================================================

ib = IdeaBoard()


# =====================================================
# GIROSCOPIO
# =====================================================

i2c = board.I2C()

gyro = LSM6DS3TRC(i2c,0x6b)



# =====================================================
# BLE
# =====================================================

ble = BLERadio()

ble.name = "Sumobot"


uart = UARTService()

advertisement = ProvideServicesAdvertisement(uart)


ble.start_advertising(advertisement)


print("Esperando BLE")



# =====================================================
# VARIABLES
# =====================================================

comando = "STOP"

drift = 0



# =====================================================
# PDI
# =====================================================

Kp = 0.15
Ki = 0.8
Kd = 0.05


error_anterior = 0

error_integral = 0


velocidad_base = 0.5


tiempo_anterior = time.monotonic()



# =====================================================
# CALIBRAR DRIFT
# =====================================================

def calibrar_drift():

    print("Calibrando...")


    suma = 0
    muestras = 0


    inicio = time.monotonic()


    while time.monotonic()-inicio < 4:


        valor = gyro.gyro[2]


        if abs(valor)<0.008:

            suma += valor
            muestras += 1


        time.sleep(0.005)



    if muestras:

        resultado = suma/muestras

    else:

        resultado = 0



    print("Drift:",resultado)


    return resultado




# =====================================================
# PDI NO BLOQUEANTE
# =====================================================

def avanzar_pdi():

    global error_anterior
    global error_integral
    global tiempo_anterior


    ahora = time.monotonic()


    dt = ahora - tiempo_anterior


    tiempo_anterior = ahora



    if dt <= 0:

        dt = 0.01



    error = gyro.gyro[2] - drift



    error_integral += error * dt



    error_integral = max(
        -1,
        min(
            1,
            error_integral
        )
    )



    derivada = (
        error-error_anterior
    )/dt



    correccion = (

        Kp*error
        +
        Ki*error_integral
        +
        Kd*derivada

    )



    correccion = max(
        -0.3,
        min(
            0.3,
            correccion
        )
    )



    motor1 = velocidad_base + correccion

    motor2 = velocidad_base - correccion



    motor1 = max(
        -1,
        min(
            1,
            motor1
        )
    )


    motor2 = max(
        -1,
        min(
            1,
            motor2
        )
    )



    ib.motor_1.throttle = motor1

    ib.motor_2.throttle = motor2



    ib.pixel=(0,255,0)



    error_anterior = error




# =====================================================
# MOVIMIENTOS
# =====================================================

def reset_pdi():

    global error_anterior
    global error_integral


    error_anterior = 0

    error_integral = 0




def stop():

    ib.motor_1.throttle=0

    ib.motor_2.throttle=0


    ib.pixel=(0,0,0)


    reset_pdi()



def derecha():

    ib.motor_1.throttle=0.4

    ib.motor_2.throttle=-0.4


    ib.pixel=(255,255,0)



def izquierda():

    ib.motor_1.throttle=-0.4

    ib.motor_2.throttle=0.4


    ib.pixel=(0,0,255)




# =====================================================
# ESTADOS
# =====================================================


def estado_calibrando():

    global drift


    ib.pixel=(255,0,0)


    drift=calibrar_drift()


    ib.pixel=(0,255,0)


    return "DESCONECTADO"




def estado_desconectado():

    stop()


    if ble.connected:

        return "STOP"



    return "DESCONECTADO"




def estado_stop():

    stop()


    if not ble.connected:

        return "DESCONECTADO"



    if comando=="AVANZAR":

        return "AVANZAR"



    if comando=="DERECHA":

        return "DERECHA"



    if comando=="IZQUIERDA":

        return "IZQUIERDA"



    return "STOP"




def estado_avanzar():

    avanzar_pdi()


    if not ble.connected:

        return "DESCONECTADO"



    if comando=="STOP":

        return "STOP"



    if comando=="DERECHA":

        reset_pdi()

        return "DERECHA"



    if comando=="IZQUIERDA":

        reset_pdi()

        return "IZQUIERDA"



    return "AVANZAR"




def estado_derecha():

    derecha()


    if comando=="STOP":

        return "STOP"



    if comando=="AVANZAR":

        reset_pdi()

        return "AVANZAR"



    if comando=="IZQUIERDA":

        return "IZQUIERDA"



    return "DERECHA"




def estado_izquierda():

    izquierda()


    if comando=="STOP":

        return "STOP"



    if comando=="AVANZAR":

        reset_pdi()

        return "AVANZAR"



    if comando=="DERECHA":

        return "DERECHA"



    return "IZQUIERDA"





# =====================================================
# MAQUINA DE ESTADOS
# =====================================================

sm = StateMachine("CALIBRANDO")


sm.add_state(
    "CALIBRANDO",
    estado_calibrando
)


sm.add_state(
    "DESCONECTADO",
    estado_desconectado
)


sm.add_state(
    "STOP",
    estado_stop
)


sm.add_state(
    "AVANZAR",
    estado_avanzar
)


sm.add_state(
    "DERECHA",
    estado_derecha
)


sm.add_state(
    "IZQUIERDA",
    estado_izquierda
)




# =====================================================
# LOOP PRINCIPAL
# =====================================================

conectado=False



while True:


    # ------------------------
    # BLE
    # ------------------------

    if ble.connected and not conectado:

        conectado=True

        print("BLE conectado")



    if not ble.connected and conectado:

        conectado=False

        print("BLE perdido")



    # ------------------------
    # Leer comando
    # ------------------------

    if ble.connected:


        if uart.in_waiting:


            data=uart.readline()


            if data:


                try:

                    comando=data.decode(
                        "utf-8"
                    ).strip()


                    print(
                        "CMD:",
                        comando
                    )


                except:

                    pass



    # ------------------------
    # Máquina estados
    # ------------------------

    sm.step()



    time.sleep(0.01)
