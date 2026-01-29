# PyQt5 PushButtons

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me!", self) 
        # ⬆️ best practice new variable / object in a class to be under main method
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        # without self prefix - button is a local and onclick method will not recognize it.
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        #           signal.connect(slot=self.name of method)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)  
        self.label.setText("Goodbye!") 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        