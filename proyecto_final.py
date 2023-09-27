# -*- coding: utf-8 -*-
"""Proyecto final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ms3AZp-NJSwRNVPfdKY8MWDEmmZU6kK5
"""

#Vamos a hacer una calculadora para medir la masa molar de ciertos compuestos reconocidos

# Masas atómicas de los elementos químicos más usados
masas_atomicas = {
    "Al":27.00,
    "Sb":121.76,
    "P":30.98,
    "Cr":52.01,
    "Cu":63.54,
    "Cl":35.46,
    "S":32.06,
    "Mg":24.30,
    "Mn":54.93,
    "Na":23.00,
    "I":126.92,
    "Zn":85.38,
    "Ti":47.90,
    "Au":197.20,
    "Ag":107.88,
    "H2":2.016,
    "O2":32.00,
    "O3":42.00,
    "Cr2":104.02,
    "Cl2":70.92,
    "N2":28.02,
    "F2":38.00,
    "C6":72.06,
    "H12":12.12,
    "O6":96.00,
    "H": 1.01,
    "He":4.00,
    "Fe":55.85,
    "Li": 6.94,
    "Be": 9.01,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
}

# Pedir al usuario el compuesto químico
compuesto_químico = input("Ingresa un elemento o compuesto químico:  ")

# Inicializar la masa molar en 0, con el fin de que se empiece a contar desde este número
masa_molar = 0.0

# Calcular la masa molar
for elemento in compuesto_químico.split():
    if elemento in masas_atomicas:
        masa_molar += masas_atomicas[elemento]
    else:
        print(f"Elemento desconocido: {elemento}")
        break
else:
    print(f"La masa molar de {compuesto_químico} es {masa_molar} g/mol")