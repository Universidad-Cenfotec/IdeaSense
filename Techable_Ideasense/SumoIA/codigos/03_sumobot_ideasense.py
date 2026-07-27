import time

from ideaboard import IdeaBoard
from ideasense import IdeaSense

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement

from statemachine import StateMachine



# =====================================================
# HARDWARE
# =====================================================

ib = IdeaBoard()

idea = IdeaSense()



# =====================================================
# BLE
# =====================================================

ble = BLERadio()

ble.name = "Sumobot"

print("Nombre BLE:", ble.name)


uart = UARTService()

advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)

print("Esperando conexión BLE...")



# =====================================================
# VARIABLES
# =====================================================

comando = "STOP"



# =====================================================
# IDEASENSE MATRIX
# =====================================================


def clear_matrix():

    for r in range(5):
        for c in range(5):
            idea.matrix[c,r] = 0



def pixel(x,y):

    if 0 <= x < 5 and 0 <= y < 5:

        idea.matrix[x,y] = 1



# -----------------------------------------------------
# STOP
# -----------------------------------------------------

def mostrar_stop():

    clear_matrix()

    pixel(0,0)
    pixel(1,1)
    pixel(2,2)
    pixel(3,3)
    pixel(4,4)

    pixel(4,0)
    pixel(3,1)
    pixel(1,3)
    pixel(0,4)



# -----------------------------------------------------
# AVANZAR ↑
# -----------------------------------------------------

def mostrar_avanzar():

    clear_matrix()


    pixel(2,0)

    pixel(1,1)
    pixel(2,1)
    pixel(3,1)

    pixel(2,2)

    pixel(2,3)

    pixel(2,4)



# -----------------------------------------------------
# DERECHA →
# -----------------------------------------------------

def mostrar_derecha():

    clear_matrix()


    pixel(0,2)
    pixel(1,2)
    pixel(2,2)
    pixel(3,2)

    pixel(3,1)

    pixel(4,2)

    pixel(3,3)



# -----------------------------------------------------
# IZQUIERDA ←
# -----------------------------------------------------

def mostrar_izquierda():

    clear_matrix()


    pixel(4,2)
    pixel(3,2)
    pixel(2,2)
    pixel(1,2)

    pixel(1,1)

    pixel(0,2)

    pixel(1,3)




# =====================================================
# MOVIMIENTOS ROBOT
# =====================================================


def stop():

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

    ib.pixel = (0,0,0)

    mostrar_stop()

    print("STOP")



def avanzar():

    ib.motor_1.throttle = 0.5
    ib.motor_2.throttle = 0.5

    ib.pixel = (0,255,0)

    mostrar_avanzar()

    print("AVANZANDO")



def derecha():

    ib.motor_1.throttle = 0.4
    ib.motor_2.throttle = -0.4

    ib.pixel = (255,255,0)

    mostrar_derecha()

    print("DERECHA")



def izquierda():

    ib.motor_1.throttle = -0.4
    ib.motor_2.throttle = 0.4

    ib.pixel = (0,0,255)

    mostrar_izquierda()

    print("IZQUIERDA")




# =====================================================
# ESTADOS
# =====================================================


def estado_stop():

    global comando

    stop()


    if comando == "AVANZAR":
        return "AVANZAR"


    if comando == "DERECHA":
        return "DERECHA"


    if comando == "IZQUIERDA":
        return "IZQUIERDA"


    return "STOP"





def estado_avanza():

    global comando

    avanzar()


    if comando == "STOP":
        return "STOP"


    if comando == "DERECHA":
        return "DERECHA"


    if comando == "IZQUIERDA":
        return "IZQUIERDA"


    return "AVANZAR"





def estado_derecha():

    global comando

    derecha()


    if comando == "STOP":
        return "STOP"


    if comando == "AVANZAR":
        return "AVANZAR"


    if comando == "IZQUIERDA":
        return "IZQUIERDA"


    return "DERECHA"





def estado_izquierda():

    global comando

    izquierda()


    if comando == "STOP":
        return "STOP"


    if comando == "AVANZAR":
        return "AVANZAR"


    if comando == "DERECHA":
        return "DERECHA"


    return "IZQUIERDA"




# =====================================================
# MAQUINA DE ESTADOS
# =====================================================


sm = StateMachine("STOP")


sm.add_state("STOP", estado_stop)

sm.add_state("AVANZAR", estado_avanza)

sm.add_state("DERECHA", estado_derecha)

sm.add_state("IZQUIERDA", estado_izquierda)




# =====================================================
# LOOP PRINCIPAL
# =====================================================


conectado = False


while True:


    # ----------------------------
    # Estado BLE
    # ----------------------------

    if ble.connected and not conectado:

        conectado = True

        print("BLE conectado")



    elif not ble.connected and conectado:

        conectado = False

        print("BLE desconectado")



    # ----------------------------
    # Leer comando BLE
    # ----------------------------

    if ble.connected:


        if uart.in_waiting:


            data = uart.readline()


            if data:

                try:

                    comando = data.decode("utf-8").strip()

                    print("Comando recibido:", comando)


                except Exception as e:

                    print("Error BLE:",e)



    # ----------------------------
    # Ejecutar estado
    # ----------------------------

    sm.step()


    time.sleep(0.05)
