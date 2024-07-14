import os
import storage
from datetime import datetime

id_vendas = 0


def menu_clientes():
  print()
  print("############################################")
  print("#####         Módulo Vendas            #####")
  print("############################################")
  print("##### 1 - Cadastrar Venda            #####")
  print("##### 2 - Exibir Dados do Venda      #####")
  print("##### 3 - Alterar Dados do Venda     #####")
  print("##### 4 - Excluir Venda              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")

  resp2 = int(input("##### Escolha sua opção: "))
  return resp2


def buscar_produto(codigo_barra, produtos_comprados):
  if codigo_barra in produtos_comprados:
    return produtos_comprados[codigo_barra]

  return False


def define_metodo_pagamento(pagamento):
  if pagamento == 0:
    return "Pix"
  elif pagamento == 1:
    return "Cartão"
  else:
    return "Dinheiro"


def total_produto(preco, quantidade):
  return preco * quantidade


def cadastrar_venda(vendas_cadastradas, id):
  data_atual = datetime.now()
  data_atual_str = data_atual.strftime("%Y-%m-%d")
  preco, total_produto = 0, 0
  produtos_comprados = []

  cpf = input("Informe o CPF do cliente: ")
  print(" 0 - Pix\n 1 - Cartão\n 2 - Dinheiro\n")
  pagamento = int(input("Informe o método de pagamento: "))
  forma_pagamento = define_metodo_pagamento(pagamento)
  resp = "S"
  while resp == "S":
    codigo_produto = int(input("Informe o código de barras do produto: "))
    produto = buscar_produto(codigo_produto, storage.produtos_cadastrados)
    if produto:
      quantidade = int(input("Informe a quantidade de produto comprado: "))
      preco = produto[1]
      total_produto += quantidade * preco

      produtos_comprados.extend([codigo_produto, quantidade])
    else:
      print("Produto não encontrado")

    preco = 0
    resp = input("Deseja passar outro produto ?(S/N)").upper()
  venda = {
      "CPF": cpf,
      "data_compra": data_atual_str,
      "metodo_pagamento": forma_pagamento,
      "total_compra": total_produto,
      "produtos_comprados": produtos_comprados
  }
  vendas_cadastradas[id] = venda
  id += 1

  return vendas_cadastradas, id


def listar_vendas(vendas):
  os.system("clear")
  print("############################################")
  print("#####           Listar Vendas          #####")
  print("############################################\n")

  for chave, venda in vendas.items():
    print("-----------------")
    print("id produto: ", chave)
    print("CPF cliente: ", venda["CPF"])
    print("Data: ", venda["data_compra"])
    print("Método de pagamento: ", venda["metodo_pagamento"])
    print("Valor total: ", venda["total_compra"])
    print("-----------------")
    print("PRODUTOS COMPRADOS:")
    for i in range(0, len(venda["produtos_comprados"]), 2):
      produto_atual = buscar_produto(venda["produtos_comprados"][i],
                                     storage.produtos_cadastrados)
      if produto_atual:
        print("\tNome produto: ", produto_atual[0])
      print("\tCódigo de barra: ", venda["produtos_comprados"][i])
      print("\tQuantidade comprada: ", venda["produtos_comprados"][i + 1])
    print()


def remover_venda(vendas, id_venda):
  if id_venda in vendas:
    del vendas[id_venda]
    print("Venda removida com sucesso!")
  else:
    print("Venda não encontrada!")
  input("Tecle <ENTER> para continuar...")


def atualizar_venda(vendas):
  id = int(input("Informe o id da venda que deseja atualizar: "))
  if id in vendas:
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime("%Y-%m-%d")
    preco, total_produto = 0, 0
    produtos_comprados = []

    cpf = input("Informe o CPF do cliente: ")
    print(" 0 - Pix\n 1 - Cartão\n 2 - Dinheiro\n")
    pagamento = int(input("Informe o método de pagamento: "))
    forma_pagamento = define_metodo_pagamento(pagamento)
    resp = "S"
    while resp == "S":
      codigo_produto = int(input("Informe o código de barras do produto: "))
      produto = buscar_produto(codigo_produto, storage.produtos_cadastrados)
      if produto:
        quantidade = int(input("Informe a quantidade de produto comprado: "))
        preco = produto[1]
        total_produto += quantidade * preco

        produtos_comprados.extend([codigo_produto, quantidade])
      else:
        print("Produto não encontrado")

      preco = 0
      resp = input("Deseja passar outro produto ?(S/N)").upper()
    venda = {
        "CPF": cpf,
        "data_compra": data_atual_str,
        "metodo_pagamento": forma_pagamento,
        "total_compra": total_produto,
        "produtos_comprados": produtos_comprados
    }
    vendas[id] = venda
  else:
    print("Produto não encontrado!!!")
