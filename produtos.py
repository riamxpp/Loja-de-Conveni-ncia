id = 0
categorias_produtos = {
    1: "Bebida",
    2: "Limpeza",
    3: "Alimento",
    4: "Congelados"
}


def pega_categoria_produto():
  categoria = int(
      input("""Informe o categoria do produto: 
              1: Bebida
              2: Limpeza
              3: Alimento
              4: Congelados: \t"""))

  return categorias_produtos[categoria]


def cadastrar_produto(produtos):
  nome = input("Informe o nome do produto: ")
  preco = float(input("Informe o preço do produto: "))
  categoria = pega_categoria_produto()
  estoque = int(input("Qual a quantidade de produtos ?"))
  codigo_barra = int(input("Qual o código de barras ?"))
  produtos[codigo_barra] = [nome, preco, categoria, estoque]

  return produtos


def listar_produtos(produtos):
  codigo_barra = input("Informe o código de barras do produto: ")
  if codigo_barra in produtos:
    print("Nome: ", produtos[codigo_barra][0])
    print("Preço: ", produtos[codigo_barra][1])
    print("Categoria: ", produtos[codigo_barra][2])
    print("Quantidade em estoque: ", produtos[codigo_barra][3])
    print("Código de barras: ", produtos[codigo_barra][4])
    print("--------------------")
  else:
    print("Produto inexistente!")

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
  codigo_barra = int(
      input("Qual o código de barras do produto que deseja remover ?"))
  if codigo_barra in produtos:
    del produtos[codigo_barra]
    print("Aluno excluído com sucesso!")
  else:
    print("Código de barras não encontrado!")
    
  input("Tecle <ENTER> para continuar...")

def atualizar_produto(id, produtos):

  for produto in produtos:
    if id == produto["id"]:
      print("Você vai atualizar o produto %d" % produto["nome"])
      confirmacao = input("Você realmente deseja atualiza-lo ?(S/N)")
      if confirmacao.upper() == "S":
        nome = input("Qual o novo nome do produto ? ")
        preco = input("Qual o novo preço do produto ? ")

        print()
      else:
        print("Operação finalizada!")
