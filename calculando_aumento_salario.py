salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float(input('Qual é a porcentagem de aumento do salário? '))
ajuste = salario + (salario * aumento / 100)
print('Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}'.format(salario, aumento, ajuste))