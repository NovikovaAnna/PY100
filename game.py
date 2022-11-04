#рисуем игровое поле

game_table = range(9)

def draw_table(game_table):
    print("..............")
    for n in range(3):
        print("|", game_table[0+n*3], "|", game_table[1+n*3], "|", game_table[2+n*3], "|")
        print("..............")
#ввод данных  игроками
def get_input(player_1):
    valid = False
    while not valid:
        player_2 = input( "Ваш ход " + player_1 )
        try:
            player_2 = int(player_2)
        except:
            print("Некорректный ход, введите число")
            continue
        if player_2 >= 1 and player_2 <= 9:
            if(str(game_table[player_2-1])) not in "XO":
                game_table[player_2-1] = player_1
                valid = True
            else:
                print(" Клетка занята")
        else:
            print(" Неверно. Введите число от 1 до 9")
#Проверка победителя
def check_winner(game_table):
    winnig_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8,),(0,4,8),(2,4,6))
    for each in winnig_combination:
        if game_table[each[0]] == game_table[each[1]] == game_table[each[2]]:
            return game_table[each[0]]
    return False

def main(game_table):
    counter = 0
    win = False
    while not win:
        draw_table(game_table)
        if counter %2 == 0:
            get_input("X")
        else:
            get_input("O")
        counter += 1
        if counter > 4 :
            tmp = check_winner(game_table)
            if tmp :
                print( "Winner!")
                win = True
                break
        if counter == 9:
            print ("Play again! There is no winner!")
            break
    draw_table(game_table)
main(game_table)

