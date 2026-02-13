import sys
import random
import json
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QRadioButton,
    QPushButton,
    QButtonGroup,
    QHBoxLayout
)
from PyQt6.QtCore import Qt

# Создаём главное окно приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Объявляем атрибут заранее (чтобы IDE не ругалась)
        self.correct_answer_id = None

        # Загружаем вопросы из JSON-файла
        with open("questions.json", "r", encoding="utf-8") as f:
            self.questions = json.load(f)

        # --- Инициализация сессии ---
        # Берём случайные 50 вопросов из общего списка
        self.selected_questions = random.sample(self.questions, 50)
        self.current_index = 0
        self.score = 0

        # --- Настройка окна ---
        self.setWindowTitle("Тренажер тестов")
        self.setFixedSize(700, 500)

        # Центральный виджет (в QMainWindow обязателен)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Главная вертикальная разметка
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.central_widget.setLayout(self.layout)

        # Заголовок прогресса
        self.progress_label = QLabel("")
        self.progress_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.progress_label)

        # --- Метка прогресса (Вопрос 1 из 50) ---
        self.question_label = QLabel("")
        self.question_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
        """)
        self.question_label.setWordWrap(True)
        self.layout.addWidget(self.question_label)

        # Группа кнопок
        self.button_group = QButtonGroup(self)

        self.option_widgets = []
        self.options_radios = []
        self.options_labels = []

        for i in range(4):
            container, radio, label = self.create_option_widget(i)
            self.layout.addWidget(container)

            self.option_widgets.append(container)
            self.options_radios.append(radio)
            self.options_labels.append(label)

        # Кнопка ответа
        self.answer_button = QPushButton("Ответить")
        self.layout.addWidget(self.answer_button)

        # QLabel для показа правильного ответа
        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.next_button = QPushButton("Далее")
        self.next_button.setVisible(False)
        self.layout.addWidget(self.next_button)

        # Кнопка функции
        self.answer_button.clicked.connect(self.check_answer)
        self.load_question()
        self.next_button.clicked.connect(self.next_question)

    def create_option_widget(self, option_id):
        option_widget = QWidget()
        option_widget.setStyleSheet("""
            padding-top: 6px;
            padding-bottom: 6px;
        """)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        option_widget.setLayout(layout)

        radio = QRadioButton()
        radio.setFixedWidth(20)

        letter_label = QLabel(["A)", "B)", "C)", "D)"][option_id])
        letter_label.setFixedWidth(25)

        text_label = QLabel("")
        text_label.setStyleSheet("""
            font-size: 14px;
        """)
        text_label.setWordWrap(True)

        layout.addWidget(radio)
        layout.addWidget(letter_label)
        layout.addWidget(text_label, 1)

        self.button_group.addButton(radio, option_id)

        return option_widget, radio, text_label

    def next_question(self):
        self.current_index += 1

        if self.current_index >= len(self.selected_questions):
            self.show_result()
        else:
            self.load_question()

    def show_result(self):
        percent = int((self.score / len(self.selected_questions)) * 100)

        self.progress_label.setText("")
        self.question_label.setText("Тест завершён")

        for widget in self.option_widgets:
            widget.hide()

        self.answer_button.hide()
        self.next_button.hide()

        self.result_label.setText(
            f"Результат: {self.score} из {len(self.selected_questions)}\n"
            f"Процент: {percent}%"
        )

    # Метод загрузки вопроса
    def load_question(self):
        question_data = self.selected_questions[self.current_index]

        # Прогресс
        self.progress_label.setText(
            f"Вопрос {self.current_index + 1} из {len(self.selected_questions)}\n"
        )

        # Текст вопроса
        self.question_label.setText(question_data["question"])

        options = question_data["options"]

        for i, option_text in enumerate(options):
            self.options_labels[i].setText(option_text)

        self.correct_answer_id = question_data["correct"]

        # Сброс состояния
        self.button_group.setExclusive(False)
        for radio in self.options_radios:
            radio.setChecked(False)
        self.button_group.setExclusive(True)

        # Сброс цвета вариантов
        for label in self.options_labels:
            label.setStyleSheet("font-size: 14px;")

        for radio in self.options_radios:
            radio.setEnabled(True)

        self.answer_button.setEnabled(True)
        self.result_label.setText("")
        self.next_button.setVisible(False)

    # Метод проверки вопроса
    def check_answer(self):
        selected_id = self.button_group.checkedId()

        if selected_id == -1:
            self.result_label.setText("Выберите вариант ответа.")
            return

        correct_letter = ["A", "B", "C", "D"][self.correct_answer_id]

        # Вывод результата
        if selected_id == self.correct_answer_id:
            self.result_label.setText("Верно!")
            self.score += 1
        else:
            self.result_label.setText(f"Неверно. Правильный ответ: {correct_letter}")

        # Подсветка вариантов
        for i, radio in enumerate(self.options_radios):
            if i == self.correct_answer_id:
                self.options_labels[i].setStyleSheet(
                    "font-size: 14px; color: green; font-weight: 500;"
                )
            elif i == selected_id:
                self.options_labels[i].setStyleSheet(
                    "font-size: 14px; color: red;"
                )

        # Блокируем кнопки
        for radio in self.options_radios:
            radio.setEnabled(False)

        # Отключаем кнопку ответа
        self.answer_button.setEnabled(False)

        # Показываем кнопку "Далее"
        self.next_button.setVisible(True)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())