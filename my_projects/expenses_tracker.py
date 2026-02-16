# Expenses Tracker

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QComboBox, QDateEdit, QDoubleSpinBox, QLabel, QPushButton, QVBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# -----------------------------------------------------
# Backend storage

expenses_list = []

class ExpensesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🪙 ~Expenses Tracker App~ 🪙")
        self.setMinimumSize(600, 520)
        self.init_ui()

# --------------- Building UI ------------------
    def init_ui(self):

        # ------ Central Widget ------ 
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(14)
        main_layout.setContentsMargins(24, 24, 24, 24) 

        # ------- Title ------- 
        self.title_label = QLabel("🪙 ~Expenses Tracker~ 🪙")
        self.title_label.setFont(QFont("Georgia", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # ------ Divider --------------
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        # creating widgets
        
        self.category_label = QLabel("Category: ", self)
        self.category_input = QComboBox(self)
        self.amount_label = QLabel("Amount: $", self)
        self.amount_input = QDoubleSpinBox(self)
        self.date_label = QLabel("Date: ", self)
        self.data_input = QDateEdit(self)
        self.submit_button = QPushButton("Submit details", self)
        self.display_button = QPushButton("Display List", self)

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

        # self.setLayout(vbox)
        main_layout.addLayout(vbox)

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
                font-weight: bold;
                margin-bottom: 20px;        
            }
            QPushButton#submit_button{
                padding: 10px;
                background-color: #226ce3;
                color: #19263b;
                margin-bottom: 20px; 
                font-weight: bold;          
            }
            QPushButton#display_button{
                padding: 10px;
                background-color: #15ed90;
                color: #104a31;
                margin-bottom: 20px;
                font-weight: bold;          
            } 
            QPushButton#submit_button:hover{
                padding: 10px;
                background-color: #87ace8;
                color: #0835c9;
                margin-bottom: 20px; 
                font-weight: bold;          
            }
            QPushButton#display_button:hover{
                padding: 10px;
                background-color: #85edc0;
                color: #08301f;
                margin-bottom: 20px;
                font-weight: bold;          
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