# 25.09.2024
# программа считает площадь круга

# даны радиусы:
# 3
# 3.983457
# 8
# 9.9871289736
# 99878

PI = 3.1415

radius1 = 3
radius2 = 3.983457
radius3 = 8
radius4 = 9.9871289736
radius5 = 99878

print(f"Радиус круга: {radius1}")
print("Формула площади круга s = PI * r^2")
area1 = PI * radius1 * radius1
print(f"Площадь круга: {area1} у.е. кв.")

print(f"Радиус круга: {radius2}")
print("Формула площади круга s = PI * r^2")
area2 = PI * radius2 * radius2
print(f"Площадь круга: {area2} у.е. кв.")

print(f"Радиус круга: {radius3}")
print("Формула площади круга s = PI * r^2")
area3 = PI * radius3 * radius3
print(f"Площадь круга: {area3} у.е. кв.")

print(f"Радиус круга: {radius4}")
print("Формула площади круга s = PI * r^2")
area4 = PI * radius4 * radius4
print(f"Площадь круга: {area4} у.е. кв.")

print(f"Радиус круга: {radius5}")
print("Формула площади круга s = PI * r^2")
area5 = PI * radius5 * radius5
print(f"Площадь круга: {area5} у.е. кв.")

# 26.09.2024
# Программа считает площадь прямоугольного треугольника
# Программа считает площадь, периметр квадрата
# Программа находит площадь, периметр трапеции 
# Программа находит площадь, периметр любого треугольника

# 02.10.2024
# 1 Реализовать функцию поиска фигуры с максимальной площадью
# 2 Реализовать функцию поиска фигуры с максимальным периметром
# 3 Реализовать пользовательский ввод даннных для фигур
# 4 Реализовать сравнение площадей и периметров фигур


# 16.10.2024
# Классы
class Shape:
    def print_data(self):
        pass
    def calculate_area(self):
        pass
    def calculate_pirimetr(self):
        pass

class Cricle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return PI * self.radius * self.radius
    def calculate_pirimetr(self):
        return PI * self.radius
    def print_data(self):
        print(f"Радиус круга: {self.radius}")
        print(f"Формула площади круга S = PI * r^2")
        print(f"Площадь круга: {self.calculate_area()} у.е. кв.")

cricle = Cricle(52)
cricle.print_data()

# 
# 
# 