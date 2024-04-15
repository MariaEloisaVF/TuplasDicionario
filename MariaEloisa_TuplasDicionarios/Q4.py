'''
4 - Crie uma estrutura de repetição para fazer a leitura de vários números inteiros e ímpares e os armazene dentro de uma lista, quando essa lista chegar a 5 elementos pare com a leitura. Em seguida, converta essa lista em uma tupla e crie outra estrutura de repetição para calcular a média entre todos os valores dentro da tupla.
'''
l1 = []
cont = 0
while cont < 5:
		num = int(input('Digite um número inteiro e ímpar: '))
		if (num%2 != 0):
				l1.append(num)
				cont+=1
		else:
				print('Número inválido!')
		tuple(l1)

media = sum(l1) / len(l1)
print("Média dos números:", media)