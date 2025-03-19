sale_amount = float(input("Введите сумму продажи: "))

if sale_amount <= 5000:
    discount = sale_amount * 0.05
elif sale_amount <= 15000:
    discount = sale_amount * 0.12
elif sale_amount <= 25000:
    discount = sale_amount * 0.20
else:
    discount = sale_amount * 0.30

print(f"Сумма скидки: {discount:} руб.")

final_amount = sale_amount - discount
print(f"Сумма, учитывая скидку: {final_amount:} руб.")