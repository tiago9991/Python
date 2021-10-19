import math
# Primeira maneira

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5
print(f'A hipotenusa vai medir {hi:.2f}')


# Segunda maneira, com import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vau medir {hi:.2f}')