# LOJA DE CONVENIÊNCIA
# CLIENTES
# VENDAS
# PRODUTOS
# RELATÓRIO
# INFORMAÇÕES
import os
import produtos

produtos_cadastrados = {}
resp = ""

while resp != "0":
  os.system("clear")
  print("#############################")
  print("### LOJA DE CONVENIÊNCIA ####")
  print("#### 1 - CLIENTES       #####")
  print("#### 2 - VENDAS         #####")
  print("#### 3 - PRODUTOS       #####")
  print("#### 4 - RELATÓRIO      #####")
  print("#### 5 - INFORMAÇÕES    #####")
  print("#### 0 - SAIR           #####")
  resp = input("#### ESCOLHA A SUA OPÇÃO: ")

  if resp == "1":
    print()
    print("CLIENTE")
    input("Tecle <ENTER> para continuar...")
  elif resp == "2":
    print()
    print("############################################")
    print("#####         Módulo Produto         #####")
    print("############################################")
    print("##### 1 - Cadastrar Produto          #####")
    print("##### 2 - Exibir Dados do Produto    #####")
    print("##### 3 - Alterar Dados do Produto   #####")
    print("##### 4 - Excluir Produto            #####")
    print("##### 0 - Retornar ao Menu Principal   #####")
    resp2 = int(input("##### Escolha sua opção: "))

    if resp2 == 1:
      produtos_cadastrados = produtos.cadastrar_produto(produtos_cadastrados)
    elif resp2 == 2:
      produtos.listar_produtos(produtos_cadastrados)
    elif resp2 == 3:
      produtos.atualizar_produto(produtos_cadastrados)
    elif resp2 == 4:
      produtos.remover_produto(produtos_cadastrados)

  elif resp == "3":
    print()
    print("PRODUTOS")
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
