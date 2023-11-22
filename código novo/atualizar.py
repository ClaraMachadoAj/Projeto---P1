import os
os.system('cls')

def atualizar():
    verificador = ''

    nome_antigo = input('Qual nome do livro você deseja alterar? ').upper()
    arquivo = open('biblioteca.txt', 'r')
    arquivo_manipular = arquivo.readlines()
    arquivo.close()
    cont_a = 0
    for linha in arquivo_manipular:
        if nome_antigo in linha:

            fav = input("Para modificar um valor de um livro existente digite: MODIFICAR\nPara adicionar ou remover um livro como favorito digite: FAVORITO\n\n").upper()
            if fav == "MODIFICAR":
                linha_split = linha.split("; ")
                arquivo = open('biblioteca.txt', 'w+', encoding='utf-8')
                choose = input("O que voce deseja alterar: Nome, Autor, Categoria ou Custo\n").upper()

                if choose == 'NOME':
                    alteracao = input("Novo nome do livro:").upper()
                    linha_split[0] = alteracao
                    arquivo.write("; ".join(linha_split))
                    arquivo.close()

                elif choose == 'AUTOR':
                    alteracao = input("Nome do novo autor:").upper()
                    linha_split[1] = alteracao
                    arquivo.write("; ".join(linha_split))
                    arquivo.close()

                elif choose == 'CATEGORIA':
                    alteracao = input("Nova categoria do livro:").upper()
                    linha_split[2] = alteracao
                    arquivo.write("; ".join(linha_split))
                    arquivo.close()

                elif choose == 'CUSTO':
                    alteracao = input("Novo valor do livro:").upper()
                    linha_split[3] = alteracao
                    arquivo.write("; ".join(linha_split))
                    arquivo.close()

            elif fav == "FAVORITO":
                choose_fav = input("Para remover dos FAVORITOS digite: DESFAVORITAR\nPara adicionar digite: FAVORITAR").upper()
                if choose_fav == "DESFAVORITAR":
                    for i in range(len(arquivo_manipular)):
                        if nome_antigo in arquivo_manipular[i]:
                            arquivo_manipular.pop(i)
                            arquivo = open('biblioteca.txt', 'w+', encoding='utf-8')
                            arquivo.writelines("; ".join(arquivo_manipular))
                            arquivo.close()
                            break

            cont_a += 1
            arquivo.close()
    if cont_a == 0:
        print("O livro inserido não foi encontrado na biblioteca")


atualizar()
