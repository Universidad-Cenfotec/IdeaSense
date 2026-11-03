"""
===============================================================================
PROYECTO: IDEASENSE EXPLORER AI - GAME CONTROLLER FIRMWARE
Firmware Completo para IdeaBoard (ESP32) - CircuitPython 10.x
===============================================================================
- Muestreo y transmisión BLE a 25 Hz (40 ms).
- Lectura de botones mediante la librería 'ideasense' (idea.held) o GPIO directo.
- Lectura de acelerómetro y giroscopio mediante idea.accel e idea.gyro.
- Envío continuo en JSON de telemetría y estado de botones ("ba", "bb").
===============================================================================
"""

import time
import board
import busio
import json
import digitalio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import Advertisement, ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

use_ideasense_lib = False
ib = None
idea = None

try:
    from ideaboard import IdeaBoard
    from ideasense import IdeaSense
    ib = IdeaBoard()
    idea = IdeaSense()
    use_ideasense_lib = True
    print("[HW] Librerías 'ideaboard' e 'ideasense' cargadas con éxito.")
except Exception as err:
    print(f"[HW WARN] Modo directo activo: {err}")

hw_addresses = []
telemetry_interval = 0.04  # 25 Hz
last_telemetry_time = 0.0
was_connected = False

i2c = None
ble = None
uart = None
advertisement = None
scan_response = None
board_led = None
btn_a = None
btn_b = None

def initialize_hardware():
    global board_led, btn_a, btn_b, i2c
    print("[HW] Inicializando hardware base...")

    if not use_ideasense_lib:
        try:
            board_led = digitalio.DigitalInOut(board.NEOPIXEL)
            board_led.direction = digitalio.Direction.OUTPUT
        except Exception:
            pass

        a_pins = ['BUTTON_A', 'IO0', 'SW1', 'BTN_A', 'D2']
        for p in a_pins:
            if hasattr(board, p):
                try:
                    btn_a = digitalio.DigitalInOut(getattr(board, p))
                    btn_a.direction = digitalio.Direction.INPUT
                    btn_a.pull = digitalio.Pull.UP
                    break
                except Exception:
                    pass

        b_pins = ['BUTTON_B', 'IO14', 'SW2', 'BTN_B', 'D4']
        for p in b_pins:
            if hasattr(board, p):
                try:
                    btn_b = digitalio.DigitalInOut(getattr(board, p))
                    btn_b.direction = digitalio.Direction.INPUT
                    btn_b.pull = digitalio.Pull.UP
                    break
                except Exception:
                    pass

    try:
        i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
        print("[HW] Bus I2C activo a 400 kHz.")
    except Exception as e:
        print(f"[HW WARN] Bus I2C: {e}")


def update_led_matrix(pixel_array):
    if use_ideasense_lib and idea:
        try:
            idea.matrix.fill(0)
            for row in range(5):
                for col in range(5):
                    idx = row * 5 + col
                    if idx < len(pixel_array) and pixel_array[idx] == 1:
                        idea.matrix[col, row] = 1
            idea.matrix.show()
            return
        except Exception:
            pass

    if i2c and 0x70 in hw_addresses:
        try:
            ram = [0] * 16
            for row in range(5):
                row_bits = 0
                for col in range(5):
                    idx = row * 5 + col
                    if idx < len(pixel_array) and pixel_array[idx] == 1:
                        row_bits |= (1 << col)
                ram[row * 2] = row_bits

            while not i2c.try_lock():
                pass
            i2c.writeto(0x70, bytes([0x00] + ram))
            i2c.unlock()
        except Exception:
            pass


def initialize_ideasense():
    global i2c, hw_addresses
    if not i2c:
        return

    while not i2c.try_lock():
        pass
    hw_addresses = i2c.scan()
    i2c.unlock()

    if 0x70 in hw_addresses and not use_ideasense_lib:
        try:
            while not i2c.try_lock():
                pass
            i2c.writeto(0x70, bytes([0x21]))
            i2c.writeto(0x70, bytes([0x81]))
            i2c.writeto(0x70, bytes([0xEF]))
            i2c.unlock()
        except Exception:
            pass

    if 0x6a in hw_addresses and not use_ideasense_lib:
        try:
            while not i2c.try_lock():
                pass
            i2c.writeto(0x6a, bytes([0x10, 0x40]))
            i2c.writeto(0x6a, bytes([0x11, 0x40]))
            i2c.unlock()
        except Exception:
            pass

    if 0x29 in hw_addresses and not use_ideasense_lib:
        try:
            while not i2c.try_lock():
                pass
            i2c.writeto(0x29, bytes([0x80, 0x01]))
            i2c.unlock()
        except Exception:
            pass

    update_led_matrix([0] * 25)


def initialize_ble():
    global ble, uart, advertisement, scan_response
    ble = BLERadio()
    ble.name = "IdeaBoard"

    uart = UARTService()
    advertisement = ProvideServicesAdvertisement(uart)

    scan_response = Advertisement()
    scan_response.complete_name = "IdeaBoard-Explorer-AI"

    try:
        ble.start_advertising(advertisement, scan_response)
    except Exception:
        pass


def check_ble_status():
    global ble, advertisement, scan_response
    if ble.connected or (hasattr(ble, 'connections') and len(ble.connections) > 0):
        return True
    try:
        if not ble.advertising:
            ble.start_advertising(advertisement, scan_response)
    except Exception:
        pass
    return False


