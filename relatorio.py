import os


def menu_relat():
  os.system('clear')
  print("############################################")
  print("#####         Módulo Relatório         #####")
  print("############################################")
  print("##### 1 - Lista Geral de Cliente       #####")
  print("##### 2 - Lista Geral de Produtos      #####")
  print("##### 3 - Lista Geral de Vendas        #####")
  print("##### 4 - Lista de Compras por Cliente #####")
  print("##### 5 - Lista de Produtos vendiso    #####")
  print("##### 0 - Retornar ao Menu Principal   #####")
  op_relat = int(input("##### Escolha sua opção: "))
  return op_relat


def lista_geral_clientes(clientes):
  os.system('clear')
  print()
  print(
      "##################################################################################"
  )
  print(
      "######################      Relatório Geral de Clientes     ######################"
  )
  print(
      "##################################################################################"
  )
  print("|-----------|--------------|-------------------|-----------------|")
  print("|    CPF    |    Nome      |       Idade       |     Celular     |")
  print("|-----------|--------------|-------------------|-----------------|")
  for cliente in clientes.items():
    print("| %-9s " % (cliente[0]), end='')
    print("| %-12s " % (cliente[1][0]), end='')
    print("| %-17s " % (cliente[1][2]), end='')
    print("| %-15s |" % (cliente[1][3]))
  print()
  input("Tecle <ENTER> para continuar...")


def lista_geral_produtos(produtos):
  os.system('clear')
  print()
  print(
      "##################################################################################"
  )
  print(
      "######################      Relatório Geral de Produtos     ######################"
  )
  print(
      "##################################################################################"
  )
  print(
      "|-------------------|--------------|-------------------|---------------|"
  )
  print(
      "|  Código de barra  |    Nome      |      Estoque      |     Preço     |"
  )
  print(
      "|-------------------|--------------|-------------------|---------------|"
  )
  for produto in produtos.items():
    print("| %-17s " % (produto[0]), end='')
    print("| %-12s " % (produto[1][0]), end='')
    print("| %-17s " % (produto[1][3]), end='')
    print("| %-13s |" % (produto[1][1]))
  print()
  input("Tecle <ENTER> para continuar...")
