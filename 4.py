while True:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))

    result = num_1 + num_2
    print(f"Сумма чисел: {result}")

    program_end = input("Завершить программу? Если да, введите (Y): ")
    if "y" == program_end or "Y" == program_end :
        print("Программа завершена.")
        break
