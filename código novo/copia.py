import os
os.system('cls')

from visualizar_livro import visualizar_livro
from atualizar_nome import atualizar_nome

biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = []

#FUNÇÕES PRINCIPAIS

def atualizar_nome():

  # Verifica se o livro existe

  nome_do_livro = input("Qual livro você deseja atualizar? ")

  arquivo = open(biblioteca, 'r', encoding='utf-8')

  for linha in arquivo:
    if nome_do_livro in linha and linha.split(';')[0] == nome_do_livro:
      existe = True
      break
  else:
    existe = False

  arquivo.close()

  # Atualiza o nome do livro

  if existe:
    novo_nome = input("Qual o novo nome do livro? ")

    arquivo = open(biblioteca, 'r+', encoding='utf-8')

    for linha in arquivo:
      if nome_do_livro in linha:
        linha = linha.replace(nome_do_livro, novo_nome)

    arquivo.seek(0)
    arquivo.truncate()
    arquivo.writelines(arquivo)

    arquivo.close()

  else:
    print("O livro não existe.")


def adicionar_livro():
  
    nome = (input("Qual o nome do livro? ")).upper()
    
    arquivo = open(biblioteca, 'r', encoding = 'utf-8')
    for linha in arquivo:
      if nome in linha:
        selecao = input(f'o livro {nome} já existe em sua biblioteca, você deseja continuar? ').upper()
      else:
        selecao = 'SIM'
    arquivo.close()

    if selecao == 'SIM':
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
    
      arquivo = open('biblioteca.txt', 'a', encoding='utf-8')
    
      if favoritado == 'SIM':
        arquivo.write(f"{nome}; {autor}; {genero}; {custo}; Favorito\n")
      else:
        arquivo.write(f"{nome}; {autor}; {genero}; {custo}\n")
    
    arquivo.close()
    
    print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
    exibir_livros(livros)
 
def visualizar_livro(generos):
  per = input("O que você deseja visualizar? [geral, genero, favoritos, lista] ").upper()
    
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
#FUNÇÕES PRINCIPAIS

#FUNÇÕES COMPLEMENTARES
def selecionar_linha(arquivo):
  for linha in arquivo:
          print(linha.strip())

def exibir_livros(livros):
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")


    for index in range(len(livros['NOME'])):
        print(f"{livros['NOME'][index]}\t\t{livros['AUTOR'][index]}\t\t{livros['GENERO'][index]}\t\t{livros['CUSTO'][index]}\n")
#FUNÇÕES COMPLEMENTARES

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
    elif direcionamento == 'ATUALIZAR':
        atualizar_nome()
    #EXCLUIR LIVRO: