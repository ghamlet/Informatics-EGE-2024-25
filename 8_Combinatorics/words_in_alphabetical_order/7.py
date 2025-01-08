
def convert(num, base): 
    return sum(razryad * base ** i for i, razryad in enumerate(num[::-1]))

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
word = 'ИНФОРМАТИКА'

c = [alphabet.index(letter) for letter in word]
print(c)

r = convert(c, 33)
print(r + 1)
