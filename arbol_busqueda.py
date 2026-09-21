class arbol:
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
                self.izdo = arbol(elemento)
            else:
                self.izdo.Insert(elemento) # Si ya hay, llamamos a Insert con ese subárbol izquierdo.
        # :: SI es MAYOR, por la DERECHA. El resto es igual, pero con el subárbol derecho.
        else:
            if self.dcho is None: 
                self.dcho = arbol(elemento)
            else:
                self.dcho.Insert(elemento)