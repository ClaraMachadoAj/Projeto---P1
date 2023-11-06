import os
os.system('cls')



def add(pergunta):
     if pergunta == 'S':
        nome = input("Qual o nome do livro?\n").title()
        autor = input("Quem escreveu este livro?\n").title()
        categoria = input("Qual a categoria do livro?\n").title()
        custo = float(input("Quanto custou este livro?"))

        print("As informações do(s) livro(s) adicionado(s) são: \n")
        print("Nome     Autor     Categoria     Custo\n")
        print(f"{nome}\t\t\{autor}\t\t{categoria}\t\t{custo}")
        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()