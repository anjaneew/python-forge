# PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt # to work with states

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        #            text content & where to add the checkbox
        self.checkbox = QCheckBox("Do you trust yourself?", self) 
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 200)
        self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Arial;")
        self.checkbox.setChecked(False) # can change default behavior 
        #     connecting signal of state change to a slot of checkbox change
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        # checkbox.*signal*.connect(*slot=self.name of method*)


    # adding functionality
    def checkbox_changed(self, state):
        print(state) # values >  0 unchecked 2 checked 1 partially checked 
        # if state == 2: better way below
        if state == Qt.Checked:
            print("You got this! Keep going.")
        else:
            print("Have no fear, " \
            "you'll find your way. " \
            "It's in your bones. " \
            "It's in your soul.")    
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())    