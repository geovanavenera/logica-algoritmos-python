print ('Bem-vinda Geovana Soares')

valoresToras = {
    'PIN':150.40,
    'PER':160.20,
    'MOG':190.90,
    'IPE':210.10,
    'IMB':220.70 }

#escolha do tipo de madeira
def escolha_tipo():

    while True:

        print('(PIN) Tora de Pinho')
        print('(PER) Tora de Peroba')
        print('(MOG) Tora de  Mogno')
        print('(IPE) Tora de Ipê')
        print('(IMB) Tora de Imbuia')

        tipo = input('Entre com o tipo de Madeira desejado').strip().upper()

        if tipo in valoresToras:
            return valoresToras[tipo]
        else:
            print ('Escolha invalida, digite o modelo novamente')

#Quantidade de toras
def qnt_toras():

    while True:
        try:
            qnt = int(input('Entre com a quantidade de toras (m³)'))
            if qnt > 2000:
                print('Não aceitamos pedidos com essa quantidade')
                continue

            if qnt <= 99:
                desconto = 0
            elif qnt <= 499:
                desconto= 4/100
            elif qnt <= 999:
                desconto= 9/100
            else:
                desconto= 16/100

            return qnt, desconto

        except ValueError:
            print('Valor invalido, digite novamente')

#Escolha do transporte
def transporte():

    while True:

        print ('(1) Transporte Rodoviario  - R$ 1000,00')
        print ('(2) Transporte Ferroviario - R$ 2000,00')
        print ('(3) Transporte Hidroviario - R$ 2500,00')

        transporte = input('Escolha o tipo de transporte').strip().lower()
        if transporte == '1':
            return 1000
        elif transporte == '2':
            return 2000
        elif transporte == '3':
            return 2500
        else:
            print('Opção invalida, digite  transporte novamente')

#variaveis para calculo final

precoMadeira = escolha_tipo()
qnt, desconto = qnt_toras()
valorTransporte = transporte()

#calculo do valor total
total = ((precoMadeira * qnt )* (1 - desconto)) + valorTransporte
print (f'Total: R$ {total:.2f}')
