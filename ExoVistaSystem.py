import sys
from os import path

import numpy as np
import pandas as pd

from src import Settings, generate_scene, read_solarsystem

# ExoVista v2.4

# Generates a single, user-defined planetary system.

filename = "tau_ceti.dat"
filein = ""
ndisk = 2

if len(sys.argv) > 1:
    filein = sys.argv[1]
    if not path.exists(filein):
        print("Error: input file not found.")
        filein = ""

while not path.exists(filename):
    if filein != "":
        filename = filein
    else:
        print("Enter input file name.")
        filename = input()

    if not path.exists(filename):
        print("Error: file not found.")
        filename = ""
        filein = ""
        continue

    line = ""

    fin = open(filename, "r")
    line = fin.readline()

    if line != "Star\n":
        print("Error: wrong file format.")
        filename = ""
        filein = ""
        continue
    while line != "Planets\n":
        try:
            line = fin.readline()
        except:
            print("Error: file contains no planets.")
            filename = ""
            filein = ""
            break
    while line != "Disks\n":
        try:
            line = fin.readline()
        except:
            print("Error: file contains no disk components.")
            filename = ""
            filein = ""
            break
    ndisk = -1
    while line != "Settings\n":
        try:
            line = fin.readline()
            if line != "Settings\n":
                ndisk += 1
        except:
            break
        if len(line.split()) == 0:
            ndisk -= 1
            break

settings = Settings.Settings(
    output_dir="./output", ncomponents=ndisk, timemax=10.0
)  # "standard" configuration
s, p, a, d, c, new_settings = read_solarsystem.read_solarsystem(
    settings, system_file=filename
)
print("Generating scene...")
generate_scene.generate_scene(s, p, d, a, c, new_settings)
