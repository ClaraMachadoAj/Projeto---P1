import os
os.system('cls')

from selecionar_linha import selecionar_linha

biblioteca  = 'biblioteca.txt' 


def visualizar_livro(generos):
  per = input("O que você deseja visualizar? [geral, genero, favoritos] ").upper()
    
  arquivo = open('biblioteca.txt', 'r', encoding='utf-8')

  if per == 'GERAL':
      print(arquivo.read())
      
    
  elif per == 'GENERO':

    for index in range(len(generos)):
        print(f'{generos[index]}')

    escolha = input('Qual gênero você deseja visualizar? ')

    arquivo = open(biblioteca, 'r', encoding = 'utf8') 
    selecionar_linha(arquivo, escolha)

      
      
  elif per == 'FAVORITOS':
    print(arquivo.read().find("Favorito"))
    
    
  arquivo.close()

while True:
   visualizar_livro(generos)