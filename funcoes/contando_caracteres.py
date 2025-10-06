def conta_caractere(palavra):
    quantidade = len(palavra)
    return quantidade


def main():
    palavra = input('Digite uma palavra: ')
    print(f'Essa palavra tem {conta_caractere(palavra)} caracteres ')

if __name__ == '__main__':
    main()