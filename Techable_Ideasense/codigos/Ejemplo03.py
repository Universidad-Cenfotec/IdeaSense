"""
Teachable IdeaSense — Ejemplo 03: detector de objeto
====================================================

Recibe por BLE (UART Nordic) la clase detectada por un modelo de Teachable
Machine en el navegador y confirma visualmente si el objeto entrenado está
frente a la cámara:

    Clase del modelo  ->  Estado   ->  Matriz          LED RGB
    "Carrito"         ->  CHECK    ->  ✔ (visto bueno)  verde
    "Nulo"            ->  NULO     ->  ✖ (equis)        rojo

Modelo de ejemplo: https://teachablemachine.withgoogle.com/models/iIaAJedxa/
(ver Techable_Ideasense/modelos/modelos.md). Los nombres de las clases del
modelo deben coincidir exactamente (mayúsculas incluidas) con los de este
código.

Hardware : IdeaBoard + IdeaSense Explorer
Controles: Conectarse desde la plataforma Teachable IdeaSense (dispositivo "IdeaSense").
Usa      : adafruit_ble, statemachine, idea.matrix, ib.pixel
Autoría  : Universidad CENFOTEC (sigue la estructura de Ejemplo01 y Ejemplo02)
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense

Cómo ejecutarlo: abrir https://ideacode.crcibernetica.com en Chrome o Edge,
conectar la IdeaBoard por USB, copiar lib/statemachine.py a /lib en la tarjeta,
pegar este código y guardarlo como code.py.
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

# Última clase recibida desde el navegador
mensaje = "Nulo"

# =====================================================
# UTILIDAD
# =====================================================

def mostrar(patron):
    """Dibuja un patrón 5x5 (lista de filas) en la matriz."""
    for r in range(5):
        for c in range(5):
            idea.matrix[c, r] = patron[r][c]

# =====================================================
# PATRONES
# =====================================================

CHECK = [
    [0,0,0,0,1],
    [0,0,0,1,0],
    [1,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]

X = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
]

# =====================================================
# ESTADOS
# Cada estado dibuja su patrón y devuelve el próximo estado.
# =====================================================

def estado_check():
    mostrar(CHECK)
    ib.pixel = (0, 80, 0)      # verde

    if mensaje == "Nulo":
        return "NULO"

    return "CHECK"


def estado_nulo():
    mostrar(X)
    ib.pixel = (80, 0, 0)      # rojo

    if mensaje == "Carrito":
        return "CHECK"

    return "NULO"

# =====================================================
# MÁQUINA DE ESTADOS
# =====================================================

sm = StateMachine("NULO")

sm.add_state("CHECK", estado_check)
sm.add_state("NULO", estado_nulo)

mostrar(X)

# =====================================================
# CONTROL DE CONEXIÓN
# =====================================================

conectado = False

# =====================================================
# LOOP PRINCIPAL
# =====================================================

while True:

    # Volver a anunciarse por BLE después de una desconexión
    if not ble.connected and not ble.advertising:
        ble.start_advertising(advertisement)

    # Detectar conexión
    if ble.connected and not conectado:
        conectado = True
        print("BLE conectado")

    # Detectar desconexión
    elif not ble.connected and conectado:
        conectado = False
        mensaje = "Nulo"
        print("BLE desconectado")
        print("Esperando conexión BLE...")

    # Leer mensajes BLE (una línea por clase detectada)
    if ble.connected and uart.in_waiting:
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
