''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 4.4.1.8
'''

import os

def find(path, dir):
    
    path = os.path.abspath(path)

    for root, dirs, files in os.walk(path):
        if dir in dirs:
            print(os.path.join(root, dir))

        for subdir in dirs:
            find(os.path.join(root, subdir), dir)

find("./tree", "python")
