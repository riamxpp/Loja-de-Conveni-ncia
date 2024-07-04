categorias_produtos = {
    1: "Bebida",
    2: "Limpeza",
    3: "Alimento",
    4: "Congelados"
}
import os

def menu_produtos():
  print()
  print("############################################")
  print("#####         Módulo Produto         #####")
  print("############################################")
  print("##### 1 - Cadastrar Produto          #####")
  print("##### 2 - Exibir Dados do Produto    #####")
  print("##### 3 - Alterar Dados do Produto   #####")
  print("##### 4 - Excluir Produto            #####")
  print("##### 0 - Retornar ao Menu Principal   #####")

def pega_categoria_produto():
  categoria = int(
      input("""Informe o categoria do produto: 
              1: Bebida
              2: Limpeza
              3: Alimento
              4: Congelados: \t"""))

  return categorias_produtos[categoria]


def cadastrar_produto(produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####         Cadastrar Produto        #####")
  print("############################################")
  print()

  nome = input("Informe o nome do produto: ")
  preco = float(input("Informe o preço do produto: "))
  categoria = pega_categoria_produto()
  estoque = int(input("Qual a quantidade de produtos ? "))
  codigo_barra = int(input("Qual o código de barras ? "))
  produtos[codigo_barra] = [nome, preco, categoria, estoque, codigo_barra]
  print("Produto cadastrado com sucesso!\n")

  input("Tecle <ENTER> para continuar...")
  return produtos


def listar_produtos(produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####          Listar Produto          #####")
  print("############################################")
  print()

  codigo_barra = int(input("Informe o código de barras do produto: "))
  if codigo_barra in produtos:
    print("--------------------\n")
    print("Nome: ", produtos[codigo_barra][0])
    print("Preço: ", produtos[codigo_barra][1])
    print("Categoria: ", produtos[codigo_barra][2])
    print("Quantidade em estoque: ", produtos[codigo_barra][3])
    print("Código de barras: ", produtos[codigo_barra][4])
    print("--------------------\n")
  else:
    print("Produto inexistente!\n")

  input("Tecle <ENTER> para continuar...")


"""
#irei usar no relatorio
def listar_produtos(codigo_barra, produtos):
  for produto in produtos:
    print("Nome: ", produto[codigo_barra][0])
    print("Preço: ", produto[codigo_barra][1])
    print("Categoria: ", produto[codigo_barra][2])
    print("Quantidade em estoque: ", produto[codigo_barra][3])
    print("Preço: ", produto[codigo_barra][1])
    print("--------------------")
"""


def remover_produto(produtos):
  os.system('clear')
  print()
  print("############################################")
  print("#####          Remover Produto         #####")
  print("############################################")
  print()

  codigo_barra = int(
      input("Qual o código de barras do produto que deseja remover ?"))
  if codigo_barra in produtos:
    del produtos[codigo_barra]
    print("Produto removido com sucesso!\n")
  else:
    print("Código de barras não encontrado!\n")

  input("Tecle <ENTER> para continuar...")


def atualizar_produto(produtos):
  os.system('clear')
  print("############################################")
  print("#####         Atualizar Produto        #####")
  print("############################################\n")

  codigo_de_barras = int(input("Informe o código de barras para excluir: "))

  if codigo_de_barras in produtos:
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    categoria = pega_categoria_produto()
    estoque = int(input("Qual a quantidade de produtos ? "))
    produtos[codigo_de_barras] = [
        nome, preco, categoria, estoque, codigo_de_barras
    ]
    print("Produto atualizado com sucesso!\n")
  else:
    print("Produto não encontrado!\n")

  input("Tecle <ENTER> para continuar...")
