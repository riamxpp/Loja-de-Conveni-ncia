import os
import produtos
import Clientes
import storage
import vendas
from datetime import datetime

id_vendas = 0
resp = ""


def menu_principal():
  print("#############################")
  print("### LOJA DE CONVENIÊNCIA ####")
  print("#### 1 - CLIENTES       #####")
  print("#### 2 - PRODUTO        #####")
  print("#### 3 - VENDAS         #####")
  print("#### 4 - RELATÓRIO      #####")
  print("#### 5 - INFORMAÇÕES    #####")
  print("#### 0 - SAIR           #####")
  resp = input("#### ESCOLHA A SUA OPÇÃO: ")
  return resp


while resp != "0":
  os.system("clear")
  resp = menu_principal()

  if resp == "1":
    resp1 = Clientes.menu_clientes()
    if resp1 == 1:
      clientes_cadastrados = Clientes.cadastrar_cliente(
          storage.clientes_cadastrados)
    elif resp1 == 2:
      Clientes.listar_clientes(storage.clientes_cadastrados)
    elif resp1 == 3:
      Clientes.atualizar_cliente(storage.clientes_cadastrados)
    elif resp1 == 4:
      Clientes.remover_cliente(storage.clientes_cadastrados)

  elif resp == "2":
    resp2 = produtos.menu_produtos()

    if resp2 == 1:
      produtos_cadastrados = produtos.cadastrar_produto(
          storage.produtos_cadastrados)
    elif resp2 == 2:
      produtos.listar_produtos(storage.produtos_cadastrados)
    elif resp2 == 3:
      produtos.atualizar_produto(storage.produtos_cadastrados)
    elif resp2 == 4:
      produtos.remover_produto(storage.produtos_cadastrados)

  elif resp == "3":
    resp3 = vendas.menu_clientes()
    if resp3 == 1:
      storage.vendas_cadastradas, id = vendas.cadastrar_venda(
          storage.vendas_cadastradas, id_vendas)
    elif resp3 == 2:
      vendas.listar_vendas(storage.vendas_cadastradas)
      print()
    elif resp3 == 3:
      vendas.atualizar_venda(storage.vendas_cadastradas)
      print()
    elif resp3 == 4:
      id_venda = int(input("Informe o id da compra que deseja remover: "))
      vendas.remover_venda(storage.vendas_cadastradas, id_venda)
      print()

    print()
    print("VENDAS")
    input("Tecle <ENTER> para continuar...")
  elif resp == "4":
    print()
    print("RELATÓRIO")
    input("Tecle <ENTER> para continuar...")
  elif resp == "5":
    print()
    print("INFORMAÇÕES")
    input("Tecle <ENTER> para continuar...")

print("FIM DO PROGRAMA")
