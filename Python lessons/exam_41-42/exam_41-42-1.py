import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QPushButton, QLabel, QListWidget,
    QVBoxLayout, QHBoxLayout, QMessageBox
)

# ООП

class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def prepare(self):
        steps = [
            f"{self.name}: замешиваем тесто...",
            f"{self.name}: добавляем ингредиенты...",
            f"{self.name}: выпекаем...",
            f"{self.name}: нарезаем...",
            f"{self.name}: упаковываем..."
        ]

        result = ""
        for step in steps:
            result += step + "\n"
            time.sleep(0.3)  # имитация процесса

        return result


class ChickenPizza(Pizza):
    def __init__(self):
        super().__init__("Кисло-сладкий цыпленок", 2000)


class CalzonePizza(Pizza):
    def __init__(self):
        super().__init__("Кальцоне", 2500)


class FourCheesePizza(Pizza):
    def __init__(self):
        super().__init__("Четыре сыра", 3000)


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total_price(self):
        return sum(p.price for p in self.pizzas)


# Интерфейс

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🍕Пиццерия")
        self.setMinimumSize(500, 300)

        self.order = Order()

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # === Меню
        menu_layout = QVBoxLayout()

        btn_chicken = QPushButton("Кисло-сладкий цыпленок")
        btn_calzone = QPushButton("Кальцоне")
        btn_4cheese = QPushButton("Четыре сыра")

        btn_chicken.clicked.connect(self.add_chicken)
        btn_calzone.clicked.connect(self.add_calzone)
        btn_4cheese.clicked.connect(self.add_4cheese)

        menu_layout.addWidget(QLabel("Меню:"))
        menu_layout.addWidget(btn_chicken)
        menu_layout.addWidget(btn_calzone)
        menu_layout.addWidget(btn_4cheese)
        menu_layout.addStretch()

        # === Заказ
        order_layout = QVBoxLayout()

        self.order_list = QListWidget()
        self.total_label = QLabel("Итого: 0")

        btn_checkout = QPushButton("Оформить заказ")
        btn_checkout.clicked.connect(self.checkout)

        order_layout.addWidget(QLabel("Ваш заказ:"))
        order_layout.addWidget(self.order_list)
        order_layout.addWidget(self.total_label)
        order_layout.addWidget(btn_checkout)

        main_layout.addLayout(menu_layout)
        main_layout.addLayout(order_layout)

        # === Удаление
        btn_delete = QPushButton("Удалить выбранную пиццу")
        btn_delete.clicked.connect(self.delete_pizza)

        order_layout.addWidget(btn_delete)

        # Стили
        self.setStyleSheet("""
            QWidget {
                font-size: 14px;
            }
            QPushButton {
                padding: 8px;
                border-radius: 6px;
                background-color: #f0f0f0;
            }
            QPushButton:hover {
                background-color: #d6eaff;
            }
            QLabel {
                font-weight: bold;
            }
        """)

    # Логика

    def add_chicken(self):
        self.add_pizza(ChickenPizza())

    def add_calzone(self):
        self.add_pizza(CalzonePizza())

    def add_4cheese(self):
        self.add_pizza(FourCheesePizza())

    def add_pizza(self, pizza):
        self.order.add_pizza(pizza)
        self.update_ui()

    def delete_pizza(self):
        selected_row = self.order_list.currentRow()

        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Выберите пиццу для удаления")
            return

        del self.order.pizzas[selected_row]
        self.update_ui()

    def update_ui(self):
        self.order_list.clear()

        for pizza in self.order.pizzas:
            self.order_list.addItem(f"{pizza.name} - {pizza.price}")

        self.total_label.setText(f"Итого: {self.order.get_total_price()}")

    def checkout(self):
        if not self.order.pizzas:
            QMessageBox.warning(self, "Ошибка", "Заказ пуст!")
            return

        result_text = ""

        for pizza in self.order.pizzas:
            result_text += pizza.prepare() + "\n"

        result_text += "\n✅ Ваш заказ готов! Заберите его на стойке."

        QMessageBox.information(self, "Готово", result_text)

        self.order = Order()
        self.update_ui()


# Запуск

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())