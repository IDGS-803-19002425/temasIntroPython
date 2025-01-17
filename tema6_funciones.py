import os

#16 archivos commit#

def suma():
    os.system("cls")
    print("Suma de numeros: ")
    print("Dame dos numeros: ")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es: ", num1 + num2)
    

def resta():
    os.system("cls")
    print("Resta de numeros: ")
    print("Dame dos numeros: ")    
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es: ", num1 - num2)

def multiplicar():
    os.system("cls")
    print("Multiplicacion de numeros: ")
    print("Dame dos numeros: ")    
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es: ", num1 * num2)

def dividir():
    os.system("cls")
    print("Division de numeros: ")
    print("Dame dos numeros: ")
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    print("El resultado es: ", num1 / num2)

def run():
    os.system("cls")        
    print("Menu principal:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Opcion: "))
    while opcion != 5:                
        if opcion == 1:            
            suma()            
            print("¿Desea regresar?")                               
            respuesta = input("S/N: ")
            if respuesta == "S":
                run()
            if respuesta == "N":
                exit()               
        if opcion == 2:            
            resta()            
            print("¿Desea regresar?")
            respuesta = input("S/N: ")
            if respuesta == "S":
                run()
            if respuesta == "N":
                exit()               
        if opcion == 3:            
            multiplicar()
            print("¿Desea regresar?")
            respuesta = input("S/N: ")
            if respuesta == "S":
                run()
            if respuesta == "N":
                exit()               
        if opcion == 4:            
            dividir()   
            print("¿Desea regresar?")
            respuesta = input("S/N: ")
            if respuesta == "S":
                run()
            if respuesta == "N":
                exit()                        
            
        if opcion == 5:            
            print("Saliendo...")
            exit()  

if __name__ == "__main__":
    os.system("cls")
    run()



