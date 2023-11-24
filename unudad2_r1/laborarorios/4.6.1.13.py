''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 4.6.1.13
'''

from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
    
        weeks = self.monthdays2calendar(year, 1)

        count = sum(day[weekday] != 0 for month_week in weeks for day in month_week)

        return count


my_calendar = MyCalendar()

# Prueba 1
result1 = my_calendar.count_weekday_in_year(year=2019, weekday=0)
print(result1)  # Debería imprimir 52

# Prueba 2
result2 = my_calendar.count_weekday_in_year(year=2000, weekday=6)
print(result2)  
