﻿''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 3.2.1.14
'''

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        val = super().pop()  # Llama al método pop de la clase base
        self.__counter += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

