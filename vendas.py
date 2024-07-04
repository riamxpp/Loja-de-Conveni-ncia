def menu_vendas():
  print()
  print("############################################")
  print("#####         Módulo Cliente           #####")
  print("############################################")
  print("##### 1 - Cadastrar Cliente            #####")
  print("##### 2 - Exibir Dados do Cliente      #####")
  print("##### 3 - Alterar Dados do Cliente     #####")
  print("##### 4 - Excluir Cliente              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")

  resp2 = int(input("##### Escolha sua opção: "))
  return resp2

def cadastrar_venda(vendas):
  nome = input("Informe o nome do produto: ")
  preco = input("Informe o preço do produto: ")
  quantidade = int(input("Informe a quantidade vendida: "))
  valor_venda = preco * quantidade
  codigo_barra = int(input("Informe o código de barras do produto vendido: "))
  
  vendas[codigo_barra] = [nome, preco, quantidade, valor_venda, codigo_barra]

  return vendas