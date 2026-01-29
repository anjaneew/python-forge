# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("/home/anjaneew/python-forge/pyqt5/dragon.png")
        label.setPixmap(pixmap)

        # scale image to size of label
        label.setScaledContents(True)

        #--------------positioning--------------

        # # bottom right
        # label.setGeometry(self.width() - label.width(),
        #                   self.height() - label.height(), 
        #                   label.width(), label.height())
        
        # # bottom left
        # label.setGeometry(0,
        #                   self.height() - label.height(), 
        #                   label.width(), label.height())

        # center                                    // integer division
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2, 
                          label.width(), label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()