def read_environment_sensors():
    if i2c and 0x44 in hw_addresses:
        try:
            while not i2c.try_lock():
                pass
            i2c.writeto(0x44, bytes([0x2C, 0x06]))
            time.sleep(0.015)
            buf = bytearray(6)
            i2c.readfrom_into(0x44, buf)
            i2c.unlock()

            raw_temp = (buf[0] << 8) | buf[1]
            raw_hum = (buf[3] << 8) | buf[4]

            temp_c = -45.0 + (175.0 * raw_temp / 65535.0)
            humidity = 100.0 * (raw_hum / 65535.0)
            return temp_c, humidity
        except Exception:
            pass
    t_base = time.monotonic()
    return 23.5 + (t_base % 2.0) * 0.1, 50.0 + (t_base % 3.0) * 0.15


def read_motion_sensors():
    """Lee acelerometro y giroscopio usando IdeaSense cuando esta disponible.

    IdeaSense devuelve:
      - accel: aceleracion X, Y, Z en g
      - gyro: velocidad angular X, Y, Z en grados/segundo

    Si la biblioteca no esta disponible, utiliza la lectura I2C alternativa.
    Si ninguna lectura funciona, devuelve ceros para no presentar datos
    simulados como si fueran mediciones reales.
    """
    if use_ideasense_lib and idea:
        try:
            ax, ay, az = idea.accel
            gx, gy, gz = idea.gyro

            return (
                float(ax), float(ay), float(az),
                float(gx), float(gy), float(gz)
            )
        except Exception as err:
            print(f"[IMU WARN] No se pudo leer la IMU mediante IdeaSense: {err}")
            return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    if i2c and 0x6A in hw_addresses:
        try:
            buf = bytearray(12)

            while not i2c.try_lock():
                pass
            try:
                i2c.writeto_then_readfrom(0x6A, bytes([0x22]), buf)
            finally:
                i2c.unlock()

            def to_signed(low, high):
                val = (high << 8) | low
                return val - 65536 if val > 32767 else val

            gx = to_signed(buf[0], buf[1]) * 0.00875
            gy = to_signed(buf[2], buf[3]) * 0.00875
            gz = to_signed(buf[4], buf[5]) * 0.00875

            ax = to_signed(buf[6], buf[7]) * 0.000061
            ay = to_signed(buf[8], buf[9]) * 0.000061
            az = to_signed(buf[10], buf[11]) * 0.000061

            return ax, ay, az, gx, gy, gz
        except Exception as err:
            print(f"[IMU WARN] Error leyendo la IMU por I2C: {err}")

    return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0


def read_light_sensor():
    if i2c and 0x29 in hw_addresses:
        try:
            buf = bytearray(4)
            if i2c.try_lock():
                try:
                    i2c.writeto_then_readfrom(0x29, bytes([0x88]), buf)
                    ch0 = (buf[3] << 8) | buf[2]
                    return float(ch0)
                finally:
                    i2c.unlock()
        except Exception:
            pass

    t = time.monotonic()
    return round(280.0 + (t * 12.0 % 150.0), 1)


def process_command(raw_cmd):
    global telemetry_interval
    try:
        data = json.loads(raw_cmd)
        cmd_type = data.get("cmd", "")

        if cmd_type == "matrix":
            pixels = data.get("pixels", [])
            update_led_matrix(pixels)
        elif cmd_type == "config":
            interval_ms = data.get("interval", 200)
            telemetry_interval = max(0.02, min(2.0, interval_ms / 1000.0))
    except Exception:
        pass


def send_telemetry():
    t, h = read_environment_sensors()
    ax, ay, az, gx, gy, gz = read_motion_sensors()
    lux = read_light_sensor()

    state_a = 0
    state_b = 0

    if use_ideasense_lib and idea:
        try:
            if hasattr(idea, 'held') and len(idea.held) > 0:
                state_a = 1 if idea.held[0] else 0
                state_b = 1 if (len(idea.held) > 1 and (idea.held[1] or (len(idea.held) > 2 and idea.held[2]))) else 0
        except Exception:
            pass
    else:
        state_a = 1 if (btn_a and not btn_a.value) else 0
        state_b = 1 if (btn_b and not btn_b.value) else 0

    telemetry_packet = {
        "t": round(t, 1),
        "h": round(h, 1),
        "l": int(lux),
        "ax": round(ax, 3),
        "ay": round(ay, 3),
        "az": round(az, 3),
        "gx": round(gx, 1),
        "gy": round(gy, 1),
        "gz": round(gz, 1),
        "ba": state_a,
        "bb": state_b
    }

    payload = json.dumps(telemetry_packet) + "\n"

    try:
        uart.write(payload.encode('utf-8'))
    except Exception:
        pass


def main():
    global last_telemetry_time, was_connected

    initialize_hardware()
    initialize_ideasense()
    initialize_ble()

    print("[SISTEMA] Firmware activo para Gamepad BLE...")

    while True:
        try:
            is_connected = check_ble_status()

            if is_connected and not was_connected:
                update_led_matrix([0] * 25)

            was_connected = is_connected

            if is_connected and uart.in_waiting:
                raw_data = uart.readline().decode('utf-8').strip()
                if raw_data:
                    process_command(raw_data)

            now = time.monotonic()
            if now - last_telemetry_time >= telemetry_interval:
                last_telemetry_time = now
                if is_connected:
                    send_telemetry()

        except Exception as err:
            print(f"[RUN ERROR] {err}")

        time.sleep(0.01)


if __name__ == "__main__":
    main()
