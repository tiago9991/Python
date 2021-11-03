from random import randint
from time import sleep
print('Seu carro passou no radar 🚗...')
sleep(1)
print('O limite e de 80Km/h... vamos ver sua velocidade')
sleep(2)
velocidade = randint(10, 180)
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você estava a {velocidade}Km/h e foi multado, o valor da multa é {multa:.2f}')
else:
    print(f'Sua velocidade é {velocidade}, continue respeitando os limites')