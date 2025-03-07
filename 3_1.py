num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
oper = input("Введите операцию (+, -, *, /): ")

if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2
elif oper == "/":
    if num2 == 0:
        result = "Ошибка: деление на ноль"
    else:
        result = num1 / num2
else:
    result = "Ошибка: неизвестная операция"

print(f"Результат: {result}")
