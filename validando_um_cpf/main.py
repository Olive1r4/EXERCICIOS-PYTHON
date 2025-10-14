from validar_cpf import validar_cpf

def main():

    cpf = input('Digite o seu CPF: ').strip()
    print(validar_cpf(cpf))
    
if __name__ == '__main__':
    main()
