import os
os.system ('cls')

def excluir_livros():
    escolha = input('Qual livro você deseja excluir? ').upper()
    arquivo = open('biblioteca.txt', 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    linhas_filtradas = [linha for linha in linhas if escolha in linha]
    if not linhas_filtradas:
        print('Esse livro não existe em sua biblioteca')
    else:
        for linha in linhas_filtradas:
            linhas.remove(linha)
        arquivo = open('biblioteca.txt', 'w', encoding='utf-8')
        arquivo.writelines(linhas)
        arquivo.close()
        print(f'O livro {escolha} foi excluído com sucesso')


excluir_livros()