from random import sample
print('Vamos sortear 2 pessoas para apresentar o trabalho')
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
ordem = sample(lista, k=2)
print('Os alunos escolhidos são')
print(ordem)