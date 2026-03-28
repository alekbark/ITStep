import random

def play_game():
    print("Добро пожаловать в игру: Камень, Ножницы, Бумага!")

    while True:
        print("\nВыберите:")
        print("1 - Камень")
        print("2 - Ножницы")
        print("3 - Бумага")

        user_input = input("Ваш выбор: ")

        if user_input not in ["1", "2", "3"]:
            print("Некорректный ввод!")
            continue

        choices = {
            "1": "Камень",
            "2": "Ножницы",
            "3": "Бумага"
        }

        user_choice = choices[user_input]
        computer_choice = random.choice(list(choices.values()))

        print(f"\nВы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        # Логика определения победителя
        if user_choice == computer_choice:
            print("Ничья!")
        elif (
            (user_choice == "Камень" and computer_choice == "Ножницы") or
            (user_choice == "Ножницы" and computer_choice == "Бумага") or
            (user_choice == "Бумага" and computer_choice == "Камень")
        ):
            print("Вы победили! 🎉")
        else:
            print("Вы проиграли 😢")

        # Повтор игры
        again = input("\nСыграть ещё раз? (y/n): ").lower()
        if again != "y":
            print("Спасибо за игру!")
            break


# запуск
play_game()