# PyQt5 CSS Styles - setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700, 300, 500, 500) - unnecessary cz of layout manager
        self.button1 = QPushButton("#1") #  - ', self' unnecessary cz of layout manager
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        # helps to differentiate
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # add css to a class
        # note - if hsl(141, 90%, 62%) - remove °
        self.setStyleSheet("""
            QPushButton{
                font-size: 30px;
                font-family: Arial;
                padding: 10px 20px;
                margin: 10px;
                border: 1px solid;
                border-radius: 15px;                                                           
            }
            QPushButton#button1{
                background-color: #f54994           
            }   
            QPushButton#button2{
                background-color: #49f585           
            } 
            QPushButton#button3{
                background-color: #81aef7           
            }
            QPushButton#button1:hover{
                background-color: #e30264;
                font-weight: bold;           
            }   
            QPushButton#button2:hover{
                background-color: #05f559;
                font-weight: bold;           
            } 
            QPushButton#button3:hover{
                background-color: #1064eb;
                font-weight: bold;           
            }           
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        

