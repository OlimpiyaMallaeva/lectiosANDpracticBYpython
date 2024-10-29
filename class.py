# 16.10.2024
# Классы

class Shape:
    def print_data(self):
        pass
    def calculate_area(self):
        pass
    def calculate_pirimetr(self):
        pass

# Класс для круга _____________________________________________________________

PI = 3.14

class Cricle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return PI * self.radius * self.radius
    def calculate_pirimetr(self):
        return PI * self.radius
    def print_data(self):
        print(f"Радиус круга: {self.radius} у.е. кв.")
        print(f"Формула площади круга S = PI * r^2")
        print(f"Площадь круга: {self.calculate_area()} у.е. кв.")

#cricle = Cricle(52)
#cricle.print_data()


# Класс для квадрата __________________________________________________________

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def calculate_area(self):
       return self.side ** 2
    def calculate_pirimetr(self):
        return 4 * self.side
    def print_data(self):
        print(f"Длина стороны, по совместительству и высоты квадрата: {self.side} у.е. кв.")
        print(f"Формула площади квадрата: S = side^2")
        print(f"Площадь квадрата: {self.calculate_area()} у.е. кв.")
        print(f"Формула периметра квадрата: P = side * 4")
        print(f"Периметр квадрата: {self.calculate_pirimetr()} у.е. кв.")

#square = Square(5)
#square.print_data()


# Класс для треугольника ______________________________________________________

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def calculate_area(self):
        return (self.base * self.height) / 2
    def calculate_pirimetr(self):
     return self.base * 3
    def print_data(self):
        print(f"Длина основания треугольника: {self.base} у.е. кв.")
        print(f"Высота треугольника: {self.height} у.е. кв.")
        print(f"Формула площади треугольника: S = (base * height) / 2")
        print(f"Площадь треугольника: {self.calculate_area()} у.е. кв.")
        print(f"Формула периметра треугольника: P = side * 3")
        print(f"Периметр треугольника: {self.calculate_pirimetr()} у.е. кв.")

#triangle = Triangle(5, 4)
#triangle.print_data()


# Класс для трапеции __________________________________________________________

class Trapezoid(Shape):
    def __init__(self, side1, side2, side3, side4, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.height = height
    def calculate_area(self): 
        return self.height * (self.side2 + self.side4) / 2
    def calculate_pirimetr(self):
        return self.side2 + self.side4 + self.side1 + self.side3
    def print_data(self):
        print(f"Длинна первого основания трапеции: {self.side2} у.е. кв.")
        print(f"Длинна второго основания трапеции: {self.side4} у.е. кв.")
        print(f"Длинна первой боковой стороны трапеции: {self.side1} у.е. кв.")
        print(f"Длинна второй боковой стороны трапеции: {self.side3} у.е. кв.")
        print(f"Высота трапеции: {self.height} у.е. кв.")
        print(f"Формула площади трапеции: S = ((osnovanie_1 + osnovanie_2) * height) / 2")
        print(f"Площадь трапеции: {self.calculate_area()} у.е. кв.")
        print(f"Формула периметра трапеции: P = side2 + side4 + side3 + side5")
        print(f"Периметр трапеции: {self.calculate_pirimetr()} у.е. кв.")

#trapezoid = Trapezoid(5, 20, 5, 10, 5)
#trapezoid.print_data()