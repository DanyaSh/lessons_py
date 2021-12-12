'''
https://smartiqa.ru/python-workbook/class#1

02_lesson_Triangle.py
Задание:
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.

Построить треугольник из отрезков можно лишь в одном случае: сумма длин двух любых сторон всегда больше третьей.
'''

class TriangleChecker():
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a=side_a
        self.side_b=side_b
        self.side_c=side_c

    def is_triangle(self):
        try:
            self.side_a=float(self.side_a)
            self.side_b=float(self.side_b)
            self.side_c=float(self.side_c)
            if self.side_a==0 or self.side_b==0 or self.side_c==0:
                print('Нужно вводить только положительные числа!')
            elif self.side_a<0 or self.side_b<0 or self.side_c<0:
                print('С отрицательными числами ничего не выйдет!')
            elif self.side_a>self.side_b+self.side_c or self.side_b>self.side_a+self.side_c or self.side_c>self.side_b+self.side_a:
                print('Жаль, но из этого треугльник не сделать.')
            else:
                print('Ура, можно построить треугольник!')
        except ValueError:
            print('Нужно вводить только числа!')

#_______________test_____________________
print('_______________test_____________________')
triangle1 = TriangleChecker(2, 3, 4)
triangle1.is_triangle()
triangle2 = TriangleChecker(77, 3, 4)
triangle2.is_triangle()
triangle3 = TriangleChecker(77, 3, 'Сторона3')
triangle3.is_triangle()
triangle4 = TriangleChecker(77, -3, 4)
triangle4.is_triangle()
print('_______________end_test_____________________')
print('\n')
#_______________end_test_____________________

a=input('Введите длину стороны a, затем нажмите Enter...')
b=input('Введите длину стороны b, затем нажмите Enter...')
c=input('Введите длину стороны c, затем нажмите Enter...')

triangle=TriangleChecker(a, b, c)
triangle.is_triangle()