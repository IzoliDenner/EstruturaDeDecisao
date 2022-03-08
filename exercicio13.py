#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

dia = int(input('Por favor, digite um numero que corresponde o dia da semana:\n'))

if dia == 1:
    print('Hoje é Domingo, aproveite seu dia.')

elif dia == 2:
    print('Hoje é Segunda, inicio de semana fique calmo...')

elif dia == 3:
    print('Hoje é Terça, depois da segunda, continue calmo...')

elif dia == 4:
    print('Hoje é Quarta, mais próximo da sexta...')

elif dia == 5:
    print('Hoje é Quinta, quase la...')

elif dia == 6:
    print('Hoje é Sexta, Chegouuuuu, aproveite...')

elif dia == 7:
    print('Hoje é Sabado, Iniciou-se o Fds...')

else:
    print('Este é um valor invalido por favor, digite um valor de 1 a 7.')