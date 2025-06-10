
print(bin(123)[2:])
print(oct(123)[2:])
print(hex(123)[2:])


def convert_to(x, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result.upper() 