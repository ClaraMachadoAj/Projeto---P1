import os
os.system('cls')

from visualizar_livro import visualizar_livro
from atualizar_nome import atualizar_nome

livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = ['FANTASIA','TERROR', 'ROMANCE', 'SUSPENSE', 'AUTOAJUDA']
biblioteca = 'biblioteca.txt'


#visualizar_livro(generos)

atualizar_nome(biblioteca)