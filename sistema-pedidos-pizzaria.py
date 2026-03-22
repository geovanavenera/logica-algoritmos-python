print('  Bem-vinda a Pizzaria da  Geovana Soares     ')
print('----------------------------------------------')
print('Tamanho | Pizza Salgada (PS) | Pizza Doce (PD)')
print('----------------------------------------------')
print('   P    |        R$30        |      R$34      ')
print('   M    |        R$45        |      R$48      ')
print('   G    |        R$60        |      R$66      ')

nomes = {
    'PS': 'pizza salgada',
    'PD': 'pizza doce'
}
precos= {
    'PS': {'P':30, 'M':45, 'G':60},
    'PD': {'P':34, 'M':48, 'G':66}
}

valorTotal = 0

while True:
#escolha do sabor
    sabor =(input('Escolha o sabor desejado (PS/PD): ').upper())
    if sabor not in ('PS', 'PD'):
        print('Sabor inválido. Tente novamente.')
        continue

#escolha do tamanho
    tamanho = (input('Escolha o tamanho da sua pizza (P/M/G): ').strip().upper())
    if tamanho not in ('P', 'M', 'G'):
        print('Tamanho inválido. Tente novamente.')
        continue

#calculo acumulador
    valor = precos[sabor][tamanho]
    valorTotal += valor

    print (f'Voce pediu {nomes[sabor]} no tamanho {tamanho} no valor R$: {valor}')

#pergunta se quer mais alguma coisa
    pedidoNovo= (input ('Gostaria de mais alguma coisa? (S/N)').strip().upper())
    if pedidoNovo == 'S':
        continue
    elif pedidoNovo =='N':
       print (f'Valor total a ser pago: R$ {valorTotal:.2f}, Obrigada e volte sempre')
       break
    else:
       print ('Opçao Invalida')
       break