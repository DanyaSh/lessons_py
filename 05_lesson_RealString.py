'''
https://smartiqa.ru/python-workbook/class#1

05_lesson_RealString.py
Задание:
Строки в Питоне сравниваются на основании значений символов. 
Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим. 
А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки), а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить). 
Такое положение дел не устроило Анну. 
Она считает, что строки нужно сравнивать по количеству входящих в них символов.
Для этого девушка создала класс RealString и реализовала озвученный инструментарий. Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString. 
К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.

В общем случае для создания такого класса понадобится 4 метода, так как в Питоне реализованы «богатые» сравнения. 
Это значит, что если имеется сравнение «больше», то автоматом появится возможность осуществлять сравнение «меньше». 

__________________________________________________________________________
Решение с тремя методами использует библиотеку functools @total_ordering


from functools import total_ordering
 
@total_ordering
class RealString:
	def __init__(self, some_str):
    	self.some_str = str(some_str)
 
	def __eq__(self, other):
    	if not isinstance(other, RealString):
        	other = RealString(other)
    	return len(self.some_str) == len(other.some_str)
 
	def __lt__(self, other):
    	if not isinstance(other, RealString):
        	other = RealString(other)
    	return len(self.some_str) < len(other.some_str)


Тут же все реализованно буквально, задействовав все магические методы
'''

class RealString:

    def __init__(self, string):
        self.string=str(string)
    
    def __lt__(self, other):
        return(len(self.string)<len(str(other)))
    
    def __le__(self, other):
        return(len(self.string)<=len(str(other)))
        
    def __gt__(self, other):
        return(len(self.string)>len(str(other)))
        
    def __ge__(self, other):
        return(len(self.string)>=len(str(other)))
        
    def __eq__(self, other):
        return(len(self.string)==len(str(other)))

# Тесты
str1 = RealString('Молоко')
str2 = RealString('Абрикосы растут')
str3 = 'Золото'
str4 = [1, 2, 3]
print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)