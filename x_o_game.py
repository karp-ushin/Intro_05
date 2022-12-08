pg_size = 9
pg = ["□" for i in range(pg_size)]  # playground
have_winner = 0
for i in range(pg_size):
    whose_move = 'x' if i % 2 == 0 else 'o'
    move = int(input(f"Ходят {whose_move} : "))
    while not(0 <= move < pg_size):
        move = int(input("Число должно лежать в интервале от 0 до 8 : "))
    while pg[move] != "□":
        move = int(input("Эта клеточка занята. Сходите по-другому : "))
    pg[move] = whose_move
    print(f'{pg[0]} {pg[1]} {pg[2]}')
    print(f'{pg[3]} {pg[4]} {pg[5]}')
    print(f'{pg[6]} {pg[7]} {pg[8]}')
    if (pg[0] == pg[1] == pg[2] != "□") or (pg[3] == pg[4] == pg[5] != "□") or (pg[6] == pg[7] == pg[8] != "□") or \
       (pg[0] == pg[3] == pg[6] != "□") or (pg[1] == pg[4] == pg[7] != "□") or (pg[2] == pg[5] == pg[8] != "□") or \
       (pg[0] == pg[4] == pg[8] != "□") or (pg[2] == pg[4] == pg[6] != "□"):
        print(f'Выиграли {whose_move}.')
        have_winner = 1
        break
if have_winner == 0:
    print('Ничья.')
