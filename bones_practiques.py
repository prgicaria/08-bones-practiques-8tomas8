#!/usr/bin/env python

'''Institut Icària. 1r de Batxillerat. Curs 2024-2025.
Entrar dos números i calcular el quocient de la divisió i el residu'''

__author__ = "Tomàs Ibáñez Pérez"
__email__ = "tibanez@instituticaia.cat"
__date__ = "2024/10/14"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
