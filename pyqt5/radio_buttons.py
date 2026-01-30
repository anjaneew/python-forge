# PyQt5 radio buttons

# note - default behavior is all PyQt5 Radio buttons are in same group

import sys
#    package > module   >   class
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                             QRadioButton, QButtonGroup)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        # creating buttons
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("On-line", self)
        # creating button groups to avoid default behavior
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10, 0, 500, 100)
        self.radio2.setGeometry(10, 50, 500, 100)
        self.radio3.setGeometry(10, 100, 500, 100)
        self.radio4.setGeometry(10, 200, 500, 100)
        self.radio5.setGeometry(10, 250, 500, 100)

        # individually - self.radio1.setStyleSheet("font-size: 30px;")

        # self.setStyleSheet("SELECTOR{""styles""}") - multiple elements
        self.setStyleSheet("QRadioButton{""font-size: 30px;""padding: 10px;""}")

        # adding radio buttons to respective button groups
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # adding event listeners
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self): 
         # find sender
         radio_button = self.sender() # return the widget which was selected
         if radio_button.isChecked():
              print(f"{radio_button.text()} is selected.")   

if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec_()) 