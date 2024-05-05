#!/usr/bin/env python3
import os

# Obtener la ruta absoluta del archivo actual (__file__)
ruta_absoluta = os.path.abspath(__file__)
print("Ruta absoluta del archivo actual:", ruta_absoluta)

# Obtener el directorio del archivo actual (__file__)
directorio_actual = os.path.dirname(__file__)
print("Directorio del archivo actual:", directorio_actual)