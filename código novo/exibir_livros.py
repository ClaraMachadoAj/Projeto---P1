def exibir_livros(livros):
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")


    for index in range(len(livros['Nome'])):
        print(f"{livros['Nome'][index]}\t\t{livros['Autor'][index]}\t\t{livros['Categoria'][index]}\t\t{livros['Custo'][index]}\n")