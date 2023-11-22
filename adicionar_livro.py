import os
os.system('cls')

from exibir_livros import exibir_livros


biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = []

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
        arquivo.write(f"\n{nome}; {autor}; {genero}; {custo}; Favorito")
      else:
        arquivo.write(f"\n{nome}; {autor}; {genero}; {custo}")
    
    arquivo.close()
    
    print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
    exibir_livros(livros)
    
      
    

while True:
    adicionar_livro()