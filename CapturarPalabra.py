from io import open
class CapturarPalabra:
    palabraEspañol = ""
    palabraIngles = ""

    def __init__(self, español, ingles):
        self.palabraEspañol = español
        self.palabraIngles = ingles


    def capturar(self):
        textoEspañol = self.palabraEspañol
        textoIngles = self.palabraIngles
        archivo = open("Diccionario.txt", "a")
        archivo.write( textoEspañol + ":" + textoIngles + "\n")         
        archivo.close()
        

        
                
    