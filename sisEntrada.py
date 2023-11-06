import os
os.system('cls')

while True:
    per=input("Deseja cadastrar um livro? [S] sim e [N] não. ").upper()

    nome=input("Qual o nome do livro?\n").title()
    autor=input("Quem escreveu este livro?\n").title()
    cat=input("Qual a categoria do livro?\n").title()
    custo=float(input("Quanto custou este livro?"))

    print("As informações do(s) livro(s) adicionado(s) são: \n")
    print("Nome     Autor     Categoria     Custo\n")
    print(f"{nome}\t\t\{autor}\t\t{cat}\t\t{custo}")

    if per=='N':
        break