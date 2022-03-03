# 6 Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite o primeiro numero: \n'))
n2 = int(input('Digite o segundo numero: \n'))
n3 = int(input('Digite o terceiro numero: \n'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior numero')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior numero')
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior numero')