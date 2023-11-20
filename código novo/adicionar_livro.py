import os
os.system('cls')

from exibir_livros import exibir_livros


biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = []

def adicionar_livro():
  
    nome = (input("Qual o nome do livro? ")).upper()
    
    if nome in livros['NOME']:
      return print("Este livro já existe em sua biblioteca!")
      
      
    autor = (input("\nQuem escreveu este livro? ")).upper()
      
    genero = input('\nQual gênero literário é o seu livro? ').upper()
    if genero not in generos:
      generos.append(genero)
  
    custo = float(input("\nQuanto custou esse livro? "))
    
    favoritado = input('\nEste livro é um de seus favoritos? [Sim ou Não] ').upper()
    
    if favoritado == 'SIM':
      livros['FAVORITO'].append(favoritado)
    
    
    livros['NOME'].append(nome)
    livros['AUTOR'].append(autor)
    livros['GENERO'].append(genero)
    livros['CUSTO'].append(custo)
    
    arquivo = open('biblioteca.txt', 'r+', encoding='utf-8')
    
    if favoritado == 'SIM':
      arquivo.write(f"Nome: {nome}; Autor: {autor}; Genêro Literário: {genero}; Custo: {custo}; Favorito")
    else:
      arquivo.write(f"Nome: {nome}; Autor: {autor}; Genêro Literário: {genero}; Custo: {custo}\n")
    
    arquivo.close()
    
    print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
    exibir_livros(livros)
    
adicionar_livro()