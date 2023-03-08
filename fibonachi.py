# iteradores

import time

class FiboIter:
   
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            if self.counter > 10:
                raise StopIteration
            return self.aux
        
        
""" swap "intercambio"linea22. primer valor antes del = toma el valor del primer valor luego del = 
y el segundo valor antes del = toma el valor del segundo valor luego del  =  
con esta accion se reemplaza la accion de las lineas 20 y 21 """    

"""instanciar al interador "clase"  instanciar es  acto de convertir apartir de los planos de una
  clse un objeto FiboIter un objeto
  se crea una variable para almacenar fibonacci"""

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(1)
        

