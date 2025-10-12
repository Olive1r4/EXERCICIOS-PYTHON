def main():
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    op = input('Escolha a operação (| + | - | * | / |): ')

    match op:
        case "+":
            print(f'O resultado é: {(lambda x, y: x + y)(x, y)}')
        case "-":
            print(f'O resultado é: {(lambda x, y: x - y)(x, y)}')
        case "*":
            print(f'O resultado é: {(lambda x, y: x * y)(x, y)}')
        case "/":
            print(f'O resultado é: {(lambda x, y: x / y)(x, y) if y != 0
                                    else 'Erro: Divisão por zero'}')

if __name__ == '__main__':
    main()
