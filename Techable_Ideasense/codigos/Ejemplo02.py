"""
Teachable IdeaSense — Ejemplo 02: números
=========================================

Recibe por BLE la clase Uno, Dos, Tres o Nulo y muestra el número en la
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
ble.name = "IdeaSense"

print("Nombre BLE:", ble.name)

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)

print("Esperando conexión BLE...")

# =====================================================
# VARIABLE GLOBAL
# =====================================================

mensaje = "Nulo"

# =====================================================
# UTILIDAD
# =====================================================

def mostrar(patron):
    for r in range(5):
        for c in range(5):
            idea.matrix[c, r] = patron[r][c]

# =====================================================
# PATRONES
# =====================================================

UNO = [
    [0,0,1,0,0],
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,1,1,1,0]
]

DOS = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0]
]

TRES = [
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0]
]

NULO = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

# =====================================================
# ESTADOS
# =====================================================

def estado_uno():
    global mensaje

    mostrar(UNO)

    if mensaje == "Dos":
        return "DOS"

    if mensaje == "Tres":
        return "TRES"

    if mensaje == "Nulo":
        return "NULO"

    return "UNO"


def estado_dos():
    global mensaje

    mostrar(DOS)

    if mensaje == "Uno":
        return "UNO"

    if mensaje == "Tres":
        return "TRES"

    if mensaje == "Nulo":
        return "NULO"

    return "DOS"


def estado_tres():
    global mensaje

    mostrar(TRES)

    if mensaje == "Uno":
        return "UNO"

    if mensaje == "Dos":
        return "DOS"

    if mensaje == "Nulo":
        return "NULO"

    return "TRES"


def estado_nulo():
    global mensaje

    mostrar(NULO)

    if mensaje == "Uno":
        return "UNO"

    if mensaje == "Dos":
        return "DOS"

    if mensaje == "Tres":
        return "TRES"

    return "NULO"

# =====================================================
# MÁQUINA DE ESTADOS
# =====================================================

sm = StateMachine("NULO")

sm.add_state("UNO", estado_uno)
sm.add_state("DOS", estado_dos)
sm.add_state("TRES", estado_tres)
sm.add_state("NULO", estado_nulo)

mostrar(NULO)

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

    # Leer mensajes BLE
    if ble.connected:

        if uart.in_waiting:

            texto = uart.readline()

            if texto:

                try:

                    mensaje = texto.decode("utf-8").strip()

                    print("Recibido:", mensaje)

                except Exception as e:

                    print("Error:", e)

    # Ejecutar la máquina de estados
    sm.step()

    time.sleep(0.05)
