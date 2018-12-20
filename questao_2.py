class Fila:
    def __init__(self):
        
        self.objetos = []
        

    def EVazio(self):
        
        return len(self.objetos) == 0

    def peek(self):
        
        
        comprimento = len(self.objetos)
        
        return self.itens[0]
    

    def enqueue(self, objetos):
        
        self.objetos.append(objetos)
        

    def dequeue(self):
        
        if self.EVazio():
            
            return False
        
        return self.objetos.pop(0)
    

    def length(self):
        
        return len(self.objetos)

fila = Fila()
fila.enqueue("Maria")
print(fila.EVazio())
