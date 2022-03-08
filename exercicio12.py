'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

salarioh = float(input('Digite o seu o quanto ganha por hora: '))
horast = float(input('Digite as horas trabalhadas no mes: '))

salario = salarioh * horast

if salario <= 900:
    ir = 0
    inss = salario * 0.10
    fgts = salario * 0.11

    descontos = ir + inss + fgts
    salarioliquido = salario - descontos

    print(f'Salario Bruto:         R$ {salario:.2f}')
    print(f'Imposto de renda (5%): R$ {ir:.2f} - não aplicado para este salario.')
    print(f'INSS (10%):            R$ {inss:.2f}')
    print(f'FGTS (11%):            R$ {fgts:.2f}')
    print(f'Total de descontos:    R$ {descontos:.2f}')
    print(f'Salario Liquido:       R$ {salarioliquido:.2f}')

if salario > 900 and salario <= 1500:
    ir = 0.05
    inss = salario * 0.10
    fgts = salario * 0.11

    descontos = ir + inss + fgts
    salarioliquido = salario - descontos

    print(f'Salario Bruto:         R$ {salario:.2f}')
    print(f'Imposto de renda (5%): R$ {ir:.2f} ')
    print(f'INSS (10%):            R$ {inss:.2f}')
    print(f'FGTS (11%):            R$ {fgts:.2f}')
    print(f'Total de descontos:    R$ {descontos:.2f}')
    print(f'Salario Liquido:       R$ {salarioliquido:.2f}')

if salario > 1500 and salario <= 2500:
    ir = 0.10
    inss = salario * 0.10
    fgts = salario * 0.11

    descontos = ir + inss + fgts
    salarioliquido = salario - descontos

    print(f'Salario Bruto:         R$ {salario:.2f}')
    print(f'Imposto de renda (10%): R$ {ir:.2f} ')
    print(f'INSS (10%):            R$ {inss:.2f}')
    print(f'FGTS (11%):            R$ {fgts:.2f}')
    print(f'Total de descontos:    R$ {descontos:.2f}')
    print(f'Salario Liquido:       R$ {salarioliquido:.2f}')

if salario > 2500:
    ir = 0.20
    inss = salario * 0.10
    fgts = salario * 0.11

    descontos = ir + inss + fgts
    salarioliquido = salario - descontos

    print(f'Salario Bruto:         R$ {salario:.2f}')
    print(f'Imposto de renda (20%): R$ {ir:.2f} ')
    print(f'INSS (10%):            R$ {inss:.2f}')
    print(f'FGTS (11%):            R$ {fgts:.2f}')
    print(f'Total de descontos:    R$ {descontos:.2f}')
    print(f'Salario Liquido:       R$ {salarioliquido:.2f}')