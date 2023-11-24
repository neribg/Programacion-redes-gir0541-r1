''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 4.3.1.15
'''
def contar_letras(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
            conteo_letras = {}
            
            for char in content:
                if char.isalpha() and char.isascii():
                    char = char.lower()
                    
                    conteo_letras[char] = conteo_letras.get(char, 0) + 1
            
            for letra, contador in sorted(conteo_letras.items()):
                print(f'{letra} -> {contador}')
    
    except FileNotFoundError:
        print(f'El archivo {file_name} no se encontró.')

archivo_input = input("Ingrese el nombre del archivo de entrada: ")

contar_letras(archivo_input)
