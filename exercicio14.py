'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
  O algoritmo deve mostrar na tela as notas, a média,
  o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input('Digite sua primeira nota: \n'))
nota2 = float(input('Digite sua segunda  nota: \n'))

media = (nota1 + nota2) / 2
media - float(media)

if media >= 9 and media < 11:
    print('Média de aproveitamento: A = Aprovado')

elif media >= 7.5 and media < 9:
    print('Média de aproveitamento: B = Aprovado')

elif media >= 6.0 and media < 7.5:
    print('Média de aproveitamento: C = Aprovado')

elif media >= 4 and media < 6:
    print('Média de aproveitamento: D = Reprovado')

elif media <4:
    print('Média de aproveitamento: E = Reprovado')

