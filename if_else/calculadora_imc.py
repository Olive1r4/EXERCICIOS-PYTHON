def calcular_imc(peso, altura):
    return peso / (altura**2)

def main():
    peso = float(input('Digite seu peso (Kg): '))
    altura = float(input('Digite sua altura (m): '))

    imc = calcular_imc(peso, altura)
    print(f'Seu IMC é: {imc:.2f}')

    if (imc < 25):
        print('Você está com peso norma.')
    else:
        print('Você está acima do peso')

if __name__ == '__main__':
    main()