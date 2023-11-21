import os
os.system('cls')

from visualizar_livro import visualizar_livro
from atualizar_nome import atualizar_nome
from exibir_livros import exibir_livros
from selecionar_linha import selecionar_linha
from adicionar_livro import adicionar_livro

biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = []

print ("Olá Nathália!\n O que você deseja fazer hoje? ")
direcionamento = input("[adicionar, visualizar, atualizar ou excluir]").upper()

while True:
    #ADICIONAR LIVRO
    if direcionamento == 'ADICIONAR':
        adicionar_livro()
    elif direcionamento == 'VISUALIZAR':
    #VISUALIZAR LIVRO
        visualizar_livro(generos)
    #ATUALIZAR LIVRO
    
    #EXCLUIR LIVRO:
