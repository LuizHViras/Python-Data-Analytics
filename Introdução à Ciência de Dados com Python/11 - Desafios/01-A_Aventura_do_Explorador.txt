# Desafio: A Aventura do Explorador

# Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta.

# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

# Programa:
quantidade_passos = int(input())

if quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")
elif quantidade_passos > 0:
  for numero_passo in range(1, quantidade_passos + 1):
    if numero_passo == 1:
      print("Explorador: 1 passo")
    else:
      print(f"Explorador: {numero_passo} passos")