'''
1 - Observe a tabela abaixo.
produto            |       preço
- - - - - - - - - - - - - - - - - - - - -
Processador    |   250.50
Memória RAM |   500.25	
HDD                  |   299.99
SSD                   |   399.00
Monitor            |  1000.19
Teclado            |     50.00	
Mouse              |     30.00	

Crie um dicionário usando os dados da acima, sendo chaves e valores, respectivamente, os produtos e os preços.
Crie um laço de repetição para que o usuário digite o nome do produto e a saída do programa mostre o preço do mesmo. Caso seja digitado um produto inexistente, o programa informa a mensagem "produto inexistente". Para encerrar o programa o usuário deverá digitar "FIM".  
Exemplos de execução:
>> Informe o produto: HDD 
>> Preço do HDD: R$ 299.99

>> Informe o produto: INTIN
>> Produto não encontrado! 

>> Informe o produto: FIM
>> Obrigado por visitar nossa loja. Volte sempre! 
'''

dic = {'Processador': 250.50, 'Memoria RAM': 500.25, 'HDD': 299.99, 'SSD': 399.00, 'Monitor':1000.19, 
       'Teclado':50.00,
       'Mouse':30.30}

for _ in range(1,8):
  produto = input('Informe o produto: ')
  if produto == "Processador":
      print(dic['Processador'])
  elif produto == "Memoria RAM":
      print(dic['Memoria RAM'])
  elif produto == "HDD":
      print(dic['HDD'])
  elif produto == "SSD":
      print(dic['SSD'])
  elif produto == "Monitor":
      print(dic['Monitor'])
  elif produto == "Teclado":
      print(dic['Teclado'])
  elif produto == "Mouse":
      print(dic['Mouse'])
  elif produto == "fim":
      print('Obrigado por visitar nossa loja. Volte sempre!')     
      quit()
  else:
      print('Produto Inexistente')