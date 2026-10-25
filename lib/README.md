# Librerías

Archivos que van en la carpeta `/lib` de la IdeaBoard.

| Archivo | Qué es | ¿Hay que copiarlo? |
| :--- | :--- | :--- |
| [`ideasense.py`](ideasense.py) | Librería de la IdeaSense Explorer (matriz, botones y sensores). Copia de referencia de la [versión oficial de CRCibernética](https://github.com/CRCibernetica/circuitpython-ideaboard/blob/master/lib/ideasense.py), licencia MIT. | No, la IdeaBoard ya la trae. Solo si se borró o se actualizó. |
| [`statemachine.py`](statemachine.py) | Máquina de estados mínima de Universidad CENFOTEC. | Sí, para los ejemplos de `Techable_Ideasense/` y `SumoIA/`. |

> La librería del perceptrón multicapa está en [`MultiLayerPerceptron/mlp.py`](../MultiLayerPerceptron/mlp.py).

## Cómo copiar una librería a la tarjeta

La IdeaBoard no aparece como unidad USB. Para pasar archivos:

- **IdeaCode** (<https://ideacode.crcibernetica.com/>): conectar, abrir el archivo y guardarlo en la tarjeta dentro de `/lib`, con el mismo nombre (en minúscula).
- **Thonny**: *Ver → Archivos*, seleccionar el archivo local y *Subir a /lib*.
- **Línea de comandos**: [`ibserial.py`](https://github.com/CRCibernetica/circuitpython-ideaboard/blob/master/tools/ibserial.py) de CRCibernética.

## Dependencias de `ideasense.py`

Todas vienen instaladas en la IdeaBoard. Si hubiera que reinstalarlas, están en [CRCibernetica/circuitpython-ideaboard/lib](https://github.com/CRCibernetica/circuitpython-ideaboard/tree/master/lib):

`adafruit_ht16k33/`, `adafruit_sht31d.mpy`, `adafruit_ltr329_ltr303.mpy`, `adafruit_lsm6ds/`, `adafruit_register/` (y `font5x5.py` para mostrar texto).

Los ejemplos con Bluetooth usan además `adafruit_ble/`.

---

## Referencia de `IdeaSense`

```python
from ideasense import IdeaSense
idea = IdeaSense()          # crear UNA sola vez
```

Si la tarjeta IdeaSense no está conectada, el constructor lanza `ValueError: No I2C device at address`.

### Matriz 5×5

| Código | Efecto |
| :--- | :--- |
| `idea.matrix[x, y] = 1` | Enciende un LED. `x` = columna 0–4 (izq. → der.), `y` = fila 0–4 (arriba → abajo). Fuera de rango lanza `ValueError`. |
| `idea.matrix.fill(0)` / `fill(1)` | Apaga / enciende toda la matriz. |
| `idea.matrix.brightness(0.5)` | Brillo de 0.0 a 1.0 (por defecto 0.3). **Es un método**: `brightness = 0.5` lo rompe. |
| `idea.matrix.show()` | Envía el dibujo a los LEDs. |

Los LEDs **no se pueden leer**: si el programa necesita saber qué está encendido, guarde su propia lista 5×5 y redibújela.

### Sensores

| Propiedad | Unidad | Notas |
| :--- | :--- | :--- |
| `idea.temp` | °C | Puede marcar 1–2 °C de más por el calor de la propia tarjeta. |
| `idea.humid` | % HR | |
| `idea.light` | cuentas | Luz visible + infrarroja. No son lux; elegir umbrales probando en el aula. |
| `idea.accel` | m/s² | Tupla `(ax, ay, az)`. Quieta y plana, un eje marca ≈ ±9.8. |
| `idea.gyro` | rad/s | Tupla `(gx, gy, gz)`. Quieta, todo ≈ 0. |

### Botones A, B, C (0, 1, 2)

```python
evento = idea.events.get()   # ButtonEvent o None
if evento and evento.pressed:
    print(evento.key_number) # 0 = A, 1 = B, 2 = C
```

| Propiedad | Devuelve |
| :--- | :--- |
| `idea.events.get()` | Siguiente evento de la cola (máx. 64), con `.key_number`, `.pressed` (True al presionar, False al soltar) y `.timestamp`. |
| `idea.pressed` | `[A, B, C]`: True solo en la vuelta del ciclo en que se presionó. |
| `idea.released` | `[A, B, C]`: True solo en la vuelta en que se soltó (≈ 0.15 s de retraso). |
| `idea.held` | `[A, B, C]`: True mientras se mantiene presionado. |

Consejos: leer cada propiedad **una vez por ciclo** y guardarla en una variable; usar `time.sleep()` de 0.05 s o menos para que los botones respondan.

---

## Referencia de `StateMachine`

```python
from statemachine import StateMachine

def esperando():
    if idea.pressed[0]:
        return "ACTIVO"
    return "ESPERANDO"

def activo():
    ib.pixel = (0, 255, 0)
    return "ACTIVO"

sm = StateMachine("ESPERANDO")
sm.add_state("ESPERANDO", esperando)
sm.add_state("ACTIVO", activo)

while True:
    sm.step()          # ejecuta el estado actual y pasa al que devuelve
    time.sleep(0.05)
```

Cada estado es una función sin argumentos que devuelve el nombre del próximo estado. Si el estado actual no tiene función registrada, `step()` no hace nada.
