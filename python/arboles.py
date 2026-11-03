

class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def espejo(raiz: Nodo):
        raiz.izq, raiz.der = raiz.der, raiz.izq
        if (raiz.izq is not None):
            espejo(raiz.izq)
        if (raiz.der is not None):
            espejo(raiz.der)
        



def son_espejo(a, b):
    raise NotImplementedError("TODO son_espejo")


def es_simetrico(raiz):
    raise NotImplementedError("TODO es_simetrico")


def inorden(raiz):
    salida = []
    def visitar(nodo):
        if nodo is not None:
            visitar(nodo.izq)
            salida.append(nodo.valor)
            visitar(nodo.der)
    visitar(raiz)
    return salida
