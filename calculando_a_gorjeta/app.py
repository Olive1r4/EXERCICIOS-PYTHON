from calcula_gorjeta import calcula_gorjeta

def main():
    try:
        valor_da_conta = float(input('Digite o valor da conta: '))
        porcentagem = float(input('Digite a porcentagem de gorjeta: '))

        valor_da_gorjeta = calcula_gorjeta(valor_da_conta, porcentagem)

        print(f'Valor da gorjeta: R$ {valor_da_gorjeta}')
        print(f'Total a pagar: R$ {valor_da_conta + valor_da_gorjeta}')
    except ValueError:
        print('ERRO: Digite apenas números válidos!!!')

if __name__ == '__main__':
    main()
