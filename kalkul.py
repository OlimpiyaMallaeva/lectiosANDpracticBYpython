# 02.10.2024
# 1 Реализовать функцию поиска фигуры с максимальной площадью
# 2 Реализовать функцию поиска фигуры с максимальным периметром
# 3 Реализовать пользовательский ввод даннных для фигур
# 4 Реализовать сравнение площадей и периметров фигур


# 0 прописать ключевые слова, чтобы человек мог ввести параметры фигуры
# 1 Воод пользвателем значений 1 фигуры
# 2 Воод пользвателем значений 2 фигуры
# 3 Воод пользвателем значений 3 фигуры
# 4 Воод пользвателем значений 4 фигуры
# 5 посчитать площадь каждой фигуры
# 6 определить максимальное значение площади среди 4 фигур
# 7 посчитать периметр каждой фигуры 
# 9 определить максимальное значение периметра среди 4 фигур
# 10 прописать ключевые слова, чтобы человек мог ввести параметры фигуры
# 11 сравнить периметр с периметроом а площадь с площадью
# 
# import math

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base * 3  # Для простоты, равносторонний треугольник

def input_shape(shape_number):
    while True:
        shape_type = input(f"Введите тип фигуры для фигуры {shape_number} (круг/прямоугольник/квадрат/треугольник): ").strip().lower()
        if shape_type == 'круг':
            radius = float(input("Введите радиус круга: "))
            return Circle(radius)
        elif shape_type == 'прямоугольник':
            width = float(input("Введите ширину прямоугольника: "))
            height = float(input("Введите высоту прямоугольника: "))
            return Rectangle(width, height)
        elif shape_type == 'квадрат':
            side = float(input("Введите длину стороны квадрата: "))
            return Square(side)
        elif shape_type == 'треугольник':
            base = float(input("Введите основание треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            return Triangle(base, height)
        else:
            print("Неизвестный тип фигуры. Попробуйте снова.")

def main():
    shapes = []
    
    for i in range(1, 5):
        shapes.append(input_shape(i))

    areas = [shape.area() for shape in shapes]
    perimeters = [shape.perimeter() for shape in shapes]

    max_area = max(areas)
    max_perimeter = max(perimeters)

    print(f"Максимальная площадь: {max_area:.2f}")
    print(f"Максимальный периметр: {max_perimeter:.2f}")

    for i in range(len(shapes)):
        print(f"Фигура {i+1}: площадь = {areas[i]:.2f}, периметр = {perimeters[i]:.2f}")

    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            if areas[i] > areas[j]:
                print(f"Фигура {i+1} больше по площади, чем фигура {j+1}")
            elif areas[i] < areas[j]:
                print(f"Фигура {j+1} больше по площади, чем фигура {i+1}")
            else:
                print(f"Фигура {i+1} и фигура {j+1} равны по площади")

            if perimeters[i] > perimeters[j]:
                print(f"Фигура {i+1} больше по периметру, чем фигура {j+1}")
            elif perimeters[i] < perimeters[j]:
                print(f"Фигура {j+1} больше по периметру, чем фигура {i+1}")
            else:
                print(f"Фигура {i+1} и фигура {j+1} равны по периметру")

if __name__ == "__main__":
    main()