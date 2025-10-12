def converte_valores(vendas):
    return [int(venda) for venda in vendas]

def soma_valores(valores):
    total = 0
    for valor in valores:
        total += valor
    return f'O total de vendas foi: {total}'

def main():
    valores_vendas = (input('Digite os valores das vendas: ')).split(' ')
    valores_convertidos = converte_valores(valores_vendas)
    print(soma_valores(valores_convertidos))


if __name__ == "__main__":
    main()
