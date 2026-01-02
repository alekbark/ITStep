# Задание №1
"""
import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    return math.factorial(n)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sine(n):
    return math.sin(math.radians(n))

def cosine(n):
    return math.cos(math.radians(n))

def tangent(n):
    return math.tan(math.radians(n))

while True:
    choice = input("Choose an operation:\n1 – Addition\n2 – Subtraction\n3 – Multiplication\n4 – Division\n5 – Power\n6 – Factorial\n7 – Fibonacci\n8 – Sine\n9 – Cosine\n10 – Tangent\n0 – Exit\n")

    if choice == "0":
        break
    elif choice == "1":
        print(addition(float(input("Enter first number: ")), float(input("Enter second number: "))))
    elif choice == "2":
        print(subtraction(float(input("Enter first number: ")), float(input("Enter second number: "))))
    elif choice == "3":
        print(multiplication(float(input("Enter first number: ")), float(input("Enter second number: "))))
    elif choice == "4":
        print(division(float(input("Enter first number: ")), float(input("Enter second number: "))))
    elif choice == "5":
        print(power(float(input("Enter first number: ")), float(input("Enter second number: "))))
    elif choice == "6":
        print(factorial(int(input("Enter number: "))))
    elif choice == "7":
        print(fibonacci(int(input("Enter number: "))))
    elif choice == "8":
        print(sine(int(input("Enter number: "))))
    elif choice == "9":
        print(cosine(int(input("Enter number: "))))
    elif choice == "10":
        print(tangent(int(input("Enter number: "))))
"""

# Задание №2
"""
board = list(map(str, range(1, 10)))
turn = "X"

def print_board(board):
    lines = [" | ".join(board[i:i+3]) for i in range(0, 9, 3)]
    border = "----------"
    print(F"{border}\n{lines[0]}\n{border}\n{lines[1]}\n{border}\n{lines[2]}\n{border}\n")

def check_winner(board):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]
    if any(cell not in ("X", "O") for cell in board):
        return None
    return "Draw"

def make_move(board, mark):
    while True:
        n = int(input(f"Куда поставим {mark}?: "))
        if n < 1 or n > 9:
            print("Ваш выбор вне диапазона игрового поля")
            continue
        idx = n - 1
        if board[idx] in ("X", "O"):
            print("Выбранная клетка уже занята!")
            continue
        board[idx] = mark
        break


while True:
    print_board(board)
    make_move(board, turn)
    result = check_winner(board)
    if result:
        print_board(board)
        if result == "Draw":
            print("Draw")
        else:
            print(f"{result} wins!")
        break
    turn = "O" if turn == "X" else "X"
"""

# Модули и пакеты. Задание №1
"""
from collections import Counter

candidate_list = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]


def count_votes(votes):
    counter = Counter(votes)
    return counter

def get_winner(counts):
    max_votes = max(counts.values())
    leaders = [name for name, cnt in counts.items() if cnt == max_votes]
    if len(leaders) == 1:
        return leaders[0]
    else:
        return min(leaders, key=len)

def collect_votes():
    votes = []
    while True:
        print("Кандидаты:", *candidate_list)
        name = input("Введите имя выбранного кандидата: ").strip()
        if name in candidate_list:
            votes.append(name)
            continue
        elif name == "стоп":
            return votes
        else:
            print("Имя кандидата выбрано неверно")
            continue

def main():
    votes = collect_votes()
    counts = count_votes(votes)
    winner = get_winner(counts)
    print(f"В выборах одержал(-а) победу {winner}")

main()
"""