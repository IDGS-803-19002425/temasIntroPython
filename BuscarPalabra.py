class BuscarPalabra:
    palabraBuscar = ""
    
    
    def __init__(self, palabra, ):
        self.palabraBuscar = palabra

    def buscar(self):        
        listaPalabras = []
        palabraBuscar = self.palabraBuscar.lower().strip()
        archivo = open("Diccionario.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        for linea in lineas:
            palabras =  linea.strip().split(":")
            if len(palabras) == 2:
                palabraEspanol = palabras[0].strip().lower()
                palabraIngles = palabras[1].strip().lower()
            if palabraBuscar == palabraEspanol:
                listaPalabras.append(palabraIngles)
                print("Palabra encontrada:", palabraIngles)
                
            if palabraBuscar == palabraIngles:
                listaPalabras.append(palabraEspanol)
                print("Palabra encontrada:", palabraEspanol)
                 
    print("Palabra no encontrada")
                
            
            
                

                        
        
        
       

            
        
        
       
        