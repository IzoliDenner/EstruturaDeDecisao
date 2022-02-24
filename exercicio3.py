# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print('Nesta etapa digite o seu Genero: ')

genero = input('Digite F para Feminino e M para Masculino.\n')

if genero == 'F':
    print('Genero Feminino.')

elif genero == 'M':
    print('Genero Masculino. ')

else:
    print ('Genero Indefinido')