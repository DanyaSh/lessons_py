'''
https://smartiqa.ru/python-workbook/class#1

01_lesson_Soda.py
Задание:
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
'''

class Soda:
    
    def __init__(self, ingredient=None):
        if ingredient!='' and type(ingredient)==str:
            self.ingredient=ingredient
        else:
            self.ingredient=None

    def __str__(self):
        if self.ingredient==None:
            res='Обычная газировка'
        else:
            res='Газировка и '+self.ingredient
        return(res)
    
    def show_my_drink(self):
        print(self)

# Тест (3 примера)
print('_____test_____')
ingredient2='малина'
ingredient3=5
soda1=Soda()
soda2=Soda(ingredient2)
soda3=Soda(ingredient3)
soda1.show_my_drink()
soda2.show_my_drink()
soda3.show_my_drink()
print('_____end_test_____')

# Тест (Ваша газировка)
ingredient=input("Введите добавку и нажмите Enter...")
soda=Soda(ingredient)
soda.show_my_drink()