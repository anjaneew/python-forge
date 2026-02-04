# Expenses Tracker

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDateEdit, QDoubleSpinBox, QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class ExpensesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("Enter your expenses", self)
        self.category_label = QLabel("Category: ", self)
        self.category_input = QComboBox(self)
        self.amount_label = QLabel("Amount: $", self)
        self.amount_input = QDoubleSpinBox(self)
        self.date_label = QLabel("Date: ", self)
        self.data_input = QDateEdit(self)
        self.submit_button = QPushButton("Submit new details", self)
        self.details_label = QLabel("Display Expenses List", self)
        self.display_button = QPushButton("Generate List", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("~Expenses Tracker~")

        # layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.category_label)
        vbox.addWidget(self.category_input)
        vbox.addWidget(self.amount_label)
        vbox.addWidget(self.amount_input)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.data_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.details_label)
        vbox.addWidget(self.display_button)

        self.setLayout(vbox)

        # Category - add items, connect signals
        self.category_input.addItems(["Groceries", "Transport", "Communication", "Rent", "Medicine"])
        self.category_input.currentTextChanged.connect(self.get_expenses)

    def get_expenses(self, category):
        return category

    def store_expenses(self):
        self.get_expenses()

    def display_expenses():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    expenses_app = ExpensesApp()
    expenses_app.show()
    sys.exit(app.exec_())