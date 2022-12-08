from random import randint
remaining_amount = 100
whose_move = str(randint(1, 2))
while remaining_amount > 0:
    if whose_move == "1":
        whose_move = "2"
    else:
        whose_move = "1"
    print("Осталось " + str(remaining_amount))
    move = int(input("Ход игрока " + whose_move + " : "))
    while not(0 < move <= 28):
        move = int(input("Число должно быть от 1 до 28 : "))
    remaining_amount -= move
print("Выиграл игрок " + whose_move)
