import os
os.system('cls')


def atualizar_nome():

    nome_antigo = input('Qual nome você deseja alterar? ')
    arquivo = open('biblioteca.txt', 'r')
    arquivo_manipular = arquivo.readlines()
    for verificador in arquivo:
        
            

atualizar_nome()