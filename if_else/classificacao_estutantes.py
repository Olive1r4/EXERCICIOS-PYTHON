def calcular_media(nota1, nota2, nota3):
    soma_total = (nota1 + nota2 + nota3)
    return soma_total/3

def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = calcular_media(nota1, nota2, nota3)
    print(f'Média: {media:.2f}')

    if (media >= 7):
        print('Aprovado')
    elif (media >= 5 or media < 7):
        print('Recuperação')
    else:
        print('Reprovado')

if __name__ == '__main__':
    main()