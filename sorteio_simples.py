from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo Aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
escolhido = (aluno1, aluno2, aluno3, aluno4)
print(f'O aluno escolhido foi {choice(escolhido)} ')