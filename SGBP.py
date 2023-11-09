import os
os.system('cls')




livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}

print('Olá Nathália!')


while True:

   direcionamento = input('O quê você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir)\n ').upper()


   if direcionamento == 'ADICIONAR':
      while True:

         livros['Nome'] = nome = input("Qual o nome do livro?\n").title()
      
      #Fazer um verificador pra ver se o livro já existe no arquivo, p n add o mesmo livro duas vezes!!

         livros['Autor'] = autor = input("Quem escreveu este livro?\n").title()
         livros['Categoria'] = categoria = input("Qual a categoria do livro?\n").title()
         livros['Custo'] = custo = float(input("Quanto custou este livro?\n"))

      

         print("\t\tAs informações do(s) livro(s) adicionado(s) são: \n")
         print("Nome\t\t\tAutor\t\t\tCategoria\t\tCusto\n")
         print(f"{livros['Nome']}\t\t{livros['Autor']}\t\t{livros['Categoria']}\t\t{livros['Custo']}\n")
         desejo = input('Você deseja continuar adicionando? [S] sim e [N] não. ').upper()

         if desejo == 'S':
            continue
         else:
            print(livros)
            break

   elif direcionamento == 'VISUALIZAR':
      vis(direcionamento)


   elif direcionamento == 'ATUALIZAR':
      att(_)

   elif direcionamento == 'EXCLUIR':
      ex(direcionamento)

#ef calculadora(custo):

   
