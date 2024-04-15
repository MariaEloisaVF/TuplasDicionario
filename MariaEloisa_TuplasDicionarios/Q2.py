'''
2 - Observe a tabela a seguir referente a uma agenda telefônica.
Nome       |   Telefone
- - - - - - - - - - - - - - - - - - 
Luiz          |   (83)999999999
Ana          |   (83)555555555
Eduarda   |   (83)222222222
Gabriel     |   (83)111111111
Anderson |   (83)888888888
Gustavo    |  (83)777777777
Liriel         |   (83)333333333

Crie um dicionário usando os dados da acima, sendo os nomes a chaves, e valores são os contatos de telefone.
Após a construção do dicionário, adicione 'Wesley' à lista telefônica com o número de telefone '(83)444444444' e 'Keliane' com o número '(83)666666666'.
Depois remova os contatos 'Luiz' e 'Gabriel' da lista telefônica.
Imprima ao final a quantidade de contatos da agenda.
'''
dic1 = {'Luiz':"(83)999999999",
	'Ana':"(83)555555555",
	'Eduarda':"(83)222222222",
	'Gabriel':"(83)111111111",
	'Anderson':"(83)888888888",
	'Gustavo':"(83)777777777",
	'Liriel':"(83)333333333"}
print(f'Lista original--> {dic1}\n')
print('------------------------------\n')
dic1['Wesley']="(83)444444444"
dic1['Keliane']="(83)666666666"

del(dic1['Luiz'])
del(dic1['Gabriel'])

print(f'Lista editada--> {dic1}\n')
print(f'Número total de contatos--> {len(dic1)}')