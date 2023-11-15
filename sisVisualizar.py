import os

livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}

def exibir_livros():
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
    for i in range(len(livros['Nome'])):
        print(f"{livros['Nome'][i]}\t\t{livros['Autor'][i]}\t\t{livros['Categoria'][i]}\t\t{livros['Custo'][i]}\n")

def adicionar_livro():
    while True:
        nome = input("Qual o nome do livro?\n").title()

        if nome in livros['Nome']:
            print('Este livro já existe em sua biblioteca!')
            continue

        autor = input("Quem escreveu este livro?\n").title()
        categoria = input("Qual a categoria do livro?\n").title()
        custo = float(input("Quanto custou este livro?\n"))

        livros['Nome'].append(nome)
        livros['Autor'].append(autor)
        livros['Categoria'].append(categoria)
        livros['Custo'].append(custo)

        arquivo = open('biblioteca.txt', 'a', encoding='utf-8')
        arquivo.write(f"Nome: {nome}, Autor: {autor}, Categoria: {categoria}, Custo: {custo}\n")
        arquivo.close()

        print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
        exibir_livros()

        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

        if desejo != 'S':
            break

def visualizar_livros():
    with open('biblioteca.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def atualizar_nome_livro(nome_antigo, novo_nome):
    # código para atualizar o nome

def atualizar_categoria_livro(nome_livro, nova_categoria):
    # código para atualizar a categoria

def atualizar_custo_livro(nome_livro_custo, novo_custo):
    # código para atualizar o custo

print('Olá Nathália!')

while True:
    direcionamento = input('O que você gostaria de realizar hoje? [adicionar, visualizar, atualizar, excluir ou sair]: \n').upper()

    if direcionamento == 'ADICIONAR':
        adicionar_livro()

    elif direcionamento == 'VISUALIZAR':
        visualizar_livros()

    elif direcionamento == 'ATUALIZAR':
        while True:
            pergunta = input("O que você deseja atualizar? [Nome, Categoria, Custo, Sair]\n").lower()

            if pergunta == 'nome':
                nome_antigo = input("Qual o nome do livro que você deseja atualizar?\n").title()
                if nome_antigo not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro = livros['Nome'].index(nome_antigo)
                novo_nome = input("Qual é o novo nome do livro?\n").title()

                livros['Nome'][indice_livro] = novo_nome
                atualizar_nome_livro(nome_antigo, novo_nome)

            elif pergunta == 'categoria':
                nome_livro = input("Qual o nome do livro que você deseja atualizar a categoria?\n").title()
                if nome_livro not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro = livros['Nome'].index(nome_livro)
                nova_categoria = input("Qual é a nova categoria do livro?\n").title()

                livros['Categoria'][indice_livro] = nova_categoria
                atualizar_categoria_livro(nome_livro, nova_categoria)

            elif pergunta == 'custo':
                nome_livro_custo = input("Qual o nome do livro que você deseja atualizar o custo?\n").title()
                if nome_livro_custo not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro_custo = livros['Nome'].index(nome_livro_custo)
                novo_custo = float(input("Qual é o novo custo do livro?\n"))

                livros['Custo'][indice_livro_custo] = novo_custo
                atualizar_custo_livro(nome_livro_custo, novo_custo)

            elif pergunta == 'sair':
                break

    elif direcionamento == 'sair':
        break