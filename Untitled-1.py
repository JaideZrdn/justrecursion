def take(n, xs):
    """
    função que retorna os primeiros n elementos da lista xs
    """
    return xs[0:n]

def drop(n, xs):
    """
    função que retorna uma lista sem os n primeiros elementos
    """
    return xs[n:]


def insord(k,xs):
    
    """
    Adiciona k à lista já ordenada xs por pesquisa binária
    """
    if len(xs)==1:
        if k<xs[0]: return [k]+xs
        else: return xs + [k]
    parametro=len(xs)//2
    menores = take(parametro,xs)
    maiores= drop(parametro,xs)
    pivot= maiores[0]
    if k==pivot:return menores + [k] + maiores
    elif k<pivot: return insord(k,menores) + maiores
    else: return menores + insord(k,maiores)
    
lista=[0,0,1,3,4,5,6,6,8,18,24,248,242]

print(insord(9, lista))

def ord(xs):
    """
    função para ordenar uma lista
    """
    if len(xs)==1: return xs
    else: return insord(xs[0], ord(xs[1:]))

list=[2,5,4,1,8,9,75,81,24,5,4,5,4,5,4]
print(ord(list))