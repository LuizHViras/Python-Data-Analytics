# Desafio: O Robô inteligente

# Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

# O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente.

# Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

# Programa:
def classificar_numero(numero):
  global positivos, negativos
  if numero > 0:
    positivos += 1
    return "positivo!"
  
  else:
    negativos += 1
    return "negativo!"
    
positivos = 0
negativos = 0   
numero = int(input())

while numero != 0:
  print(classificar_numero(numero))
  numero = int(input())

print(f"{positivos} números positivos, {negativos} números negativos")