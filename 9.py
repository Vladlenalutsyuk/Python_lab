import string  

def file(name):  
    f1 = open(name, "r") 
    lines = f1.readlines()  
    f1.close()  

    total_lines = len(lines)  #количество строк
    total_punctuation = 0  #количество знаков препинания
    punctuation_counts = {}  #для хранения и учета каждого знака препинания

    for line in lines:  
        for char in line:  
            if char in string.punctuation:  
                total_punctuation += 1  #общий счётчик знаков
                if char in punctuation_counts:
                    punctuation_counts[char] += 1  #увеличиваем счётчик для конкретного знака
                else:
                    punctuation_counts[char] = 1  #если знака ещё нет в словаре, добавляем его

    
    print("Общее количество строк:", total_lines)
    print("Общее количество знаков препинания:", total_punctuation)
    print("Количество каждого знака препинания:")
    for char, count in punctuation_counts.items():
        print(char, ":", count)

name = "lab_9.txt"
file(name)
