''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 4.3.1.16
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
            
            sorted_conteo = sorted(conteo_letras.items(), key=lambda x: x[1], reverse=True)
            
            for letra, contador in sorted_conteo:
                print(f'{letra} -> {contador}')
            output_file_name = file_name.split('.')[0] + '.hist'
            with open(output_file_name, 'w') as output_file:
                for letra, contador in sorted_conteo:
                    output_file.write(f'{letra} -> {contador}\n')
    
    except FileNotFoundError:
        print(f'El archivo {file_name} no se encontró.')

archivo_input = input("Ingrese el nombre del archivo de entrada: ")

contar_letras(archivo_input)
