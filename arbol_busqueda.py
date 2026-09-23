class Nodo:
    """
    Esta clase representa un nodo (elto) que contiene un identificador y un diccionario de atributos.
    """
    def __init__ (self, identificador, atributos: dict):
        self.identificador = identificador
        self.atributos = atributos

    def __lt__ (self, otro): # Un nodo es menor que otro si su identificador es menor.
        return self.identificador < otro.identificador

    def __str__ (self):
        return f"Nodo {self.identificador}: {self.atributos}" 

class Arbol:
    def __init__(self, elto):
        self.elto = elto
        self.izdo = None
        self.dcho = None

    def Insert(self, elemento):
        if elemento == self.elto:
            return  # Si el elemento y la raíz coinciden, no tiene sentido seguir.

        # Aquí miramos si bajamos el elemento por la izquierda o por la derecha de la raíz.
        #
        # :: SI es MENOR que la raíz, por la IZQUIERDA
        if elemento < self.elto:
            if self.izdo is None: # Si no hay subárbol izquierdo, elemento es la raíz del nuevo subárbol izquierdo.
                self.izdo = Arbol(elemento)
            else:
                self.izdo.Insert(elemento) # Si ya hay llamamos a Insert con ese subárbol izquierdo.
        # :: SI es MAYOR, por la DERECHA. El resto es igual, pero con el subárbol derecho.
        else:
            if self.dcho is None: 
                self.dcho = Arbol(elemento)
            else:
                self.dcho.Insert(elemento)

    def Exists(self, elemento):
        # Metodo que comprueba si un elemento está en el arbol
        if elemento == self.elto:
            return True             # Si lo encuentro en la raíz, ya devuelvo TRUE

        if elemento < self.elto:
            if self.izdo is None:
                return False        # Si es menor que el nodo en el que estoy, y no hay subarbol
                                    # izqdo, es porque "elemento" no está, devuelvo FALSE
            else:
                self.izdo.Exists(elemento)  # Vuelvo a llamar buscando por el subarbol izqdo

        else:
            if self.dcho is None:
                return False        # Si es mayor que el nodo y no hay subarbol dcho, "elemento"
                                    # ya no está en el árbol, devuelvo FALSE
            else:
                self.dcho.Exists(elemento)  # Sigo buscando por el subarbol dcho

    def __str__(self):
        resultado = []
        nivel = [self]

        while nivel:
            siguiente = []
            linea = []

            for nodo in nivel:
                if nodo is None:
                    linea.append("X")
                    siguiente.append(None)
                    siguiente.append(None)
                else:
                    linea.append(str(nodo.elto))
                    siguiente.append(nodo.izdo)
                    siguiente.append(nodo.dcho)

            resultado.append(" ".join(linea))

            # Si todos son None, no seguimos creando niveles de X
            if all(nodo is None for nodo in siguiente):
                break

            nivel = siguiente

        return "\n".join(resultado)

    class NodeNotFoundError(Exception):
        """
        Esta excepción se dispara cuando ModifyAttr() no encuentra ningún nodo a partir 
        del identificador
        """
        def __init__(self, identificador, msg="Nodo no encontrado"):
            self.identificador = identificador
            self.msg = msg
            super().__init__(self.msg)

        def __str__(self):
            return f"{self.identificador} -> {self.msg}"
    
    def ModifyAttr(self, identificador, nombre_atributo, nuevo_valor):
        # :: Si el parámetro identificador y el de la raiz actual coinciden, modificamos su atributo.
        if self.elto.identificador == identificador:
            self.elto.atributos[nombre_atributo] = nuevo_valor
        # :: Si el identificador es menor que el de la raíz, bajamos por la izquierda.
        elif identificador < self.elto.identificador:
            if self.izdo is None:
                raise self.NodeNotFoundError(identificador) # Si no hay subárbol izquierdo, lanzamos la excepción.
            else:
                self.izdo.ModifyAttr(identificador, nombre_atributo, nuevo_valor) # Si hay, seguimos buscando.
        # :: Si el identificador es mayor que el de la raíz, bajamos por la derecha.
        else: # El resto es igual que el caso anterior, pero por la derecha.
            if self.dcho is None:
                raise self.NodeNotFoundError(identificador)
            else:
                self.dcho.ModifyAttr(identificador, nombre_atributo, nuevo_valor)

    def GetValue(self, identificador, nombre_atributo):
        # :: Si el parámetro identificador y el de la raiz actual coinciden, devolvemos su atributo.
        if self.elto.identificador == identificador:
            return self.elto.atributos.get(nombre_atributo)
        # :: Si el identificador es menor que el de la raíz, bajamos por la izquierda.
        elif identificador < self.elto.identificador:
            if self.izdo is None:
                raise self.NodeNotFoundError(identificador) # Si no hay subárbol izquierdo, lanzamos la excepción.
            else:
                return self.izdo.GetValue(identificador, nombre_atributo) # Si hay, seguimos buscando.
        # :: Si el identificador es mayor que el de la raíz, bajamos por la derecha.
        else: # El resto es igual que el caso anterior, pero por la derecha.
            if self.dcho is None:
                raise self.NodeNotFoundError(identificador)
            else:
                return self.dcho.GetValue(identificador, nombre_atributo)


# ==========================================
# Main para probar la clase
# ==========================================

arbol = Arbol(10)

arbol.izdo = Arbol(5)
arbol.dcho = Arbol(15)

arbol.izdo.izdo = Arbol(3)
arbol.izdo.dcho = Arbol(7)

arbol.dcho.dcho = Arbol(20)

print(arbol)