# 26.09.2024
# Программа находит площадь, периметр трапеции 

longs1 = 5
longs2 = 20
longs3 = 5
longs4 = 20
h1 = 5

longs6 = 10
longs7 = 6
longs8 = 12
longs9 = 6
h2 = 5

def martishka1(side2, side4, side5):
    return side5 * (side4 + side2) * 0.5 

def martishka2(side1, side2, side3, side4): 
    return side1 + side2 + side3 + side4

def martishka3(side1, side2, side3, side4, side5):
    print(f"Площадь {martishka1(side2, side4, side5)} и периметр {martishka2(side1, side2, side3, side4)} трапеции")

martishka3(longs1, longs2, longs3, longs4, h1)
martishka3(longs6, longs7, longs8, longs9, h2)



