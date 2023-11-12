import os
os.system('cls')

import csv


# Função para adicionar um livro
def add_livro():
    while True:
        nome = input("Qual o nome do livro?\n").title()

        if nome in livros['Nome']:
            print('Este livro já existe em sua biblioteca!')
        else:
            autor = input("Quem escreveu este livro?\n").title()
            categoria = input("Qual a categoria do livro?\n").title()
            custo = float(input("Quanto custou este livro?\n"))

            livros['Nome'].append(nome)
            livros['Autor'].append(autor)
            livros['Categoria'].append(categoria)
            livros['Custo'].append(custo)

            print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
            print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
            print(f"{nome}\t\t{autor}\t\t{categoria}\t\t{custo}\n")

        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()
        if desejo != 'S':
            break

# Função para salvar os livros em um arquivo CSV
def salvar_em_csv():
    with open('biblioteca.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nome', 'Autor', 'Categoria', 'Custo'])

        for i in range(len(livros['Nome'])):
            writer.writerow([livros['Nome'][i], livros['Autor'][i], livros['Categoria'][i], livros['Custo'][i]])

# Função para carregar os livros de um arquivo CSV
def carregar_do_csv():
    try:
        with open('biblioteca.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                livros['Nome'].append(row['Nome'])
                livros['Autor'].append(row['Autor'])
                livros['Categoria'].append(row['Categoria'])
                livros['Custo'].append(float(row['Custo']))
    except FileNotFoundError:
        pass

def visualizar_livros(livros):
    for livro in livros:
        print(livro)

# Inicializar a biblioteca
livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}

# Tentar carregar os livros do arquivo CSV
carregar_do_csv()

# Seção principal do código
while True:
    direcionamento = input('O que você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir)\n ').upper()

    if direcionamento == 'ADICIONAR':
        add_livro()
        salvar_em_csv()

    elif direcionamento == 'VISUALIZAR':
        visualizar_livros(livros)
        salvar_em_csv()
        

    elif direcionamento == 'ATUALIZAR':
        # Implemente a lógica para atualizar livros
        salvar_em_csv()
        

    elif direcionamento == 'EXCLUIR':
        # Implemente a lógica para excluir livros
        salvar_em_csv()
        
    elif direcionamento == 'SAIR':
        # Salvar a biblioteca no arquivo CSV antes de sair
        salvar_em_csv()
        break

    else:
        print('Essa função não existe neste sistema')
        continue
