from CapturarPalabra import CapturarPalabra
from BuscarPalabra import BuscarPalabra
import os
  
def main():
    os.system("cls")
    while True:                
        print("Elige una opcion:" )        
        print("Bienvendo a el diccionario ")
        print("Opcion 1: Capturar palabra")
        print("Opcion 2: Buscar palabra")
        print("Opcion 3: Salir")   
        opcion = int(input())              
        if opcion == 1:
                palabraCapturadaEspanol = input("Captura la palabra en español: ")
                palabraCapturadaIngles = input("Captura la palabra en ingles: ")
                obj = CapturarPalabra(palabraCapturadaEspanol, palabraCapturadaIngles)
                obj.capturar()
        if opcion == 2:     
                    print("¿En que idioma vas a buscar?")
                    print("Opcion 1: Español")
                    print("Opcion 2: Ingles")
                    idioma = int(input())        
                    if idioma == 1:
                        palabraBuscar = input("Ingrese la palabra a buscar: ")
                        obj = BuscarPalabra(palabraBuscar)
                        obj.buscar()
                    if idioma == 2:
                        palabraBuscar = input("Ingrese la palabra a buscar: ")
                        obj = BuscarPalabra(palabraBuscar)
                        obj.buscar()                                               
        if opcion == 3:
                exit()


if __name__ == "__main__":
    main()



    