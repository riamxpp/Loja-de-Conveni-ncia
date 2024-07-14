#produtos[codigo_barra] = [nome, preco, categoria, estoque, codigo_barra]
produtos_cadastrados = {
    11111: ["Leite", 5.50, "Bebida", 10, 11111],
    22222: ["Feijão", 7.0, "Comida", 20, 22222],
    33333: ["Flocão", 1.50, "Comida", 20, 33333]
}
"""

"""
#clientes[cpf] = [nome, genero, idade, cpf]
clientes_cadastrados = {}
"""
  "12345": [
    "Riam", "M", 23, "12345"
  ],
  "54321": [
    "Diana", "F", 20, "22222"
  ]
"""
#vendas[id] = [cliente, produtos_comprados, valor_compra, data, metodo_pagamento]
vendas_cadastradas = {
    5: {
        "CPF": 12345,
        "data_compra": "2024-07-10",
        "metodo_pagamento": 0,
        "total_compra": 18.0,
        "produtos_comprados": [11111, 2, 22222, 1]
    },
    6: {
        "CPF": 12345,
        "data_compra": "2024-07-10",
        "metodo_pagamento": 0,
        "total_compra": 18.0,
        "produtos_comprados": [11111, 2, 22222, 1]
    }
}
#
"""
  0: [
    "cliente": {
      "cpf": 12345
    },
    "produtos_comprados": [
      "codigo_barra": 1111
    ],
    valor_compra: 100,
    data: "09/07/2024",
    metodo_pagamento: 0
  ]

  # vendas[id] = [cliente, data, metodo_pagamento, valor_compra, id_produto, quant, id_produto, quant]
  1: [12345, "09/07/2024", 0, 3250.50, 1111, 100, 2222, 20]

  # vendas[id] = [cliente, data, metodo_pagamento, valor_compra, [id_produto, quant, id_produto, quant]]
  2: [12345, "09/07/2024", 0, 3250.50, [1111, 100, 2222, 20]]
  
  
"""
