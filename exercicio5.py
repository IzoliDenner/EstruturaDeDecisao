'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota1 = input('Digite aqui sua primeira Nota:')
nota2 = input('Digite aqui sua segunda Nota: ')

nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1 + nota2) / 2
print(media)

if media >= 7:
    print(' voce foi APROVADO.')
if media < 7:
    print(' voce foi REPROVADO.')
if media == 10:
    print('Parabéns. voce foi APROVADO com Distinção')

'''n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))

media = (n1 + n2) / 2
print(media)


if media >= 7 and media < 10:
    print("Aprovado!")
if media < 7:
    print("Reprovado!")
if media == 10:
    print("Aprovado com distinção!")'''