''''
3 - Fazer um dicionário e adicionar 3 disciplinas com sua respectiva nota (ex: {'algoritmos': 90, 'física': 90, 'matemática': 80}), depois criar uma estrutura que encontre dentro do dicionário qual foi a menor nota.
'''
d1 = {'algoritmos': 90, 'física': 100, 'matemática': 100}

print(f'Menor nota: {d1[min(d1, key=d1.get)]}')