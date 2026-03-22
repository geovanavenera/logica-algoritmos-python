print ('Bem-vinda Geovana Soares')

valorBase = float(input('Informe o valor base do plano de saude: '))
idade = int(input('Informe a idade do cliente: '))

#a porcentagem é com base na listagem
if idade <= 18:
     porcentagem = 1
elif idade <= 28:
     porcentagem = 1.5
elif idade <= 38:
     porcentagem = 2.25
elif idade <= 48:
     porcentagem = 2.40
elif idade <= 58:
     porcentagem = 3.50
else:
     porcentagem = 6.00

#calculo do valor da mensalidade do cliente
valorMensal= valorBase * porcentagem
print (f'O valor mensal do plano é de R$ {valorMensal}')
