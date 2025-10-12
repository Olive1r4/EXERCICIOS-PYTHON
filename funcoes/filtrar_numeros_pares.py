def main():
    numeros = (input('Digite os números separados por espaço: ')).split()
    pares = filter(lambda x: int(x) % 2 == 0, numeros)
    #O método join() serve para juntar elementos de uma lista (ou outro iterável) em uma única string, colocando um separador entre eles.
    print('Números pares:', ' '.join(pares))

if __name__ == '__main__':
    main()
