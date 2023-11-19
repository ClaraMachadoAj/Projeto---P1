import os
os.system('cls')

custo_total = 0.0

while True:
    pergunta = input("Deseja cadastrar um livro? [S] sim e [N] não. ").upper()

    if pergunta != 'S' and pergunta != 'N':
        print("Erro! Responda apenas com 'S' para sim ou 'N' para não. ")
        continue

    elif pergunta == 'S':
        nome = input("Qual o nome do livro?\n").title()
        autor = input("Quem escreveu este livro?\n").title()
        categoria = input("Qual a categoria do livro?\n").title()
        custo = float(input("Quanto custou este livro?\n"))

        custo_total += custo

        print("As informações do(s) livro(s) adicionado(s) são: \n")
        print("Nome     Autor     Categoria     Custo\n")
        print(f"{nome}\t\t\{autor}\t\t{categoria}\t\t{custo}\n")
        desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

        

        if desejo == 'S':
            continue
        else: 
            break
    
    else:
        break

print(f"\nCusto total de todos os livros: R${custo_total}") 