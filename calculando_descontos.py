preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Qual e a porcentagem do desconto: '))
novo = preco - (preco * desconto / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar {:.2f}'.format(preco, desconto, novo))