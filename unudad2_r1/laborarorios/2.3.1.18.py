''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 2.3.1.18
'''
def mysplit(strng):
    words = []
    current_word = ""

    for char in strng:
        if char.isspace():  # Si el carácter es un espacio en blanco
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    return words

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
