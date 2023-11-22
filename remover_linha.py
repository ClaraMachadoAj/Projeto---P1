def remove_linha(arquivo, linha):
  
  with open(arquivo, "r") as f:
    linhas = f.readlines()

  # Encontra a posição da linha que deseja excluir.
  pos = linhas.index(linha)

  # Remove a linha da lista.
  linhas.remove(linha)

  # Escreve as linhas restantes no arquivo.
  with open(arquivo, "w") as f:
    for linha in linhas:
      f.write(linha)
