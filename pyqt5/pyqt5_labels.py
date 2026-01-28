# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        # creating label - string (text), self (window object)
        label = QLabel("Hello", self)
        # window - parent object
        label.setFont(QFont("Arial", 30)) # font & font size
        label.setGeometry(0, 0, 300, 100) 
        label.setStyleSheet("color: blue; " \
                            "background-color: grey;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline") # must end in ;
        
        # ---------alignments-----------

        # label.setAlignment(Qt.AlignTop) # vertically top
        # label.setAlignment(Qt.AlignBottom) # vertically bottom
        # label.setAlignment(Qt.AlignVCenter) # vertically Center

        # label.setAlignment(Qt.AlignRight) # Horizontally right
        # label.setAlignment(Qt.AlignLeft) # Horizontally left
        # label.setAlignment(Qt.AlignHCenter) # Horizontally center

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # combined  - Center bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # combined  - Center top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # exact center
        label.setAlignment(Qt.AlignCenter) # shortcut exact center


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    