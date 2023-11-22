import os
os.system('cls')

def atualizar():
    verificador = ''

    nome_antigo = input('Qual nome do livro você deseja alterar? ').upper()
    arquivo = open('biblioteca.txt', 'w+a', encoding='utf-8')
    arquivo_manipular = arquivo.readlines()
    arquivo.close()
    cont_a = 0
    for linha in arquivo_manipular:
        if nome_antigo in linha:

            fav = input("Para modificar um valor de um livro existente digite: MODIFICAR\nPara adicionar ou remover um livro como favorito digite: FAVORITO\n").upper()
            if fav == "MODIFICAR":
                linha_split = linha.split("; ")
                arquivo = io.open('biblioteca.txt', 'w+a', encoding='utf-8')
                choose = input("O que voce deseja alterar: Nome, Autor, Categoria ou Custo\n").upper()

                if choose == 'NOME':
                    novo_nome = input("Novo nome do livro: ").upper()
                    linha_split[0] = novo_nome.upper()
                    arquivo.writelines(linha_split)
                    arquivo.write("\n")

                elif choose == 'AUTOR':
                    novo_autor = input("Nome do novo autor: ").upper()
                    linha_split[1] = novo_autor.upper()
                    arquivo.writelines(linha_split)
                    arquivo.write("\n")

                elif choose == 'CATEGORIA':
                    novo_cat = input("Nova categoria do livro: ").upper()
                    linha_split[2] = novo_cat.upper()
                    arquivo.writelines(linha_split)
                    arquivo.write("\n")

                elif choose == 'CUSTO':
                    novo_custo = input("Novo valor do livro: ").upper()
                    linha_split[3] = novo_custo.upper()
                    arquivo.writelines(linha_split)
                    arquivo.write("\n")

            elif fav == "FAVORITO":
                choose_fav = input("Para remover dos FAVORITOS digite: DESFAVORITAR\nPara adicionar digite: FAVORITAR").upper()
                if choose_fav == "FAVORITAR":
                    cont
                elif choose_fav == "DESFAVORITAR":
                    cont
                else:
                    print("Comando Inválido!!!")

            cont_a += 1
            arquivo.close()

    if cont_a == 0:
        print("O livro inserido não foi encontrado na biblioteca")


atualizar()
