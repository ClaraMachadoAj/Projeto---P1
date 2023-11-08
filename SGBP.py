import os
os.system('cls')

livros = {'Nome': [], 'Autor': [], 'Categoria': [], 'Custo': []}


def add():
   
livros{"Nome"}.append()

while True:

   print('Olá Nathália!')
   direcionamento = input('Que você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir').upper()


   if direcionamento == 'ADICIONAR':
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

   elif direcionamento == 'VISUALIZAR':
      vis(direcionamento)


   elif direcionamento == 'ATUALIZAR':
      att(direcionamento)

   elif direcionamento == 'EXCLUIR':
      ex(direcionamento)

   
   
