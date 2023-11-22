import os
os.system('cls')

biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO': []}
generos = []
custo_total = 0.0

#FUNÇÕES PRINCIPAIS
import os
os.system('cls')

biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO': [], 'FAVORITO': []}
generos = []
custo_total = 0.0

# FUNÇÕES PRINCIPAIS
def adicionar_livro():
    global custo_total
    nome = (input("Qual o nome do livro? ")).upper()

    try:
        if nome == '':
            raise ValueError('O nome do livro deve ser uma string não vazia.')
    except ValueError as erro:
        print(erro)
        input('\nPressione Enter para continuar...')
        return

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

      try:
        if custo <= 0:
            raise ValueError('O custo do livro deve ser um número positivo.')
      except ValueError as erro1:
        print(erro1)
        input('\nPressione Enter para continuar...')
        return

      favoritado = input('\nEste livro é um de seus favoritos? [Sim ou Não] ').upper()

      try:
        if favoritado not in ['SIM', 'NÃO']:
            raise ValueError('A resposta deve ser "Sim" ou "Não".')
      except ValueError as erro2:
        print(erro2)
        input('\nPressione Enter para continuar...')
        return

      if favoritado == 'SIM':
        livros['FAVORITO'].append(favoritado)
    
    
      livros['NOME'].append(nome)
      livros['AUTOR'].append(autor)
      livros['GENERO'].append(genero)
      livros['CUSTO'].append(custo)
      custo_total += custo
    
      arquivo = open('biblioteca.txt', 'a', encoding='utf-8')
    
      if favoritado == 'SIM':
        arquivo.write(f"{nome}; {autor}; {genero}; {custo}; Favorito\n")
      else:
        arquivo.write(f"{nome}; {autor}; {genero}; {custo}\n")
    
    print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
    exibir_livros(livros)
    print(f"O custo acumulado de todos os livros é de R${custo_total} ")

    arquivo.close()

    continuar = input('\nDeseja continuar adicionando livros? [Sim ou Não] ').upper()
    if continuar == 'SIM':
      adicionar_livro()


def visualizar_livro():
  per = input("O que você deseja visualizar? [geral, genero, favoritos]\n").upper()
    
  arquivo = open('biblioteca.txt', 'r', encoding='utf-8')

  contador_genero = 0

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
        linha_dividida = linha.split('; ')
        contador_genero += float(linha_dividida[3])
        
    print(contador_genero)

  elif per == 'FAVORITOS':
    try:
      linhas = arquivo.readlines()
      linhas_filtradas = [linha for linha in linhas if 'Favorito' in linha]
      if not linhas_filtradas:
        print('Você não tem nenhum livro favorito')
      else:
        for linha in linhas_filtradas:
          print(linha)
          
    except FileNotFoundError as erro:
      print(erro)

  arquivo.close()

  continuar = input('\nDeseja continuar visualizando livros? [Sim ou Não] ').upper()
  if continuar == 'SIM':
    visualizar_livro()


def excluir_livros():
  escolha = input('Qual livro você deseja excluir? ').upper()

  arquivo = open('biblioteca.txt', 'r', encoding='utf-8')
  linhas = arquivo.readlines()
  linhas_filtradas = [linha for linha in linhas if escolha in linha]
  if not linhas_filtradas:
      print('Esse livro não existe em sua biblioteca')
  else:
    try:
      for linha in linhas_filtradas:
        linhas.remove(linha)
      arquivo = open('biblioteca.txt', 'w', encoding='utf-8')
      arquivo.writelines(linhas)
      arquivo.close()
      print(f'O livro {escolha} foi excluído com sucesso')
      custo_total -= livros['CUSTO'][linha]
      print(f'O custo acumulado de todos os livros é de R${custo_total}')
    except IndexError as erro1:
      print(erro1)


#FUNÇÕES PRINCIPAIS

#FUNÇÕES COMPLEMENTARES
def selecionar_linha(arquivo,escolha):
  try:
    for linha in arquivo:
        if escolha in linha:
          print(linha.strip())
  except FileNotFoundError as erro:
    print(erro)
  except IndexError as erro1:
    print(erro1)


def exibir_livros(livros):
  try:
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")

    for index in range(len(livros['NOME'])):
        print(f"{livros['NOME'][index]}\t\t{livros['AUTOR'][index]}\t\t{livros['GENERO'][index]}\t\t{livros['CUSTO'][index]}\n")
  except FileNotFoundError as erro:
    print(erro)
  except IndexError as erro1:
    print(erro1)

#FUNÇÕES COMPLEMENTARES

print ("Olá Nathália! ")

while True:
    direcionamento = input("O que você deseja fazer?\n[adicionar, visualizar, atualizar ou excluir]\n").upper()

    #ADICIONAR LIVRO
    if direcionamento == 'ADICIONAR':
        adicionar_livro()

    elif direcionamento == 'VISUALIZAR':
    #VISUALIZAR LIVRO
        visualizar_livro()
      
    #ATUALIZAR LIVRO
    elif direcionamento == 'ATUALIZAR':
        atualizar()

    elif direcionamento == 'EXCLUIR':
       excluir_livros()