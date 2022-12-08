def decode(s):

    decoded = ""  # сохраняет выходную строку
    i = 0
    while i < len(s):
        j = 1
        # выделяет число, задающее количество вхождений символа
        while s[i:i+j:].isdecimal():
            j += 1
        i += j
        # добавляет к результату символ в нужном количестве
        decoded += s[i-1]*int(s[i-j:i-1])
    return decoded


input_string = '3A12B1C5D'
print(decode(input_string))
