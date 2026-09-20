class TablaSimbolos:
    def __init__(self):
        self.diccionario = {}

    def InsertSymbol(self, identificador, valor, tipo, dir_mem):
        self.diccionario[identificador] = {"valor": valor, "tipo": tipo, "direccion_memoria": dir_mem}

    def ModifySymbol(self, identificador, nuevo_valor, nuevo_tipo, nueva_dir_mem):
        if nuevo_valor is not None:
            self.diccionario[identificador]["valor"] = nuevo_valor

        if nuevo_tipo is not None:
            self.diccionario[identificador]["tipo"] = nuevo_tipo

        if nueva_dir_mem is not None:
            self.diccionario[identificador]["direccion_memoria"] = nueva_dir_mem

    def Exists(self, identificador):
        if identificador in self.diccionario:
            return True
        else:
            return False

    def GetValue():