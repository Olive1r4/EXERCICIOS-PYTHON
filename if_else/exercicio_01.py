# 1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura')

# 2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
print(f'Meu nome é {input('Nome: ')} e tenho {input('Idade: ')} anos.')

# 3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha.
print('A\nL\nU\nR\nA')

# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de 
# pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais.
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')
print(f'O valor arredondado de pi é: {round(pi,2)}')
