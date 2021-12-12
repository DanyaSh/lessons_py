'''
https://smartiqa.ru/python-workbook/class#1

03_lesson_Kg.py
Задание:
Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, 
а с помощью метода to_pounds() они переводятся в фунты. 
Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания нового значения килограммов, 
get_kg()  - для вывода текущего значения кг. Из-за этого возникло неудобство: 
нам нужно теперь использовать эти 2 метода для задания и вывода значений. 
Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')
    
    def get_kg(self):
        return self.__kg

Чтобы не задавать новые значения или не получать к ним доступ через два метода, можно реализовать предложенный класс через функцию property() или свойства-декораторы. 

'''

class obj:

    def __init__(self, name, kg, val):
        try:
            self.__name = str(name)
            self.__kg = float(kg)
            self.__val = float(val)
        except ValueError:
            print('InputError')

    def __str__(self):
        return('объект_'+str(self.__name)+':\n'+str(self.__kg)+'_kg\n'+str(self.__val)+'_cm³')

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Масса задается только числом')

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, new_val):
        if isinstance(new_val, (int, float)):
            self.__kg = new_val
        else:
            raise ValueError('Объем задается только числом')
    
    def to_mm(self):
        return self.__val*1000
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, (str)):
            self.__name = new_name
        else:
            raise ValueError('Имя задается только строкой')
    
a=obj('что-нибудь', 5, 3)
print(a)
print(a.to_pounds(), '_pounds')
print(a.to_mm(), '_mm³')
a.name='кто-нибудь'
a.kg=55
a.val=13
print('_______после взмаха волшебной палочки_______')
print(a)