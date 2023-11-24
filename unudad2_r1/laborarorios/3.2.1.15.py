''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 3.2.1.15
'''

class QueueError(IndexError):  
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        try:
            return self.__queue.pop(0)
        except IndexError:
            raise QueueError("Error de Cola")


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Error de Cola")
