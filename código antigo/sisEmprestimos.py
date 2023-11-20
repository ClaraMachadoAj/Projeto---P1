import os
os.system ('cls')

#def emprestimo(dados):

while True:
        pergunta = input("Deseja fazer um empréstimo de algum livro? [S] sim e [N] não. ").upper()

        if pergunta == 'S':
            nome = input("Qual livro você quer emprestar?\n").title()
            autor = input("Quem escreveu este livro?\n").title()
            emprestimo = input('Para quem você vai emprestar?\n').title()
            prazo = input("Por quanto tempo?\n").title()
            

            print("As informações do(s) livro(s) adicionado(s) são: \n")
            print("Nome\t\tAutor\t\tPessoa\t\tPrazo\n")
            print(f"{nome}\t\t{autor}\t\t{emprestimo}\t\t{prazo}\n")

            desejo = input('Deseja emprestar mais algum? [S] sim e [N] não. ').upper()


            if desejo == 'S':
                continue
            else: 
                break
        
        else:
            break

#return (dados)