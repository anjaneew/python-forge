# Expenses Tracker

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QDateEdit, QDoubleSpinBox, QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class ExpensesApp(QWidget):
    def __init__(self):
        super().__init__()
        # creating widgets
        self.title_label = QLabel("Enter your expenses", self)
        self.category_label = QLabel("Category: ", self)
        self.category_input = QComboBox(self)
        self.amount_label = QLabel("Amount: $", self)
        self.amount_input = QDoubleSpinBox(self)
        self.date_label = QLabel("Date: ", self)
        self.data_input = QDateEdit(self)
        self.submit_button = QPushButton("Submit new details", self)
        self.display_button = QPushButton("Display Expenses List", self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("~Expenses Tracker~")

        # verticle layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.category_label)
        vbox.addWidget(self.category_input)
        vbox.addWidget(self.amount_label)
        vbox.addWidget(self.amount_input)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.data_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.display_button)

        self.setLayout(vbox)

        # making widgets aligned to center
        self.title_label.setAlignment(Qt.AlignCenter)

        # stylling: 
        # 1) labelling objects
        self.title_label.setObjectName("title_label")
        self.category_label.setObjectName("category_label")
        self.category_input.setObjectName("category_input")
        self.amount_label.setObjectName("amount_label")
        self.amount_input.setObjectName("amount_input")
        self.date_label.setObjectName("date_label")
        self.data_input.setObjectName("data_input")
        self.submit_button.setObjectName("submit_button")
        self.display_button.setObjectName("display_button")

        # 2) css 
        self.setStyleSheet("""
            QLabel, QComboBox, QDateEdit, QPushButton, QDoubleSpinBox{
                  font-family: calibri; 
                  font-size: 15px;                 
            }
            QLabel#title_label{
                           
            }
            QLabel#{
                           
            }
            QLabel#{
                           
            }                 
        """)

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