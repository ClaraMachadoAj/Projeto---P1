import os
os.system

livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}

print('Olá Nathália!')

while True:
    direcionamento = input('O que você gostaria de realizar hoje? [adicionar, visualizar, atualizar ou excluir]\n').upper()

    if direcionamento == 'ADICIONAR':
        while True:
            nome = input("Qual o nome do livro?\n").title()

            if nome in livros['Nome']:
                print('Este livro já existe em sua biblioteca!')
                continue

            autor = input("Quem escreveu este livro?\n").title()
            categoria = input("Qual a categoria do livro?\n").title()
            custo =(input("Quanto custou este livro?\n"))

            livros['Nome'].append(nome)
            livros['Autor'].append(autor)
            livros['Categoria'].append(categoria)
            livros['Custo'].append(custo)

            arquivo = open('biblioteca.txt', 'a', encoding = 'utf-8')
            arquivo.write(f"Nome: {nome}, Autor: {autor}, Categoria: {categoria}, Custo: {custo}\n")
            arquivo.close()

            print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
            print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
            print(f"{nome}\t\t{autor}\t\t{categoria}\t\t{custo}\n")

            desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

            if desejo != 'S':
                print(livros)
                break

    elif direcionamento == 'ATUALIZAR':
        while True:
            pergunta = input("O que você deseja atualizar? [Nome, Categoria, Custo, Sair]\n").lower()

            #NOME

            if pergunta == 'nome':
                nome_antigo = input("Qual o nome do livro que você deseja atualizar?\n").title()

                if nome_antigo not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro = livros['Nome'].index(nome_antigo)

                novo_nome = input("Qual é o novo nome do livro?\n").title()

                livros['Nome'][indice_livro] = novo_nome

                with open('biblioteca.txt', 'r') as arquivo:
                    linhas = arquivo.readlines()

                with open('biblioteca.txt', 'w', encoding = 'utf-8') as arquivo:
                    for linha in linhas:
                        if f"Nome: {nome_antigo}" in linha:
                            linha = linha.replace(nome_antigo, novo_nome)
                        arquivo.write(linha)

                print(f"Nome do livro atualizado para {novo_nome}")

                #CATEGORIA

            elif pergunta == 'categoria':
                nome_livro = input("Qual o nome do livro que você deseja atualizar a categoria?\n").title()

                if nome_livro not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro = livros['Nome'].index(nome_livro)

                nova_categoria = input("Qual é a nova categoria do livro?\n").title()

                livros['Categoria'][indice_livro] = nova_categoria

                with open('biblioteca.txt', 'r', encoding = 'utf-8') as arquivo:
                    linhas = arquivo.readlines()

                with open('biblioteca.txt', 'w', encoding = 'utf-8') as arquivo:
                    for linha in linhas:
                        if f"Nome: {nome_livro}" in linha:
                            linha = linha.replace(f"Nome: {nome_livro_custo}, Autor: {livros['Autor'][indice_livro_custo]}, Categoria: {livros['Categoria'][indice_livro_custo]}, Custo: {livros['Custo'][indice_livro_custo]}", f"Nome: {nome_livro_custo}, Autor: {livros['Autor'][indice_livro_custo]}, Categoria: {livros['Categoria'][indice_livro_custo]}, Custo: {novo_custo}")
                        arquivo.write(linha)

                print(f"Categoria do livro atualizada para {nova_categoria}")

                #CUSTO

            elif pergunta == 'custo':
                nome_livro_custo = input("Qual o nome do livro que você deseja atualizar o custo?\n").title()

                if nome_livro_custo not in livros['Nome']:
                    print("Livro não encontrado na biblioteca.")
                    continue

                indice_livro_custo = livros['Nome'].index(nome_livro_custo)

                novo_custo = float(input("Qual é o novo custo do livro?\n"))

                # Atualizar o custo na lista
                livros['Custo'][indice_livro_custo] = novo_custo

                # Atualizar o custo no arquivo
                with open('biblioteca.txt', 'r', encoding = 'utf-8') as arquivo:
                    linhas = arquivo.readlines()

                with open('biblioteca.txt', 'w', encoding = 'utf-8') as arquivo:
                    for linha in linhas:
                        if f"Nome: {nome_livro_custo}" in linha:
                            linha = linha.replace(f"Custo: {livros['Custo'][indice_livro_custo]}", f"Custo: {novo_custo}")
                        arquivo.write(linha)

                print(f"Custo do livro atualizado para {novo_custo}")

            elif pergunta == 'sair':
                break