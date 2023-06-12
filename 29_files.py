# Open nos deja abrir un archivo
file = open('./text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)

file.close()

# ESTA ES LA MANERA MAS COMUN DE LEER ARCHIVOS YA QUE ABRE Y CIERRA EL ARCHIVO AUTOMATICAMENTE
with open('./text.txt') as file:
  for line in file:
    print(line)