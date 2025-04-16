def is_simple_number(x):
    if x < 2:  # 0 и 1 не являются простыми
        return False
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True  # Исправлено на True
print(is_simple_number(4))