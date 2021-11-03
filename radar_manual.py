from time import sleep
velocidade = float(input('Qual é a velocidade atual do carro? '))
print('PROCESSANDO')
sleep(2)
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \U0001f926\u200D\u2642')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
else:
    print('Você está no limite permitido \U0001f44d')
    print('Tenha um bom dia! Dirija com segurança')