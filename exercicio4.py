# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('Aqui vamos verificar se a letra digitada é consoante ou vogal.')

texto = input('Digite a Letra desejada:')

if texto == 'a' or texto == 'e' or texto == 'i' or texto =='o' or texto == 'u':
    print(f'{texto}: é uma vogal')
else:
    print(f'{texto}: é uma consoante')