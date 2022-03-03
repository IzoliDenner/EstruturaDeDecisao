# 8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#   sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input('Digite o Preço do Contra Filé: R$'))
preco2 = float(input('Digite o Preço do Alcatra: R$'))
preco3 = float(input('Digite o Preço da Maminha: R$'))

mb = preco1

if preco2 < preco1 and preco2 < preco3:
    mb = preco2
if preco3 < preco1 and preco3 < preco2:
    mb = preco3

print(f'Compre o produto com o Valor: {mb}, ele é o mais barato')