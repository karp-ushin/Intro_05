from random import randint
remaining_amount = 100
print("Всего " + str(remaining_amount))
if str(randint(1, 2)) == "2":    # bot moves
    move = randint(1, 28)
    print("Компьютер взял " + str(move))
    remaining_amount -= move
    print("Осталось " + str(remaining_amount))
while True:
    move = int(input("Ваш ход "))
    while not(0 < move <= 28):
        move = int(input("Число должно быть от 1 до 28 : "))
    remaining_amount -= move
    if remaining_amount <= 0:
        print("Вы победили.")
        break
    print("Осталось " + str(remaining_amount))
    move = randint(1, 28)
    remaining_amount -= move
    if remaining_amount <= 0:
        print("Компьютер победил.")
        break
    print("Компьютер взял " + str(move))
    print("Осталось " + str(remaining_amount))
