import os
os.system('cls')

biblioteca = {}
custo_total = 0.0
biblioteca  = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO':[], 'FAVORITO:': []}

def adicionar_livro():
    nome = (input("Qual o nome do livro?")).upper()
    if nome in livros['NOME']:
        print("Este livro já existe em sua biblioteca!")
        continue
    autor = (input("Quem escreveu este livro? ")).upper()
    def genero_literario():
        genero = input('Qual gênero literário é o seu livro? ').upper()
        return map()
    custo = float(input("Quanto custou esse livro? "))
    
    