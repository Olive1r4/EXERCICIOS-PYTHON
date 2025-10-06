def calcula_idade(ano_nascimento, ano_atual):
    return (ano_atual - ano_nascimento)

def main():

    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: '))

    print(f'A idade é {calcula_idade(ano_nascimento, ano_atual)} anos')

if __name__ == '__main__':
    main()