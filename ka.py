def check_number(n):
    if n > 0:
        return "положительное"
    elif n < 0:
        return "отрицательное"
    else:
        return "ноль"

num = int(input("Введите число: "))
print(check_number(num))
