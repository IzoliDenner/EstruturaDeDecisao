# Faça um Programa que peça um número correspondente a um determinado ano e em
# seguida informe se este ano é ou não bissexto.
import math

ano = int(input('Digite um ano:\n'))

if ano % 4 == 0:
    print(f'Este é um ano Bisexto !!!. ')
else:
    print("Este não é um ano Bisexto!!!")