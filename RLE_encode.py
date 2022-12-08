def encode(s):

    encoded = ""  # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        # добавляет к результату текущий символ и его количество
        encoded += str(count) + s[i]
        i += 1
    return encoded


input_string = 'ABBCCC'
print(encode(input_string))
