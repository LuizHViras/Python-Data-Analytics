# Desafio: Estrutura de Dados: Organizando os seus Ativos

# Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.
# 1. A senha deve ter no mínimo 8 caracteres.
# 2. A senha deve conter pelo menos uma letra maiúscula (A-Z).
# 3. A senha deve conter pelo menos uma letra minúscula (a-z).
# 4. A senha deve conter pelo menos um número (0-9).
# 5. A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

# A entrada será uma única string representando a senha que precisa ser validada.

# Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

# Programa:
def verificar_forca_senha(senha):
  # Verificar se a senha tem pelo menos 8 caracteres
  if len(senha) < 8:
    return "Sua senha e muito curta. Recomenda-se no minimo 8 caracteres."

  # Verificar se a senha contém pelo menos uma letra maiúscula
  if not any(c.isupper() for c in senha):
      return "Sua senha nao atende aos requisitos de seguranca."

  # Verificar se a senha contém pelo menos uma letra minúscula
  if not any(c.islower() for c in senha):
      return "Sua senha nao atende aos requisitos de seguranca."

  # Verificar se a senha contém pelo menos um número
  if not any(c.isdigit() for c in senha):
      return "Sua senha nao atende aos requisitos de seguranca."

  # Verificar se a senha contém pelo menos um caractere especial
  if not any(c in "!@#$%^&*()" for c in senha):
      return "Sua senha nao atende aos requisitos de seguranca."

  # Se todas as condições forem atendidas, a senha é considerada forte
  return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
print(verificar_forca_senha(senha))