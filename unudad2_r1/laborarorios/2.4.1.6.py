''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 2.4.1.6
'''
def display_seven_segment(number):
 
    patterns = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]   # 9
    ]


    digits = [int(digit) for digit in str(number)]

  
    for row in range(5):
        for digit in digits:
            print(patterns[digit][row], end="   ")
        print()  


display_seven_segment(123)
print()
display_seven_segment(9081726354)
