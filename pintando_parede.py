largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area =  largura * altura
tinta = largura * (altura / 2)
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))