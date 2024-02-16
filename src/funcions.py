"""Módulo que contiene la función es_primo"""
import math


def es_primo(num):
    """
    Función para determinar si un número es primo:


    Entrada:
    - entero: número entero a determinar si es primo


    Salida:
    - True/False: e caso de ser primo o no

    """
    if num < 2:
        return False
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True
