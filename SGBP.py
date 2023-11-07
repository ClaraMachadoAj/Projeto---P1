import os
os.system('cls')

arquivo_de_armazenamento = open('biblioteca.txt', '+r')



#Menu: 

print('Olá Nathália!')
direcionamento = input('Que você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir').capitalize()


def add(direcionamento):
   
   nome = input("Qual o nome do livro?\n").title()
   autor = input("Quem escreveu este livro?\n").title()
   categoria = input("Qual a categoria do livro?\n").title()
   custo = float(input("Quanto custou este livro?"))
   print("As informações do(s) livro(s) adicionado(s) são: \n")
   print("Nome     Autor     Categoria     Custo\n")
   print(f"{nome}\t\t\{autor}\t\t{categoria}\t\t{custo}")
   desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()




if direcionamento == 'Adicionar':
   return add(direcionamento)


elif direcionamento == 'Visualizar':
   return vis(direcionamento)


elif direcionamento == 'Atualizar':
   return att(direcionamento)

elif direcionamento == 'Excluir':
   return ex(direcionamento)

else:
   
   
