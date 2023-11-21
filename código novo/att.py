# def atualizar_nome():
#   nome_antigo = input('Qual o livro que você deseja substituir o nome? ')
#   novo_nome = input('Qual novo nome você quer designar a este livro? ')
  
#   arquivo = open(biblioteca, 'r+', encoding = 'utf-8')
  
#   dados_Arquivo = arquivo.read()
  
#   dados_Arquivo = dados_Arquivo.replace(nome_antigo, novo_nome)
  
#   arquivo.write(dados_Arquivo)
#   arquivo.close()

def atualizar_nome():
    nome_antigo = input('Qual o livro que você deseja substituir o nome? ')
    novo_nome = input('Qual novo nome você quer designar a este livro? ')
    arquivo = open("biblioteca.txt", 'r', encoding = 'utf-8')
    a = arquivo.readlines()

    if a in arquivo:
        b = a.split(";")


    arquivo.close()

atualizar_nome()