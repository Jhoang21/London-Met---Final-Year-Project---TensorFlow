import os
import sys

from pathlib import Path

if not os.path.exists('CFolder'):
    os.makedirs('CFolder')

if not os.path.exists('RFolder'):
    os.makedirs('RFolder')

dir = os.path.dirname(__file__)
path = os.path.join(dir, 'CFolder')
path_ii = os.path.join(dir, 'RFolder')
files = os.listdir(path)

# --- File extension editor --
for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.txt'])))

# --- .txt to .bin to .txt converter --
def func_convert(filename):
    container = []
    with open(filename, 'rb') as file:
        while True:
            DL = file.read(1)
            if not DL:
                break
            container.append(int.from_bytes(DL, byteorder='big'))
        filename = str(ii) + ".txt"
        with open(os.path.join(path_ii, filename),'w') as file:
            for i in container:
                file.write(str(hex(container[i]))+ " ")
        print(str(ii) + ".txt has been created.")
        return container

# --- call to program --
ii = 0
try:
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'CFolder')
    path_ii = os.path.join(dir, 'RFolder')
    files = os.listdir(path)

    for index, file in enumerate(files):
        func_convert(os.path.join(path, file))
        os.remove(os.path.join(path, file))
        ii+=1

except FileNotFoundError:
    os.execl(sys.executable, sys.executable, *sys.argv)
