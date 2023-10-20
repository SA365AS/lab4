units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

n = int(input('Введите сумму: '))

if not 1 <= n <= 100000:
    print('Число должно быть от 1 до 100000')
else:
    num_str = str(n).zfill(6)
    result = ''

    if int(num_str[:3]) > 0:
        result += hundreds[int(num_str[0])] + ' '

    if int(num_str[1:3]) in range(10, 20):
        result += teens[int(num_str[2])] + ' '
    else:
        if int(num_str[1]) > 0:
            result += tens[int(num_str[1])] + ' '
        if int(num_str[2]) > 0:
            result += units[int(num_str[2])] + ' '

    if int(num_str[:3]) > 0:
        if int(num_str[1:3]) not in range(10, 20) and int(num_str[2]) in range(2, 5):
            result += 'тысячи '
        elif int(num_str[2]) == 1:
            result += 'тысяча '
        elif int(num_str[2]) > 1 or (int(num_str[1]) > 0 and int(num_str[0]) == 0):
            result += 'тысяч '

    if int(num_str[3]) > 0:
        result += hundreds[int(num_str[3])] + ' '

    if int(num_str[4:6]) in range(10, 20):
        result += teens[int(num_str[5])] + ' '
    else:
        if int(num_str[4]) > 0:
            result += tens[int(num_str[4])] + ' '
        if int(num_str[5]) > 0 and int(num_str[4]) != 1:
            result += units[int(num_str[5])] + ' '

    if int(num_str) % 10 == 1 and int(num_str) % 100 != 11:
        result += 'рубль'
    elif 2 <= int(num_str[-1]) <= 4 and (int(num_str) % 100 < 10 or int(num_str) % 100 > 20):
        result += 'рубля'
    else:
        result += 'рублей'

    print(result)




