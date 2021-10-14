print('Programa de conversão de Real em Dólar')
real = float(input('Quanto dinheiro você tem: '))
dolar = float(input('Qual é a cotação do dólar no momento: '))
print('O valor de R${:.2f} convertido em dólar é US${:.2f}.'.format(real, real/dolar))