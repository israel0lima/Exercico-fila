def lista(fila):
    
    for avioesAguardando in fila:
        print(i)

def AdicionarAvião(fila,v):

    fila.append(v)
    return fila

def DecolaAviao(fila):
    
    if(len(fila)==0):
        return fila

    fila.pop(0)
    return fila

def QuantidadeAvioes(fila):
    return len(fila)
