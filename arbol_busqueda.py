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