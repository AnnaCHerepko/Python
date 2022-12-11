field = list(range(1,10))

def draw_field(field):
    print('-'*10)
    for i in range(3):
        print(field[0+i*3],'|', field[1+i*3], '|', field[2+i*3])
        print('-'*10)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход ' + tic_tac + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Некорректный ввод')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(field[player_index-1]) not in 'XO'):
                field[player_index-1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')

def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def game(field):
    counter =0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(tmp,'Победа')
                win = True
                break
            if counter == 9:
                print('Ничья')
        draw_field(field)
game(field)
