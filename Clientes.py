import os

def menu_clientes():
  print()
  print("############################################")
  print("#####         Módulo Cliente           #####")
  print("############################################")
  print("##### 1 - Cadastrar Cliente            #####")
  print("##### 2 - Exibir Dados do Cliente      #####")
  print("##### 3 - Alterar Dados do Cliente     #####")
  print("##### 4 - Excluir Cliente              #####")
  print("##### 0 - Retornar ao Menu Principal   #####")

def cadastrar_cliente(clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cadastrar Cliente        #####")
  print("############################################")
  print()

  nome = input("Informe o nome do cliente: ")
  genero = input("Informe o gênero do cliente: ")
  idade = int(input("Informe a idade do cliente: "))
  celular = int(input("Informe o número de celular do cliente: "))
  cpf = input("Informe o cpf do cliente: ")
  clientes[cpf] = [nome, genero, idade, celular, cpf]
  print("Cliente cadastrado com sucesso!\n")

  input("Tecle <ENTER> para continuar...")
  return clientes

def listar_clientes(clientes):
  os.system('clear')
  print("############################################")
  print("#####          Listar Clientes         #####")
  print("############################################\n")

  cpf = input("Informe o cpf do cliente: ")
  if cpf in clientes:
    print("--------------------\n")
    print("Nome: ", clientes[cpf][0])
    print("Gênero: ", clientes[cpf][1])
    print("Idade: ", clientes[cpf][2])
    print("Celular: ", clientes[cpf][3])
    print("CPF: ", clientes[cpf][4])
    print("--------------------\n")
  else:
    print("Cliente inexistente!\n")

  input("Tecle <ENTER> para continuar...")

def remover_cliente(clientes):
  os.system('clear')
  print()
  print("############################################")
  print("#####          Remover Cliente         #####")
  print("############################################")
  print()

  cpf = input("Qual o código de barras do produto que deseja remover ?")
  if cpf in clientes:
    del clientes[cpf]
    print("Cliente removido com sucesso!\n")
  else:
    print("Cpf não encontrado!\n")

  input("Tecle <ENTER> para continuar...")

def atualizar_cliente(clientes):
  os.system('clear')
  print("############################################")
  print("#####         Atualizar Cliente        #####")
  print("############################################\n")

  cpf = input("Informe o cpf do cliente para excluir: ")

  if cpf in clientes:
    nome = input("Informe o nome do cliente: ")
    genero = input("Informe o gênero do cliente(M/F): ")
    idade = int(input("Informa a idade do cliente: "))
    celular = int(input("Informe o número de celular do cliente: "))
    clientes[cpf] = [nome, genero, idade, celular, cpf]
    print("Cliente atualizado com sucesso!\n")
  else:
    print("Cliente não encontrado!\n")

  input("Tecle <ENTER> para continuar...")