''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 4.5.1.22
'''

from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53, 0)
print(dt.strftime("%Y/%m/%d %H:%M:%S"))  
print(dt.strftime("%y/%B/%d %I:%M:%S %p"))  
print(dt.strftime("%a, %Y %b %d"))  
print(dt.strftime("%A, %Y %B %d"))  
print("Día de la semana:", dt.strftime("%w"))  
print("Día del año:", dt.strftime("%j"))  
print("Número de semana en el año:", dt.strftime("%U"))