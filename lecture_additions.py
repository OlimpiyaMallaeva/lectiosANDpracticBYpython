#26.09.2024
# Дополнение к лекции

PI = 3.1415

radius1 = 3
radius2 = 3.983457
radius3 = 8
radius4 = 9.9871289736
radius5 = 99878

def print_area_circle(radius): 
    print(f"Радиус круга : {radius}") 
    print("Формула площади круга S = pi * r*2") 
    print(f"Площадь круга : {calculate_area_circle(radius)} Ve кв.")

def calculate_area_circle(radius): return PI * radius * radius

print_area_circle(radius1) 
print_area_circle(radius2) 
print_area_circle(radius3) 
print_area_circle(radius4) 
print_area_circle(radius5)

# 02.10.2024
# 1 Реализовать функцию поиска фигуры с максимальной площадью
# 2 Реализовать функцию поиска фигуры с максимальным периметром
# 3 Реализовать пользовательский ввод даннных для фигур
# 4 Реализовать сравнение площадей и периметров фигур


