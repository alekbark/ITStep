# import random
#
# def guess_number():
#     print("Игра: Угадай число (от 1 до 100)")
#
#     number = random.randint(1, 100)
#
#     while True:
#         guess = int(input("Введите число: "))
#
#         if guess > number:
#             print("Меньше!")
#         elif guess < number:
#             print("Больше!")
#         else:
#             print("Ты угадал! 🎉")
#             break
#
# guess_number()


# def quiz():
#     print("Викторина!")
#
#     questions = [
#         {"q": "Столица Франции?", "a": "париж"},
#         {"q": "2 + 2 = ?", "a": "4"},
#         {"q": "Цвет неба?", "a": "синий"}
#     ]
#
#     score = 0
#
#     for item in questions:
#         answer = input(item["q"] + " ").lower()
#
#         if answer == item["a"]:
#             print("Правильно!")
#             score += 1
#         else:
#             print("Неправильно!")
#
#     print(f"Ваш результат: {score}/{len(questions)}")
#
# quiz()


import random

HANGMAN_PICS = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

def hangman():
    words = ["python", "pizza", "code"]
    word = random.choice(words)
    guessed = ["_"] * len(word)

    used_letters = []
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("Игра: Виселица")

    while attempts < max_attempts:
        print(HANGMAN_PICS[attempts])
        print("Слово:", " ".join(guessed))
        print("Использованные буквы:", ", ".join(used_letters))

        letter = input("Введите букву: ").lower()

        # Проверка ввода
        if len(letter) != 1 or not letter.isalpha():
            print("Введите одну букву!")
            continue

        # Проверка повторов
        if letter in used_letters:
            print("Ты уже вводил эту букву!")
            continue

        used_letters.append(letter)

        # Проверка попадания
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            attempts += 1
            print("Неверно!")

        # Победа
        if "_" not in guessed:
            print("\nТы победил! 🎉")
            print("Слово:", word)
            return

    # Проигрыш
    print(HANGMAN_PICS[attempts])
    print("\nТы проиграл 😢")
    print("Слово было:", word)


# запуск
hangman()