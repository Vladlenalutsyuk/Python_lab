s = input("Введите строку: ")
revers_s = ""
i = len(s) - 1  
while i >= 0:
    revers_s += s[i]
    i -= 1

print("Перевёрнутая строка:", revers_s)
