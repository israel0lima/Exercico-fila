





class fila:
    def __init__(self):

        self.elemento = list()


    def enqueue ( self, chave):

        if (self.lenght()) <= 20:
            
            self.elemento.append(chave)

        else:
            len(chave)


    def dequeue(self):

        if(not(self.isEmpyr())):

            self.elemento.pop(0)


    def isEmpyt(self):

        return len(self.elemento) == 0


    def lenght(self):

        return len (self.elemento)

fila = fila()
for valor in range (21):
    fila.enqueue(valor)

    

        
