def cadastrar_atividades():
    atividade_a = int(input('Informe os dias para a atividade A: '))
    atividade_b = int(input('Informe os dias para a atividade B: '))
    atividade_c = int(input('Informe os dias para a atividade C: '))

    if ((atividade_a or atividade_b or atividade_c) < 0):
        print('Erro: Os dias não podem ser negativos')
    else:
        print(f'Tempo total: {(atividade_a + atividade_b+ atividade_c)}')

def main():
    cadastrar_atividades()

if __name__ == '__main__':
    main()