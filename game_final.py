"""WIN_COMBINATION = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6)
                   )"""
#функция выйгрышных комбинаций
def win_combinations(game_table):
    diag1 = []
    diag2 = []
    rows = []
    cols = []
    for i in range(game_table):
        tmp_row = []
        tmp_col = []
        for h in range(game_table):
            tmp_row.append((i,h))
            tmp_col.append((h,i))
        rows.append(tmp_row)
        cols.append(tmp_col)
        diag1.append((i,i))
        diag2.append((i,game_table - 1 - i))

    return rows + cols + [diag1] + [diag2]


def draw_table(game_table, rows):
    print("..............")
    for n in range(rows):
        print("|", " | ".join([str(game_table[j+n*rows]) for j in range(rows)]), "|")
        print("..............")


#ввод данных  игроками
def get_input(game_table, player):
    while True:
        cell_to_step = input(f"Ваш ход {player}: ")
        try:
            cell_to_step = int(cell_to_step)
        except ValueError:
            print("Некорректный ход, введите число")
            continue
        if 1 <= cell_to_step <= 9:
            if game_table[cell_to_step-1] not in ("X", "O"):
                return cell_to_step
            else:
                print(" Клетка занята")
        else:
            print(" Неверно. Введите число от 1 до 9")


#Проверка победителя
def check_winner(game_table, win_combination):
    for each in win_combination:
        win = True
        for cell in each[1:]:
            win *= game_table[cell] == game_table[each[0]]
        if win:
            return True
    return False


def game(game_table, player, size, rows):
    counter = 0
    current_player = player
    while counter < size:
        draw_table(game_table, rows)
        cell_to_step = get_input(game_table, current_player)
        counter += 1
        game_table[cell_to_step - 1] = current_player
        if counter > 4:
            win = check_winner(game_table, WIN_COMBINATION)
            if win:
                print(f"Winner! player {current_player}")
                break
        current_player = "O" if current_player == "X" else "X"
    if counter == size and not win:
        print("Play again! There is no winner!")
    draw_table(game_table, rows)


def main():
    size = 9
    rows = 3
    start_player = "X"
    game_table = list(range(1, size + 1))  # создаём игровое поле
    game(game_table, start_player, size, rows)


if __name__ == "__main__":
    main()