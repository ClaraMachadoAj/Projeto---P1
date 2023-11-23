import os
os.system('cls')

# Inicializando variáveis globais
biblioteca = 'biblioteca.txt'
livros = {'NOME': [], 'AUTOR': [], 'GENERO': [], 'CUSTO': [], 'FAVORITO': []}
generos = []
custo_total = 0.0

# Funções Principais
def adicionar_livro():
    global custo_total

    nome = input("Qual o nome do livro? ").upper()
    
    if nome == '':
        print('O nome do livro não pode ser vazio.')
        input('\nPressione Enter para continuar...')
        return

    try:
        with open(biblioteca, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                if nome in linha:
                    selecao = input(f'O livro {nome} já existe em sua biblioteca, deseja continuar? [Sim ou Não]').upper()
                    break
            else:
                selecao = 'SIM'
    except FileNotFoundError as erro:
        print(erro)
        selecao = 'SIM'

    if selecao == 'SIM':
        autor = input("\nQuem escreveu este livro? ").upper()

        genero = input('\nQual gênero literário é o seu livro? ').upper()
        if genero not in generos:
            generos.append(genero)

        custo = float(input("\nQuanto custou esse livro? "))

        if custo <= 0:
            print('O custo do livro deve ser um número positivo.')
            input('\nPressione Enter para continuar...')
            return

        favoritado = input('\nEste livro é um de seus favoritos? [Sim ou Não] ').upper()

        if favoritado not in ['SIM', 'NÃO', 'NAO']:
            print('A resposta deve ser "Sim" ou "Não".')
            input('\nPressione Enter para continuar...')
            return

        if favoritado == 'SIM':
            livros['FAVORITO'].append(favoritado)

        livros['NOME'].append(nome)
        livros['AUTOR'].append(autor)
        livros['GENERO'].append(genero)
        livros['CUSTO'].append(custo)
        custo_total += custo

        with open(biblioteca, 'a', encoding='utf-8') as arquivo:
            if favoritado == 'SIM':
                arquivo.write(f"{nome}; {autor}; {genero}; {custo}; Favorito\n")
            else:
                arquivo.write(f"{nome}; {autor}; {genero}; {custo}\n")

        print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
        exibir_livros(livros)
        print(f"O custo acumulado de todos os livros é de R${custo_total} ")

    continuar = input('\nDeseja continuar adicionando livros? [Sim ou Não] ').upper()
    if continuar == 'SIM':
        adicionar_livro()

def visualizar_livro():
    per = input("O que você deseja visualizar? [geral, genero, favoritos]\n").upper()

    with open(biblioteca, 'r', encoding='utf-8') as arquivo:
        contador_genero = 0
        contador_fav = 0

        if per == 'GERAL':
            print(arquivo.read())
        elif per == 'GENERO':
            escolha = input('Qual gênero você deseja visualizar? ').upper()
            linhas = arquivo.readlines()
            linhas_filtradas = [linha for linha in linhas if escolha in linha]
            if not linhas_filtradas:
                print(f'Esse gênero não existe em sua biblioteca')
            for linha in linhas_filtradas:
                print(linha)
                linha_dividida = linha.split('; ')
                contador_genero += float(linha_dividida[3])

            print(f'O seu extrato do gênero {escolha} é: {contador_genero}')

        elif per == 'FAVORITOS':
            linhas = arquivo.readlines()
            linhas_filtradas = [linha for linha in linhas if 'Favorito' in linha]
            if not linhas_filtradas:
                print('Você não tem nenhum livro favorito')
            else:
                for linha in linhas_filtradas:
                    print(linha)
                    linha_dividida_fav = linha.split('; ')
                    contador_fav += float(linha_dividida_fav[3])
                print(f'O seu extrato de seus favoritos é: {contador_fav}')

def excluir_livros():
    global custo_total
    
    escolha = input('Qual livro você deseja excluir? ').upper()

    with open(biblioteca, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        linhas_filtradas = [linha for linha in linhas if escolha in linha]
        if not linhas_filtradas:
            print('Esse livro não existe em sua biblioteca')
        else:
            try:
                for linha in linhas_filtradas:
                    linhas.remove(linha)
                with open(biblioteca, 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(linhas)
                print(f'O livro {escolha} foi excluído com sucesso')
                # Atualizando o custo_total
                for index in range(len(livros['NOME'])):
                    if livros['NOME'][index] == escolha:
                        custo_total -= livros['CUSTO'][index]
                        break
                print(f'O custo acumulado de todos os livros é de R${custo_total}')
            except IndexError as erro1:
                print(erro1)

def atualizar():
    nome_antigo = input('Qual nome do livro você deseja alterar? ').upper()
    encontrado = False

    with open(biblioteca, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        if nome_antigo in linhas[i]:
            encontrado = True
            fav = input("Para modificar um valor de um livro existente digite: [MODIFICAR], Para adicionar ou remover um livro como favorito digite: [FAVORITO]\n").upper()
            if fav == "MODIFICAR":
                linha_split = linhas[i].split("; ")
                choose = input("O que você deseja alterar: Nome, Autor, Categoria ou Custo\n").upper()

                if choose == 'NOME':
                    alteracao = input("Novo nome do livro:").upper()
                    linha_split[0] = alteracao
                elif choose == 'AUTOR':
                    alteracao = input("Nome do novo autor:").upper()
                    linha_split[1] = alteracao
                elif choose == 'CATEGORIA':
                    alteracao = input("Nova categoria do livro:").upper()
                    linha_split[2] = alteracao
                elif choose == 'CUSTO':
                    alteracao = input("Novo valor do livro:").upper()
                    linha_split[3] = alteracao

                linhas[i] = "; ".join(linha_split) + '\n'

            elif fav == "FAVORITO":
                choose_fav = input("Para remover dos FAVORITOS digite: [DESFAVORITAR], Para adicionar digite: [FAVORITAR]\n").upper()
                if choose_fav == "DESFAVORITAR":
                    linhas[i] = linhas[i].replace('Favorito', '')
                    break
                elif 'Favorito' not in linhas[i]:
                        linhas[i] = linhas[i].rstrip('\n') + '; Favorito\n'
                        break
    if not encontrado:
        print("O livro inserido não foi encontrado na biblioteca")
    else:
        with open(biblioteca, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)

# FUNÇÕES COMPLEMENTARES
def exibir_livros(livros):
    try:
        print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")

        for index in range(len(livros['NOME'])):
            print(f"{livros['NOME'][index]}\t\t{livros['AUTOR'][index]}\t\t{livros['GENERO'][index]}\t\t{livros['CUSTO'][index]}\n")
    except FileNotFoundError as erro:
        print(erro)
    except IndexError as erro1:
        print(erro1)

# EXECUÇÃO PRINCIPAL
print("Olá Nathália!")

while True:
    direcionamento = input("O que você deseja fazer?\n[adicionar, visualizar, atualizar ou excluir]\n").upper()

    if direcionamento == 'ADICIONAR':
        adicionar_livro()
    elif direcionamento == 'VISUALIZAR':
        visualizar_livro()
    elif direcionamento == 'ATUALIZAR':
        atualizar()
    elif direcionamento == 'EXCLUIR':
        excluir_livros()