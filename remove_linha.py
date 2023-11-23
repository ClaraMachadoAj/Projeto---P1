def remove_linha(arquivo, linha, escolha):
  """Remove a linha especificada do arquivo.

  Args:
    arquivo: O caminho do arquivo.
    linha: A linha que deseja excluir.

  Returns:
    None.
  """

  with open(arquivo, "r") as f:
    linhas = f.readlines()

  # Encontra a posição da linha que deseja excluir.
  pos = linhas.index(linha)

  # Remove a linha da lista.
  linhas.remove(linha)

  # Escreve as linhas restantes no arquivo.
  with open(arquivo, "w") as f:
    linha_split = linha.split("; ")
    linha_split.replace(0, escolha)
    linha.append(linha_split)
    for linha in linhas:
      f.write("; ".join(linha))



def insere_linha(arquivo, linha):
  """Insere uma nova linha no final do arquivo.

  Args:
    arquivo: O caminho do arquivo.
    linha: A linha que deseja inserir.

  Returns:
    None.
  """

  with open(arquivo, "a") as f:
    f.write(linha)


if __name__ == "__main__":
  arquivo = "meu_arquivo.txt"
  linha = "Esta é uma nova linha."

  insere_linha(arquivo, linha)
