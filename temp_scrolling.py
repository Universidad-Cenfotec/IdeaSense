from ideasense import IdeaSense
import time

idea = IdeaSense()

# --- Fuente simple 5x5 (columnas) ---
FONT = {
    "0": [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ],
    "1": [
        [0,0,1,0,0],
        [0,1,1,0,0],
        [1,0,1,0,0],
        [0,0,1,0,0],
        [1,1,1,1,1],
    ],
    "2": [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    "3": [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
    ],
    "4": [
        [1,0,0,1,0],
        [1,0,0,1,0],
        [1,1,1,1,1],
        [0,0,0,1,0],
        [0,0,0,1,0],
    ],
    "5": [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
    ],
    "6": [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ],
    "7": [
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,1,0,0,0],
    ],
    "8": [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ],
    "9": [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
    ],
    ".": [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,1,0,0],
    ],
    "C": [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1],
    ],
    " ": [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
}

# --- convierte texto a columnas ---
def text_to_columns(text):
    cols = []
    for ch in text:
        pattern = FONT.get(ch, FONT[" "])
        for x in range(5):
            col = [pattern[y][x] for y in range(5)]
            cols.append(col)
        cols.append([0]*5)  # espacio entre letras
    return cols

def draw_window(cols, offset):
    for x in range(5):
        if offset + x < len(cols):
            col = cols[offset + x]
        else:
            col = [0]*5
        for y in range(5):
            idea.matrix[x, y] = col[y]
    idea.matrix.show()

# --- loop principal ---
while True:
    temp = idea.temp
    text = "{:.1f}C".format(temp)

    print("Temp:", text)

    cols = text_to_columns(text)

    for offset in range(len(cols)):
        draw_window(cols, offset)
        time.sleep(0.1)