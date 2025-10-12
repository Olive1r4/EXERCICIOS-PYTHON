def  soma_recursiva(num):
    if num == 1:
        return 1
    return num + soma_recursiva(num - 1)

def main():
    numero = int(input('Digite um número: '))

    print(f'A soma de 1 a {numero} é: {soma_recursiva(numero)}')

if __name__ == '__main__':
    main()
