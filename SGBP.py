import os
os.system('cls')


while True:

   print('Olá Nathália!')
   direcionamento = input('Que você gostaria de realizar hoje? (adicionar, visualizar, atualizar ou excluir').capitalize()


   if direcionamento == 'Adicionar':
      return add(direcionamento)


   elif direcionamento == 'Visualizar':
      return vis(direcionamento)


   elif direcionamento == 'Atualizar':
      return att(direcionamento)

   elif direcionamento == 'Excluir':
      return ex(direcionamento)

   
   
