class Flujo:
    def __init__(self, nombre_fichero):
        self.fichero = open(nombre_fichero, "r").read()
        self.num_linea = 1
        self.num_columna = 1
        self.puntero_caracter = 0

    def NewChar(self):
        caracter = self.fichero[self.puntero_caracter]

        self.num_columna += 1

        if caracter == "\n":
            self.num_linea += 1         # Como salto de linea, aumento el contador
            self.num_columna = 1        # En salto de fila, reseteamos el número de columna

        self.puntero_caracter += 1
        return caracter

    def ReturnChar(self):
        # Restamos 1 al puntero
        self.puntero_caracter = self.puntero_caracter - 1

    def GetNumLine(self):
        return self.num_linea
    
    def GetCharInLine(self):
        return self.num_columna

    def Probar(self):
        for caracter in self.fichero:
            print(self.NewChar())
        print(f"Ha terminado en la linea: {self.GetNumLine()}, y columna: {self.GetCharInLine()}")


flujo = Flujo("fichero_prueba.txt")
flujo.Probar()
