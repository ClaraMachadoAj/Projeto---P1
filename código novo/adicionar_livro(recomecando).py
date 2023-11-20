import os
os.system('cls')

from exibir_livros import exibir_livros


biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO:': []}

def adicionar_livro():
  
    nome = (input("Qual o nome do livro?")).upper()
    
    if nome in livros['NOME']:
      return print("Este livro já existe em sua biblioteca!")
      
      
    autor = (input("Quem escreveu este livro? ")).upper()
      
    genero = input('Qual gênero literário é o seu livro? ').upper()
  
    custo = float(input("Quanto custou esse livro? "))
    
    favorito = input('Este livro é um de seus favoritos? [Sim ou Não] ').upper
    
    if favorito == 'SIM':
      livros['FAVORITO'].append(favorito)
    
    
    livros['NOME'].append(nome)
    livros['AUTOR'].append(autor)
    livros['GENERO'].append(genero)
    livros['CUSTO'].append(custo)
    
    arquivo = open('biblioteca.txt', 'r+', encoding='utf-8')
    
    if favorito == 'SIM':
      arquivo.write(f"Nome: {nome}; Autor: {autor}; Genêro Literário: {genero}; Custo: {custo}; Favorito")
    else:
      arquivo.write(f"Nome: {nome}; Autor: {autor}; Genêro Literário: {genero}; Custo: {custo}\n")
    
    arquivo.close()
    
    print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
    exibir_livros(livros)
    
def visualizar_livro():
  per = input("O que você deseja visualizar? [geral, categoria, favoritos] ").upper()
    arquivo = open('biblioteca.txt', 'r', encoding='utf-8')
    
    if per == 'GERAL':
      print(arquivo.read())
      
    
    elif per == 'CATEGORIA':
      categoria = input('')
      
      
    elif per == 'FAVORITOS':
      print(arquivo.read().find("Favorito"))
		    arquivo.close()