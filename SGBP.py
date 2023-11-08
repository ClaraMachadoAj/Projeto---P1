import os
os.system('cls')

livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}




while True:

   print('Olá Nathália!')
   direcionamento = input('Que você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir').upper()


   if direcionamento == 'ADICIONAR':
      livros['Nome'].append(nome = input("Qual o nome do livro?\n").title())
      livros['Autor'].append(autor = input("Quem escreveu este livro?\n").title())
      livros['Categoria'].append(categoria = input("Qual a categoria do livro?\n").title())
      livros['Custo'].append(custo = float(input("Quanto custou este livro?\n")))

      

      print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
      print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
      print(f"{nome}\t\t{autor}\t\t{categoria}\t\t{custo}\n")
      desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

      if desejo == 'S':
         continue
      else:
         break

   elif direcionamento == 'VISUALIZAR':
      vis(direcionamento)


   elif direcionamento == 'ATUALIZAR':
      att(direcionamento)

   elif direcionamento == 'EXCLUIR':
      ex(direcionamento)

   
   
