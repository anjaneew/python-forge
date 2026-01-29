# PyQt5 layouts - vertical , horizontal & grid layouts
# To display layout:
#   1. create a generic widget
#   2. add a layout manager to that widget
#   3. add that widget to the main window 

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout )
#                            layout managers

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)    

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: #f5aa7f;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: #7facf5;")
        label4.setStyleSheet("background-color: pink;")
        label5.setStyleSheet("background-color: #7ff5ce;")

# ---------layout manager---------
# grid
        grid = QGridLayout()

# need to specify          row & coloumn
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 0)

        central_widget.setLayout(grid)

'''  layout managers
# Horizontal Layout Manger

        hbox = QHBoxLayout() # horizontal

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)

   Vertical Layout manager
        vbox = QVBoxLayout() # vertical

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)
'''

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()            