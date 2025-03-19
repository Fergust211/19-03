import math

while True:
    # Запрос типа фигуры
    type = input("Введите тип фигуры (К – Круг, Т – Треугольник, П – Прямоугольник): ")

    if type == 'К':
        # Вычисление площади круга
        radius = float(input("Введите радиус круга: "))
        area = 3.14 * radius ** 2
        print(f"Площадь круга: {area:}")

    elif type == 'Т':
        a = float(input("Введите длину стороны A: "))
        b = float(input("Введите длину стороны B: "))
        c = float(input("Введите длину стороны C: "))
        if a + b > c and a + c > b and b + c > a:
            p = (a + b + c) / 2  # Полупериметр
            area = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"Площадь треугольника: {area:.2f}")
        else:
            print("Невозможно вычислить площадь")

    elif type == 'П':
        # Вычисление площади прямоугольника
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = length * width
        print(f"Площадь прямоугольника: {area:}")
    else:
        print("Неверное значение")

    program_end = input("Завершить программу? Если да, введите (Y): ")
    if program_end == "y":
        print("Программа завершена.")
        break
    elif program_end == "Y":
        print("Программа завершена.")
        break