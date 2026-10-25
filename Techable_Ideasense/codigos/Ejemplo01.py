"""
Teachable IdeaSense — Ejemplo 01: pulgares
==========================================

Recibe por BLE (UART Nordic) la clase detectada por un modelo de Teachable
Machine en el navegador (Feliz, Triste, Nada) y muestra una carita en la
matriz mediante una máquina de estados. Requiere statemachine.py en /lib.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Conectarse desde la plataforma Teachable IdeaSense (dispositivo "IdeaSense").
Usa      : adafruit_ble, statemachine, idea.matrix
Autoría  : Fiorella Pérez — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, pegar este código y ejecutarlo (Ctrl+R) o
guardarlo como code.py en la tarjeta.
"""

import time

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import (
    ProvideServicesAdvertisement
)

from ideaboard import IdeaBoard
from ideasense import IdeaSense
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

# Nombre corto para evitar problemas de advertising
ble.name = "IdeaSense"

print("Nombre BLE:", ble.name)

uart = UARTService()

advertisement = ProvideServicesAdvertisement(uart)

# Comenzar publicidad UNA sola vez
ble.start_advertising(advertisement)

print("Esperando conexión BLE...")


# =====================================================
# VARIABLE GLOBAL
# =====================================================

mensaje = "Nada"


# =====================================================
# UTILIDADES
# =====================================================

def mostrar(patron):

    for r in range(5):
        for c in range(5):
            idea.matrix[c, r] = patron[r][c]


# =====================================================
# PATRONES
# =====================================================

FELIZ = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

TRISTE = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1]
]

NADA = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]


# =====================================================
# ESTADOS
# =====================================================

def estado_feliz():

    global mensaje

    mostrar(FELIZ)

    if mensaje == "Triste":
        return "TRISTE"

    if mensaje == "Nada":
        return "NADA"

    return "FELIZ"


def estado_triste():

    global mensaje

    mostrar(TRISTE)

    if mensaje == "Feliz":
        return "FELIZ"

    if mensaje == "Nada":
        return "NADA"

    return "TRISTE"


def estado_nada():

    global mensaje

    mostrar(NADA)

    if mensaje == "Feliz":
        return "FELIZ"

    if mensaje == "Triste":
        return "TRISTE"

    return "NADA"


# =====================================================
# MÁQUINA DE ESTADOS
# =====================================================

sm = StateMachine("NADA")

sm.add_state("FELIZ", estado_feliz)
sm.add_state("TRISTE", estado_triste)
sm.add_state("NADA", estado_nada)

mostrar(NADA)


# =====================================================
# CONTROL DE CONEXIÓN
# =====================================================

conectado = False


# =====================================================
# LOOP PRINCIPAL
# =====================================================

while True:

    # Volver a anunciarse por BLE después de una desconexión
    # (sin esto había que reiniciar la tarjeta para reconectar)
    if not ble.connected and not ble.advertising:
        ble.start_advertising(advertisement)

    # Detectar conexión
    if ble.connected and not conectado:

        conectado = True

        print("BLE conectado")

    # Detectar desconexión
    elif not ble.connected and conectado:

        conectado = False

        print("BLE desconectado")
        print("Esperando conexión BLE...")

    # Leer mensajes
    if ble.connected:

        if uart.in_waiting:

            texto = uart.readline()

            if texto:

                try:

                    mensaje = texto.decode("utf-8").strip()

                    print("Recibido:", mensaje)

                except Exception as e:

                    print("Error:", e)

    # Ejecutar máquina de estados
    sm.step()

    time.sleep(0.05)
