import os
os.system('cls')

def exibir_livros(livros):
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")


    for index in range(len(livros['NOME'])):
        print(f"{livros['NOME'][index]}\t\t{livros['AUTOR'][index]}\t\t{livros['GENERO'][index]}\t\t{livros['CUSTO'][index]}\n")