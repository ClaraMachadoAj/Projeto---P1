import os
os.system ('cls')

def atualizar_nome():
    nome_antigo = input('Qual o livro que você deseja substituir o nome? ').upper()
    novo_nome = input('Qual novo nome você quer designar a este livro? ').upper()

    # Caminho do arquivo
    biblioteca = 'biblioteca.txt'

    with open(biblioteca, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    # Imprime as linhas do arquivo para inspeção
    print("Conteúdo atual do arquivo:")
    for linha in linhas:
        print(linha.strip())  # Remove espaços em branco e quebras de linha

    # Verifica se o nome antigo está presente e atualiza apenas o campo de nome
    livro_encontrado = False
    for indice, linha in enumerate(linhas):
        if f"Nome: {nome_antigo};" in linha:
            linhas[indice] = linhas[indice].replace(f"Nome: {nome_antigo};", f"Nome: {novo_nome};")
            livro_encontrado = True

    # Se o livro foi encontrado, reescreve o arquivo com os dados atualizados
    if livro_encontrado:
        with open(biblioteca, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        print(f'O livro "{nome_antigo}" foi atualizado para "{novo_nome}" no arquivo.')
    else:
        print(f'O livro "{nome_antigo}" não foi encontrado no arquivo.')

# Chamada da função para atualizar o nome
atualizar_nome()


