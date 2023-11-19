import os
os.system ('cls')

#O ATUALIZAR CUSTO E CATEGORIA NÃO ESTÃO FUNCIONANDO

custo_total = 0.0

livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}
biblioteca = 'biblioteca.txt'

def exibir_livros():
    print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
    for i in range(len(livros['Nome'])):
        print(f"{livros['Nome'][i]}\t\t{livros['Autor'][i]}\t\t{livros['Categoria'][i]}\t\t{livros['Custo'][i]}\n")

def adicionar_livro():
    global custo_total #deixando custo_total uma variável global
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
        custo_total += custo

        arquivo = open('biblioteca.txt', 'a', encoding='utf-8')
        arquivo.write(f"Nome: {nome}, Autor: {autor}, Categoria: {categoria}, Custo: {custo}\n")
        arquivo.close()

        print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
        exibir_livros()

        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

        if desejo != 'S':
            break

def excluir_livro():
    nome_livro_excluir = input("Qual o nome do livro que você deseja excluir?\n").title()
    if nome_livro_excluir not in livros['Nome']:
        print("Livro não encontrado na biblioteca.")
        return

    indice_livro_excluir = livros['Nome'].index(nome_livro_excluir)
    custo_excluir = livros['Custo'][indice_livro_excluir]
    
    # Atualizando custo_total
    global custo_total
    custo_total -= custo_excluir

    # Removendo o livro da lista
    livros['Nome'].pop(indice_livro_excluir)
    livros['Autor'].pop(indice_livro_excluir)
    livros['Categoria'].pop(indice_livro_excluir)
    livros['Custo'].pop(indice_livro_excluir)

    # Atualizando o arquivo
    with open(biblioteca, 'w', encoding='utf-8') as arquivo:
        for i in range(len(livros['Nome'])):
            arquivo.write(f"Nome: {livros['Nome'][i]}, Autor: {livros['Autor'][i]}, Categoria: {livros['Categoria'][i]}, Custo: {livros['Custo'][i]}\n")

    print(f"Livro '{nome_livro_excluir}' removido com sucesso.")
    print(f"Custo total atualizado: {custo_total:.2f}")

def atualizar_nome_livro(nome_antigo, novo_nome):
    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    with open('biblioteca.txt', 'w', encoding='utf-8') as arquivo:
        for linha in linhas:
            if f"Nome: {nome_antigo}" in linha:
                linha = linha.replace(nome_antigo, novo_nome)
            arquivo.write(linha)

    print(f"Nome do livro atualizado para {novo_nome}")

def atualizar_categoria_livro(nome_livro, nova_categoria):
    with open('biblioteca.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    with open('biblioteca.txt', 'w', encoding='utf-8') as arquivo:
        for i, linha in enumerate(linhas):
            if f"Nome: {nome_livro}" in linha and i < len(livros['Categoria']):
                linhas[i] = linha.replace(f"Categoria: {livros['Categoria'][i]}", f"Categoria: {nova_categoria}")

        arquivo.writelines(linhas)
        print(f"Categoria do livro atualizada para {nova_categoria}")

def atualizar_custo_livro(nome_livro_custo, novo_custo):
    with open('biblioteca.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    with open('biblioteca.txt', 'w', encoding='utf-8') as arquivo:
        for i, linha in enumerate(linhas):
            if f"Nome: {nome_livro_custo}" in linha and i < len(livros['Custo']):
                linhas[i] = linha.replace(f"Custo: {livros['Custo'][i]}", f"Custo: {novo_custo}")

        arquivo.writelines(linhas)

    print(f"Custo do livro atualizado para {novo_custo}")

def visualizar_livros():
    with open('biblioteca.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

print('Olá Nathália!')

while True:
    direcionamento = input('O que você gostaria de realizar hoje? [adicionar, visualizar, atualizar, excluir ou sair]: \n').upper()

    if direcionamento == 'ADICIONAR':
        adicionar_livro()

    elif direcionamento == 'EXCLUIR':
        excluir_livro()    

    elif direcionamento == 'ATUALIZAR':
        while True:
            pergunta = input("O que você deseja atualizar? [Nome, Categoria, Custo, Sair]\n").lower()

            #FUNCIONANDO
            if pergunta == 'nome':
                nome_antigo = input("Qual o nome do livro que você deseja atualizar?\n").title()

                with open(biblioteca, 'r') as arquivo:
                    linhas = arquivo.readlines()

                livro_encontrado = False

                with open(biblioteca, 'w') as arquivo:
                    for indice, verificador in enumerate(linhas):
                        if nome_antigo in verificador:
                            livro_encontrado = True
                            novo_nome = input("Qual é o novo nome do livro?\n").title()
                            linhas[indice] = linhas[indice].replace(nome_antigo, novo_nome)
                            atualizar_nome_livro(nome_antigo, novo_nome)

                    arquivo.writelines(linhas)

                if not livro_encontrado:
                    print("Livro não encontrado na biblioteca.")
                    continue
            #FUNCIONANDO
                

            elif pergunta == 'categoria':
                nome_livro = input("Qual o nome do livro que você deseja atualizar a categoria?\n").title()

                with open(biblioteca, 'r') as arquivo:
                    linhas = arquivo.readlines()

                    livro_encontrado = False

                with open(biblioteca, 'w') as arquivo:
                    for indice, verificador in enumerate(linhas):
                        if nome_livro in verificador:
                            livro_encontrado = True
                            nova_categoria = input("Qual é a nova categoria do livro?\n").title()
                            linhas[indice] = verificador.replace(nome_livro, nova_categoria)
                            atualizar_categoria_livro(nome_livro, nova_categoria)

                    arquivo.writelines(linhas)

                if livro_encontrado == False:
                    print("Livro não encontrado na biblioteca.")
                    continue

# gente, eu fiquei feliz mas o custo não tá substituindo, help

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

    elif direcionamento == 'VISUALIZAR':
        visualizar_livros()

    elif direcionamento == 'SAIR':
        print('Volte sempre Nathália! :D')
        print(f"Custo total: {custo_total:.2f}")
        break

