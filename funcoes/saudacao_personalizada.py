def saudacao(hora):
    if (hora < 12):
        print('Bom dia!!!')
    elif (hora >= 12 and hora < 18):
        print('Boa tarde!!!')
    else:
        print('Boa noite!!!')

def main():
    hora = int(input('Digite a hora atual (0-23): '))
    saudacao(hora)

if __name__ == '__main__':
    main()