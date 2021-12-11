'''
https://smartiqa.ru/python-workbook/class#1

01_lesson_Soda.py
Задание:
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
'''

class Soda:
    
    def __init__(self, additive=None):
        if additive!='' and type(additive)==str:
            self.additive=additive
        else:
            self.additive=None

    def __str__(self):
        if self.additive==None:
            res='Обычная газировка'
        else:
            res='Газировка и '+self.additive
        return(res)
    
    def show_my_drink(self):
        print(self)

# Тест (3 примера)
print('_____test_____')
additive2='малина'
additive3=5
soda1=Soda()
soda2=Soda(additive2)
soda3=Soda(additive3)
soda1.show_my_drink()
soda2.show_my_drink()
soda3.show_my_drink()
print('_____end_test_____')

# Тест (Ваша газировка)
additive=input("Введите добавку и нажмите Enter...")
soda=Soda(additive)
soda.show_my_drink()