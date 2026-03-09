# Expenses Tracker

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QComboBox, QDateEdit, QDoubleSpinBox, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,  QTableWidget, QTableWidgetItem, QHeaderView, QFrame
    )
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor

# -----------------------------------------------------
# Backend storage

expenses_list = []

class ExpensesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("~Expenses Tracker App~")
        self.setMinimumSize(350, 420) # width  & height
        self.init_ui()

# --------------- Building UI ------------------
    def init_ui(self):

        # ------ Central Widget ------ 
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setSpacing(5) # space between widgets
        main_layout.setContentsMargins(18, 18, 18, 18)  
        # space between the layout and the window edges

        # ------- Title ------- # Note: self.title -> to keep the code consistence cz other parts has it
        self.title_label = QLabel("🪙 ~Expenses Tracker~ 🪙")
        self.title_label.setFont(QFont("Georgia", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # ------ Divider --------------
        line1 = QFrame()
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line1)        

        #------ Input Area --------------

        # Puts widgets in a row (left to right) →→→
        #Like: [widget1] [widget2] [widget3]
        form_layout = QHBoxLayout()
        form_layout.setSpacing(5)

        # 1. Expenses Category 
        col1 = QVBoxLayout()
        col1.addWidget(QLabel("Category: ")) # Self removed from widget creation - latest
        self.category_input = QComboBox()
        self.category_input.addItems(["Groceries", "Transport", "Communication", "Rent", "Medicine"])
        col1.addWidget(self.category_input)
        form_layout.addLayout(col1)

        # 2. Expenses Amount
        col2 = QVBoxLayout()
        col2.addWidget(QLabel("Amount: "))
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0.01, 99999.99) # min / max values
        self.amount_input.setSingleStep(0.50) # arrow step
        self.amount_input.setDecimals(2)  # decimal places
        self.amount_input.setValue(10.00) # default value
        self.amount_input.setPrefix("$ ") # prefix
        col2.addWidget(self.amount_input)
        form_layout.addLayout(col2)

        # 3. Date
        col3 = QVBoxLayout()
        col3.addWidget(QLabel("Date: "))
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setDisplayFormat("yy-MMM-d")
        col3.addWidget(self.date_input)
        form_layout.addLayout(col3)

        # adding to main
        main_layout.addLayout(form_layout)

        #=== Add Button =======
        self.add_btn = QPushButton("Add New Expense")
        self.add_btn.setFixedHeight(40)
        self.add_btn.setFont(QFont("Arial", 11, QFont.Bold)) # QFont.Bold is a constant
        self.add_btn.setStyleSheet(
            "QPushButton { background-color: #e07b54; color: #571b17;}"
            "QPushButton:hover { background-color: #c9623c; }"
            "QPushButton:pressed { background-color: #a84e30; }"
        )

        #Connect the button click to our handler function
        self.add_btn.clicked.connect(self.store_expenses)
        main_layout.addWidget(self.add_btn)

        # ----- Divider -----
        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line2)

        # ===== Expenses History =========
        history_label = QLabel("Expenses History")
        history_label.setFont(QFont("Georgia", 13, QFont.Bold))
        history_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(history_label)


        # creating widgets
        # self.category_label = QLabel("Category: ", self)
        # self.category_input = QComboBox(self)
        # self.amount_label = QLabel("Amount: $", self)
        # self.amount_input = QDoubleSpinBox(self)

        # self.date_label = QLabel("Date: ", self)
        # self.data_input = QDateEdit(self)
        # self.submit_button = QPushButton("Submit details", self)
        # self.display_button = QPushButton("Display List", self)

        # verticle layout
        # vbox = QVBoxLayout()

        # vbox.addWidget(self.category_label)
        # vbox.addWidget(self.category_input)
        # vbox.addWidget(self.amount_label)
        # vbox.addWidget(self.amount_input)
        # vbox.addWidget(self.date_label)
        # vbox.addWidget(self.data_input)
        # vbox.addWidget(self.submit_button)
        # vbox.addWidget(self.display_button)

        # self.setLayout(vbox)
        # main_layout.addLayout(vbox)

        # making widgets aligned to center
        # self.title_label.setAlignment(Qt.AlignCenter)

        # stylling: 
        # 1) labelling objects
        # self.title_label.setObjectName("title_label")
        # self.category_label.setObjectName("category_label")
        # self.category_input.setObjectName("category_input")
        # self.amount_label.setObjectName("amount_label")
        # self.amount_input.setObjectName("amount_input")
        # self.date_label.setObjectName("date_label")
        # self.data_input.setObjectName("data_input")
        # self.submit_button.setObjectName("submit_button")
        # self.display_button.setObjectName("display_button")

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