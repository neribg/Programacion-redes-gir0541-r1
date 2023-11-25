''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 23 de novienbre de 2023
Descripcion: 2.8.1.4
'''
def read_int(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: el valor no está dentro del rango permitido ({min_value}..{max_value})")
        except ValueError:
            print("Error: entrada incorrecta")

v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)
print("El número es:", v)

