from machine import Pin
import neopixel
import select
import sys

NUM_ROWS = 12
NUM_COLS = 10
DATA_PINS = [2, 4, 5, 12, 13, 14, 15, 17, 18, 19, 21, 22]
strips = [neopixel.NeoPixel(Pin(pin), NUM_COLS) for pin in DATA_PINS]

while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        data = sys.stdin.buffer.read(NUM_ROWS * NUM_COLS * 3)
        if len(data) == NUM_ROWS * NUM_COLS * 3:
            idx = 0
            for r in range(NUM_ROWS):
                for c in range(NUM_COLS):
                    r_val = data[idx]
                    g_val = data[idx+1]
                    b_val = data[idx+2]
                    strips[r][c] = (r_val, g_val, b_val)
                    idx += 3
                strips[r].write()
