def cria_desconto(percentual):
    def aplica_desconto(preco):
        return preco * (1 - percentual / 100)
    return aplica_desconto

def main():
    desconto = cria_desconto(int(input('Digite a porcentagem de desconto: ')))
    valor = float(input('Digite o valor da compra: '))

    print(f'Preço final com desconto: {desconto(valor)}')

if __name__ == '__main__':
    main()
