#!/usr/bin/env python3
import sys, time, math

gradient = '-g' in sys.argv or '--gradient' in sys.argv

text = sys.stdin.read().rstrip('\n')
lines = text.split('\n')
n = len(lines)

freq = 0.05 if gradient else 0.3

def rainbow_line(line, offset, row):
    out = []
    for i, ch in enumerate(line):
        hue = (i * freq + row * freq * 2 + offset) % 1.0
        r = int((math.sin(hue * 2 * math.pi) * 0.5 + 0.5) * 255)
        g = int((math.sin((hue + 1/3) * 2 * math.pi) * 0.5 + 0.5) * 255)
        b = int((math.sin((hue + 2/3) * 2 * math.pi) * 0.5 + 0.5) * 255)
        out.append(f'\x1b[38;2;{r};{g};{b}m{ch}')
    return ''.join(out) + '\x1b[0m'

offset = 0
while True:
    frame = '\x1b[2J\x1b[H'
    for row, line in enumerate(lines):
        frame += rainbow_line(line, offset, row) + '\n'
    sys.stdout.write(frame)
    sys.stdout.flush()
    offset = (offset + 0.02) % 1.0
    time.sleep(0.033)
