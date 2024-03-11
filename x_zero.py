# Игра крестики нолики практическое задание

def print_board(board): # Игровое поле
    print("   1   2   3") # обозначения столбцов
    for i in range(3):
        print(f"{i + 1} [{'] ['.join(board[i])}]") # соединяем строки так чтоб "клетки" заполнялись используем f-строки


def check_win(board, player): # Проверка победителя
    for line in board:
        if all(cell == player for cell in line):
            return True
    for col in range(3):
        if all(board[line][col] == player for line in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def x_zero(): # тело игры
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Игра в «Крестики-нолики»")
    print_board(board)

    for _ in range(9):
        print(f"Ход игрока за {players[current_player]}")
        good_move = False
        while not good_move:
            line = int(input("Выберите строку (1-3): "))
            col = int(input("Выберите столбец (1-3): "))

            if line in range(1, 4) and col in range(1, 4):
                line -= 1
                col -= 1

                if board[line][col] == " ":
                    good_move = True
                else:
                    print("Эта клетка уже занята. Выберете другую.")
            else:
                print("Номер строки или столбца за пределами игрового поля. Повтроите ход.")

        board[line][col] = players[current_player]
        print_board(board)

        if check_win(board, players[current_player]):
            print(f"Победил игрок за {players[current_player]}!")
            return

        current_player = 1 - current_player

    print("Ничья!")


x_zero()