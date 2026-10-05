def calculator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else "Zero tho divide cheyaku"

print(calculator(10, 5, '+'))
print(calculator(10, 5, '*'))
