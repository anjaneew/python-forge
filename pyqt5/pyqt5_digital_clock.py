# Python PyQt5 Digital Clock

# Fonts - Ds Digital - TTF file (.ttf TrueType Font)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 300, 300, 200) 

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)   
        self.setLayout(vbox)

        # styling
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;" 
                                      "color: #34f52a") 
        self.setStyleSheet("background-color: #181f18")

        # custom font
        font_id = QFontDatabase.addApplicationFont("pyqt5/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        # add functionality
        self.timer.timeout.connect(self.update_time) # update regularly
        self.timer.start(1000) # update every 1 second

        self.update_time() 

    def update_time(self): 
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # AP - AM PM
        self.time_label.setText(current_time) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())