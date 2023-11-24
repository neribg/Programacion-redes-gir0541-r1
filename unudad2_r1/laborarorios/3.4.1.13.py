''' 
Alumno: Felipe Neri Francisco Bueno González
Fecha: 22 de novienbre de 2023
Descripcion: 3.4.1.13
'''

class WeekDayError(Exception):
    pass

class Weeker:
    days_of_week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.days_of_week:
            raise WeekDayError("Día de la semana no válido")
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        current_index = self.days_of_week.index(self.__current_day)
        new_index = (current_index + n) % 7
        self.__current_day = self.days_of_week[new_index]

    def subtract_days(self, n):
        current_index = self.days_of_week.index(self.__current_day)
        new_index = (current_index - n) % 7
        self.__current_day = self.days_of_week[new_index]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
