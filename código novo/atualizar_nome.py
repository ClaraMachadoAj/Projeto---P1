import os
os.system('cls')


def atualizar_nome():
    verificador = ''

    nome_antigo = input('Qual nome você deseja alterar? ')
    arquivo = open('biblioteca.txt', 'r')
    arquivo_manipular = arquivo.readlines()
    arquivo.close()
    cont_a = 0
    for linha in arquivo_manipular:
            if nome_antigo in linha:

                fav = input("Para modificar um valor de um livro existente digite: MODIFICAR\nPara adicionar ou remover um livro como favorito digite: FAVORITO").upper()
                if fav == "MODIFICAR":
                    linha.split(";")
                    arquivo = arquivo.open('bilbioteca.txt' , 'a')
                    choose = input("O que voce deseja alterar: NOME , AUTOR , CATEGORIA , CUSTO ").upper()
                    
                    if choose == 'NOME':
                        novo_nome = input("Novo nome do livro:")

                    elif choose == 'AUTOR':
                        novo_autor = input("Nome do novo autor:")
                        
                    elif choose == 'CATEGORIA':
                        novo_cat = input("Nova categoria do livro:")

                    elif choose == 'CUSTO':
                         novo_custo = input("Novo valor do livro:")

                elif fav == "FAVORITO":
                    choose_fav = input("Para remover dos FAVORITOS digite: DESFAVORITAR\nPara adicionar digite: FAVORITAR").upper()
                    if choose_fav == "FAVORITAR":

                    elif choose_fav == "DESFAVORITAR":
                         
                    else:
                         print("Comando Inválido!!!")
                cont_a += 1
                

arquivo.close()
          
                      


    if cont_a == 0:
            print("O livro inserido não foi encontrado na biblioteca") 
    arquivo = open('biblioteca.txt', 'w', encoding='utf-8')
    arquivo.writelines(linhas)
    arquivo.close()


atualizar_nome()

