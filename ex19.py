#sorteando alunos
import random
alunos = []

aluno1 = str(input('Qual o nome do primeiro aluno? '))
alunos.append(aluno1)
aluno2 = str(input('Qual o nome do segundo aluno? '))
alunos.append(aluno2)
aluno3 = str(input('Qual o nome do terceiro aluno? '))
alunos.append(aluno3)
aluno4 = str(input('Qual o nome do quarto aluno? '))
alunos.append(aluno4)

alunoSorteado = random.choice(alunos)

print(f'O alunos escolhido foi {alunoSorteado}')