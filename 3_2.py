vr = input("Введите математическое выражение: ")

for oper in "+-*/":
    if oper in vr:
        num1, num2 = vr.split(oper)
        num1, num2 = float(num1), float(num2)
        break
else:
    print("Ошибка: некорректное выражение")
    exit()

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

print(f"Результат: {result}")
