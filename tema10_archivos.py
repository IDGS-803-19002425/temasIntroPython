
from io import open
texto = "una linea de texto con a"
archivo = open("archivo.txt", "a")
archivo.write(texto)
archivo.write(texto)
archivo.close()

