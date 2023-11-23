import os
os.system('cls')

def atualizar():
    nome_antigo = input('Qual nome do livro você deseja alterar? ').upper()
    encontrado = False

    try:
        arquivo = open('biblioteca.txt', 'r', encoding='utf-8')
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        print('O arquivo "biblioteca.txt" não foi encontrado.')
        return

    for i in range(len(linhas)):
        if nome_antigo in linhas[i]:
            encontrado = True
            fav = input("Para modificar um valor de um livro existente digite: MODIFICAR\n"
                        "Para adicionar ou remover um livro como favorito digite: FAVORITO\n\n").upper()
            if fav == "MODIFICAR":
                linha_split = linhas[i].split("; ")
                choose = input("O que voce deseja alterar: Nome, Autor, Categoria ou Custo\n").upper()
                
                if choose == 'NOME':
                    alteracao = input("Novo nome do livro:").upper()
                    linha_split[0] = alteracao
                elif choose == 'AUTOR':
                    alteracao = input("Nome do novo autor:").upper()
                    linha_split[1] = alteracao
                elif choose == 'CATEGORIA':
                    alteracao = input("Nova categoria do livro:").upper()
                    linha_split[2] = alteracao
                elif choose == 'CUSTO':
                    alteracao = input("Novo valor do livro:").upper()
                    linha_split[3] = alteracao
                
                linhas[i] = "; ".join(linha_split) + '\n'

            elif fav == "FAVORITO":
                choose_fav = input("Para remover dos FAVORITOS digite: DESFAVORITAR\n"
                                   "Para adicionar digite: FAVORITAR\n").upper()
                if choose_fav == "DESFAVORITAR":
                    linhas.pop(i)
                    break

    if not encontrado:
        print("O livro inserido não foi encontrado na biblioteca")
    else:
        try:
            arquivo = open('biblioteca.txt', 'w', encoding='utf-8')
            arquivo.writelines(linhas)
            arquivo.close()
        except FileNotFoundError:
            print('O arquivo "biblioteca.txt" não foi encontrado.')



atualizar()
