import random 

# Список пользователей и паролей
users = {                                                  
    "admin": "12345",
    "user1": "password123",
    "user2": "qwerty"
}      
def login_system():
    print("Добро пожаловать в систему!")
    username = input("Введите логин: ")                
    password = input("Введите пароль: ")                                

    # Проверка логина и пароля
    if username in users and users[username] == password:
        print(f"Успешный вход! Добро пожаловать, {username}")
        return True
    else:
        print("Неверный логин или пароль.")
        return True

def display():
    print("GAME by Azer Aslanov. Made in Azerbaijan. 29.10.24\n")
    print("WELCOME! WHAT DO YOU WANT TO PLAY?")
    print("If you want to play XoXo, type 'XoXo'.")
    print("If you want to play the random number game, type 'random'.")
    print("If you want to play MS, type 'MS'.")

def random_number_game():
    print("1: Number between 1 and 3 (Level 1)")
    print("2: Number between 5 and 10 (Level 2)")
    print("3: Number between 10 and 20 (Level 3)")
    print("4: Number between 20 and 30 (Level 4)")
    print("5: Number between 30 and 40 (Level 5)")

    def get_random_number(start, end):
        return random.randint(start, end)

    levels = [
        (1, 3),
        (5, 10),
        (10, 20),
        (20, 30),
        (30, 40)
    ]                

    for i, (start, end) in enumerate(levels, 1):
        secret_number = get_random_number(start, end)
        try:
            guess = int(input(f"Guess the number (Level {i}) between {start} and {end}: "))
            if guess == secret_number:
                print(f"YES, that's the correct number! Next level.")
            else:
                print("No, try again!")
                break
        except ValueError:
            print("Please enter a valid number.")
            break                                                              
    print("Game Over")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def xo_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Player {winner} wins!")
                    break
                if is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input, please enter numbers between 0 and 2.")

def ms_game():
    print("In the MS game, two players A and B take turns.")
    print("A plays first. The objective is to guess if the number is bigger or smaller.")

    A_score = 0
    B_score = 0
    round_num = 1

    while round_num <= 5:  # Limit the number of rounds
        print(f"Round {round_num}:")
        W = input("Player A, do you want to guess 'BIGGER' or 'LESS'? ").upper()
        
        if W == "BIGGER":
            A_guess = int(input("Player A, enter your guess: "))
            B_guess = int(input("Player B, enter your guess: "))
            if A_guess > B_guess:
                print("Player A wins this round!")
                A_score += 1
            elif B_guess > A_guess:
                print("Player B wins this round!")
                B_score += 1
            else:
                print("It's a draw this round!")  
        elif W == "LESS":
            A_guess = int(input("Player A, enter your guess: "))
            B_guess = int(input("Player B, enter your guess: "))
            if A_guess < B_guess:
                print("Player A wins this round!")
                A_score += 1
            elif B_guess < A_guess:
                print("Player B wins this round!")
                B_score += 1
            else:
                print("It's a draw this round!")
        else:
            print("Invalid input. Please enter 'BIGGER' or 'LESS'.")
            continue

        round_num += 1

    # Final Score
    print(f"\nFinal Scores: Player A: {A_score} - Player B: {B_score}")
    if A_score > B_score:
        print("Player A wins the game!")
    elif B_score > A_score:
        print("Player B wins the game!")
    else:
        print("It's a tie game!")
                                                                        
# Main loop
if login_system():
    display()
    g = input() 

    if g == "RANDOM":
        random_number_game()
    elif g == "XoXo":
        xo_game()
    elif g == "MS":
        ms_game()
    else:
        print("Invalid game choice.")  
