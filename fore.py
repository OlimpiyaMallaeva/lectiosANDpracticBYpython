# 26.09.2024
# Программа находит площадь, периметр любого треугольника

longs1 = 4
longs2 = 2
longs3 = 3
h1 = 3

def martishka1(side1, h1):
    return 0.5 * side1 * h1

def martishka2(side1, side2, side3): 
    return side1 + side2 + side3

def martishka3(side1, side2, side3):
    print(f"Площадь любого треугольника: {martishka1(side1, h1)}, периметр любого треугольника: {martishka2(side1, side2, side3)}")

martishka1(longs1, h1)
martishka2(longs1, longs2, longs3)
martishka3(longs1, longs2, longs3)
