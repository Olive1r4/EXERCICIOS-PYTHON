def main():
    
    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
    buscar_livro = 'O Hobbit'
    for livro in livros:
        if (buscar_livro == livro):
            print(f'Livro encontrado: {buscar_livro}')

if __name__ == '__main__':
    main()