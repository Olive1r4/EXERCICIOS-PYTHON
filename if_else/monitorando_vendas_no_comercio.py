    # Lista de produtos
produtos = [
    {'nome':'Maçãs', 'qtd':0},
    {'nome':'Bananas', 'qtd':0}
]

def cadastrar_vendas():
    for produto in produtos:
        produto['qtd'] = int(input(f'Digite a quantidade de {produto['nome']} vendidas: '))

def maior_venda():
    maior = produtos[0]
    for produto in produtos:
        if produto['qtd'] > maior['qtd']:
            maior = produto

    print(f'As {maior['nome']} tiveram mais vendas')

def main():
    cadastrar_vendas()
    maior_venda()
    
if __name__ == '__main__':
    main()