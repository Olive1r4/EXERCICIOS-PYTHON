def main():

    estoque = 5
    while estoque > 0:
        print(f'Venda realizada! Estoque restante: {estoque - 1}')
        estoque -= 1
    print('Estoque esgotado')

if __name__ == '__main__':
    main()