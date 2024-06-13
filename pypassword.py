import random
import string

def main():
  print("Bem vindo ao pypassword! Seu gerador de senhas com python.")
  print("Escolha o tamanho da senha que deseja gerar: ")
  size = int(input())
  if size < 6:
    print("Senhas com menos de 6 caracteres são consideradas fracas.")
    print("Você deseja continuar? (S/n)")
    response = input()
    if response == "n":
      return
  print("Você deseja adicionar caracteres especiais? (S/n)")
  special = input() or "S"
  print("Você deseja adicionar números? (S/n)")
  numbers = input() or "S"
  print("Você deseja adicionar letras maiúsculas? (S/n)")
  uppercase = input() or "S"
  print("Você deseja adicionar letras minúsculas? (S/n)")
  lowercase = input() or "S"
  if not any(option.lower() == "s" for option in [special, numbers, uppercase, lowercase]):
    print("Você precisa escolher pelo menos uma opção!")
    return
  characters = ""
  password_chars = []
  if special:
    characters += string.punctuation
    password_chars.append(random.choice(string.punctuation))
  if numbers:
    characters += string.digits
    password_chars.append(random.choice(string.digits))
  if uppercase:
    characters += string.ascii_uppercase
    password_chars.append(random.choice(string.ascii_uppercase))
  if lowercase:
    characters += string.ascii_lowercase
    password_chars.append(random.choice(string.ascii_lowercase))

  while len(password_chars) < size:
    password_chars.append(random.choice(characters))

  random.shuffle(password_chars)
  password = "".join(password_chars)

  print(f"A senha gerada foi: {password}")

if __name__ == "__main__":
  main()