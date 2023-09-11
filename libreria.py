## Programa escrito en python orientado a la deteccion y conteo de palabras, signos y espacios en textos ingresados por el usuario

import string

def count_words(text):
  """
  Cuenta el número de palabras en un texto.

  Args:
    text: La cadena de caracteres a contar.

  Returns:
    El número de palabras en el texto.
  """

  words = text.split()
  return len(words)

def count_signs(text):
  """
  Cuenta el número de signos en un texto.

  Args:
    text: La cadena de caracteres a contar.

  Returns:
    El número de signos en el texto.
  """

  signs = set(string.punctuation)
  count = 0
  for character in text:
    if character in signs:
      count += 1
  return count

def count_spaces(text):
  """
  Cuenta el número de espacios en un texto.

  Args:
    text: La cadena de caracteres a contar.

  Returns:
    El número de espacios en el texto.
  """

  return text.count(' ')

def main():
  """
  Solicita al usuario un texto y muestra el número de palabras, signos y espacios.
  """

  text = input("Ingrese un texto: ")
  words = count_words(text)
  signs = count_signs(text)
  spaces = count_spaces(text)
  print("El texto tiene {} palabras, {} signos y {} espacios.".format(
      words, signs, spaces))


if __name__ == "__main__":
  main()