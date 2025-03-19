while True:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))

    result = num_1 + num_2
    print(f"Сумма чисел: {result}")

    program_end = input("Завершить программу? Если да, введите (Y): ")
    if program_end == "y":
        print("Программа завершена.")
        break
    elif program_end == "Y":
        print("Программа завершена.")
        break