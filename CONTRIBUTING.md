# Cómo contribuir

¡Gracias por sumar ejemplos! Para que el repositorio siga ordenado:

## 1. Dónde va cada cosa

| Tipo de aporte | Carpeta |
| :--- | :--- |
| Programa corto que usa la IdeaSense | `ejemplos/<tema>/` (crear un tema nuevo con el siguiente número si ninguno encaja) |
| Librería reutilizable que va en `/lib` de la tarjeta | `lib/` |
| Modelo exportado desde IdeaAI | `IdeaAI_Ejemplos/` |
| Proyecto con Teachable Machine o Bluetooth | `Techable_Ideasense/` |
| Página web o herramienta del portal | `docs/` (y agregarla a la lista `herramientas` en `docs/index.html`) |

No dejar archivos `.py` sueltos en la raíz del repositorio.

## 2. Nombres de archivo

- En minúscula, con guiones bajos y sin tildes ni espacios: `medidor_luz.py`, no `Medidor de Luz.py`.
- Los módulos que se importan deben llamarse exactamente como en el `import` (por ejemplo `statemachine.py` para `from statemachine import StateMachine`).

## 3. Encabezado obligatorio

Todo programa empieza con:

```python
"""
Nombre del ejemplo
==================

Qué hace el programa, en dos o tres líneas.

Hardware : IdeaBoard + IdeaSense Explorer (+ lo que se conecte)
Controles: cómo se usa (botones, gestos, pines)
Usa      : partes de la API que se practican (idea.accel, ib.pixel, ...)
Autoría  : Nombre Apellido — Universidad CENFOTEC
Repositorio: https://github.com/Universidad-Cenfotec/IdeaSense
"""
```

## 4. Buenas prácticas para CircuitPython en la IdeaBoard

- Crear `idea = IdeaSense()` e `ib = IdeaBoard()` una sola vez.
- Todo `while True:` lleva un `time.sleep()` (0.01 – 0.1 s).
- `idea.matrix.brightness(0.3)` es un método; no asignarle un valor.
- Leer `idea.pressed` / `idea.held` una vez por ciclo y guardarlo en una variable.
- Comentarios en español, pensados para estudiantes.
- Probar el código en una tarjeta real con [IdeaCode](https://ideacode.crcibernetica.com/) antes de subirlo.

## 5. Documentar

- Agregar el ejemplo a la tabla del `README.md` de su carpeta y a la del `README.md` principal.
- Si necesita hardware adicional, indicar las conexiones (pin, voltaje, GND).
