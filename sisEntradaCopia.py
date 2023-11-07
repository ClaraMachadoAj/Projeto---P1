import os
os.system('cls')

livros = []

pergunta = input("Deseja cadastrar um livro? [S] sim e [N] não. ").upper()

while True:
    if pergunta == 'S':
        nome = input("Qual o nome do livro?\n").title()
        autor = input("Quem escreveu este livro?\n").title()
        categoria = input("Qual a categoria do livro?\n").title()
        custo = float(input("Quanto custou este livro?\n"))

        livro = {
            'Nome': nome,
            'Autor': autor,
            'Categoria': categoria,
            'Custo': custo
        }

        livros.append(livro)

        print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
        print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
        print(f"{nome}\t\t{autor}\t\t{categoria}\t\t{custo}\n")
        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

        if desejo == 'S':
            continue
        else:
            break

    else:
        break

print("\n\t\tLista de livros cadastrados:\n")
print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")

for livro in livros:
    print(f"{livro['Nome']}\t\t{livro['Autor']}\t\t{livro['Categoria']}\t\t{livro['Custo']}\n")