def day_num_and_seas(day, month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1]:
        return "Ошибка: некорректная дата"

    
    day_num = sum(days_in_month[:month - 1]) + day
    
    if month in [12, 1, 2]:
        season = "Зима"
    elif month in [3, 4, 5]:
        season = "Весна"
    elif month in [6, 7, 8]:
        season = "Лето"
    else:
        season = "Осень"
    
    return f"День в году: {day_num}, Сезон: {season}"


day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

print(day_num_and_seas(day, month))