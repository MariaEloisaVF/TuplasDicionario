'''
5 - Crie um dicionário para armazenar o nome do aluno (chave) e 4 notas (elementos) para 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média.
'''
alunos = {}

for _ in range(1,4):
	nome = input('Nome do aluno: ') 
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	nota3 = float(input('Nota 3: '))
	nota4 = float(input('Nota 4: '))
	notas = [nota1, nota2, nota3, nota4]
	media = (nota1 + nota2 + nota3 + nota4)/4
	alunos[nome]= notas, media
print(alunos)