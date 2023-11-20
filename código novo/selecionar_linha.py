def selecionar_linha(arquivo, escolha):
  
  for linha in arquivo:
        if escolha in linha:
          
          print(linha.strip())