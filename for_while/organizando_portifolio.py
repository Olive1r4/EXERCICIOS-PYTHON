def main():

    projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
    for projeto in projetos:
        if projeto != None:
            print(projeto)
        else:
            print('Projeto ausente')

if __name__ == '__main__':
    main()