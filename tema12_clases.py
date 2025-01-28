
class Operasbas:
    #Declaracion de atributos o propuedades
    num1 = 0
    num2 = 0
    resultado = 0
    #Declaracion de constructor de la clase
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b


    #Declaracion de los metodos de la clase
    def suma(self):
        self.resultado = self.num1 + self.num2
        print("La suma es {}".format(self.resultado))

#declarion de la funcion main para ejecutar el codigo
def main():
    obj = Operasbas(3,5)
    obj.suma()

if __name__ == "__main__":
    main()




