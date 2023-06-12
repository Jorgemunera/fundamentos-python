# la w+ hace referencia a permisos de lectura y escritura pero sobreescribiendo todo el archivo
# r+ nos permite leer y escribir, pero la escritura es agregar mas al archivo como tal

with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')