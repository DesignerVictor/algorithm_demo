def gcd(num1, num2):
    """更相减损术求最大公约数"""
    if num1 == num2:
        return num1
    if num1 < num2:
        num1, num2 = num2, num1
    tmp = num1 - num2
    while tmp != num2:
        num1 = num2
        num2 = tmp
        if num1 < num2:
            num1, num2 = num2, num1
        tmp = num1 - num2
    return tmp

