#7 Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    maior = n3

print(f'O maior numero informado é o {maior}, e o menor numero informado é o {menor}')
