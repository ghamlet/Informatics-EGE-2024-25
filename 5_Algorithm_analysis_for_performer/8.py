for n in range(10, 100):
    #Строится двоично-десятичное представление – каждый разряд десятичного числа кодируется с помощью 4 бит, затем полученные коды записываются друг за другом с сохранением незначащих нулей.
    chislo = ''.join([bin(int(razryad))[2:].zfill(4) for razryad in str(n)])
    
    # print(chislo)

    #Полученная двоичная последовательность инвертируется – все нули меняются на единиц, все единицы на нули.
    
    chislo: str = chislo.replace("1", "2")
    chislo = chislo.replace("0", "1")
    chislo = chislo.replace("2", "0")
    
    R = int(chislo, 2)
    if R == 151:
        print(n)