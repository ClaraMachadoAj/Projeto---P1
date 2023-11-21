import os
os.system ('cls')

def atualizar_nome():
    nome_antigo = input('Qual o livro que você deseja substituir o nome? ').upper()
    novo_nome = input('Qual novo nome você quer designar a este livro? ').upper()

    with open(biblioteca, 'r+', encoding='utf-8') as arquivo:
        dados_Arquivo = arquivo.read()
        dados_Atualizados = dados_Arquivo.replace(nome_antigo, novo_nome)

        arquivo.seek(0)
        arquivo.write(dados_Atualizados)
        arquivo.truncate()

biblioteca = 'biblioteca.txt'
atualizar_nome(biblioteca)