def check_number(n):
    if n > 0:
        return "положительное"
    elif n < 0:
        return "min"
    else:
        return "ноль"
    else:
        return "ноль"
num = int(input("Введите : "))
print(check_number(num))
