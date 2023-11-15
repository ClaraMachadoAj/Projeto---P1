import os
os.system('cls')

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
            custo = float(input("Quanto custou este livro?\n"))

            livros['Nome'].append(nome)
            livros['Autor'].append(autor)
            livros['Categoria'].append(categoria)
            livros['Custo'].append(custo)

            arquivo = open('biblioteca.txt', 'a')
            arquivo.write(f"Nome: {nome}, Autor: {autor}, Categoria: {categoria}, Custo: {custo}\n")
            arquivo.close()

            print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
            print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
            print(f"{nome}\t\t{autor}\t\t{categoria}\t\t{custo}\n")

            desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

            if desejo != 'S':
                print(livros)
                break