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
        return identificador in self.diccionario

    def GetValue(self, nombre_atributo, identificador):
        """
        Si ambos nombre_atributo e identificador existen, devuelve un valor; si no, None.
        """
        if self.Exists(identificador):
            return self.diccionario[identificador].get(nombre_atributo)
        return None
