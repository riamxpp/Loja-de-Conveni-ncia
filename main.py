import os
import produtos
import Clientes
import storage
import vendas
import pickle
import storage
import relatorio

try:
  arq_produtos = open("produtos.dat", "rb")
  alunos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
arq_produtos.close()

try:
  arq_clientes = open("Clientes.dat", "rb")
  alunos = pickle.load(arq_clientes)
except:
  arq_clientes = open("Clientes.dat", "wb")
arq_clientes.close()

try:
  arq_vendas = open("vendas.dat", "rb")
  alunos = pickle.load(arq_vendas)
except:
  arq_vendas = open("vendas.dat", "wb")
arq_vendas.close()

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
    resp4 = relatorio.menu_relat()
    if resp4 == 1:
      relatorio.lista_geral_clientes(storage.clientes_cadastrados)
    elif resp4 == 2:
      print()
    elif resp4 == 3:
      print()
    elif resp4 == 4:
      print()
    elif resp4 == 5:
      print()
    input("Tecle <ENTER> para continuar...")
  elif resp == "5":
    print()
    print("INFORMAÇÕES")
    input("Tecle <ENTER> para continuar...")

print("FIM DO PROGRAMA")

arq_produtos = open("produtos.dat", "wb")
pickle.dump(storage.produtos_cadastrados, arq_produtos)
arq_produtos.close()

arq_clientes = open("Clientes.dat", "wb")
pickle.dump(storage.clientes_cadastrados, arq_clientes)
arq_clientes.close()

arq_vendas = open("vendas.dat", "wb")
pickle.dump(storage.vendas_cadastradas, arq_vendas)
arq_vendas.close()
