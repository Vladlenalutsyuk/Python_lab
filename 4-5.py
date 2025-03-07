class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
        
# важность
def vaj(op): 
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):  
        return 2
    return 0

def run_operator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ValueError("Ошибка: деление на ноль")
        return a / b

def calculation(expression):
    values = Stack()
    operators = Stack()
    i = 0
    
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        
        if expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.push(num)
            i -= 1
        
        elif expression[i] == '(':
            operators.push(expression[i])
        
        elif expression[i] == ')':
            while not operators.is_empty() and operators.peek() != '(':
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                values.push(run_operator(a, b, op))
            operators.pop()
        
        elif expression[i] in ('+', '-', '*', '/'):
            while (not operators.is_empty() and
                   vaj(operators.peek()) >= vaj(expression[i])):
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                values.push(run_operator(a, b, op))
            operators.push(expression[i])
        
        i += 1
    
    while not operators.is_empty():
        b = values.pop()
        a = values.pop()
        op = operators.pop()
        values.push(run_operator(a, b, op))
    
    return values.pop()

expression = input("Введите арифметическое выражение: ")
try:
    result = calculation(expression)
    print("Результат:", result)
except ValueError as e:
    print(e)
