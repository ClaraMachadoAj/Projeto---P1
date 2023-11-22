import os
os.system('cls')

from selecionar_linha import selecionar_linha

biblioteca  = 'biblioteca.txt' 


def visualizar_livro():
  per = input("O que você deseja visualizar? [geral, genero, favoritos] ").upper()
    
  arquivo = open('biblioteca.txt', 'r', encoding='utf-8')

  if per == 'GERAL':
      print(arquivo.read())
      
    
  elif per == 'GENERO':

    escolha = input('Qual gênero você deseja visualizar? ').upper()

    linhas = arquivo.readlines()
    linhas_filtradas = [linha for linha in linhas if escolha in linha]
    if not linhas_filtradas:
       print('Esse gênero não existe em sua biblioteca')
    for linha in linhas_filtradas:
        print(linha)

      
      
  elif per == 'FAVORITOS':
    print(arquivo.read().find("Favorito"))
    
    
  arquivo.close()


visualizar_livro()