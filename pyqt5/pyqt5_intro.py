# GUI = Graphical User Interface

'''
Installation 

virtual environment 
    pip install PyQt5
wsl2
    sudo apt install python3-pyqt5   
check version
    pip show PyQt5   
'''
import sys # system specific parameters & functions
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

'''
# boilerplate for basic window ------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
       super().__init__()

def main(): 
    app = QApplication(sys.argv) # app object
    window = MainWindow() # window object
    window.show()
    sys.exit(app.exec_()) # app's executes method - waits around for user input and handles events 

# sys.argv - allows PyQt5 to pass any command line arguments (future proofing)

if __name__ == "__main__":
    main()

# boilerplate for basic window ------------------------------------------------    
'''

class MainWindow(QMainWindow):
    def __init__(self):
       super().__init__()
       # customization
       self.setWindowTitle("My Python App") # title
    #  self.setGeometry(x, y, width, height) # size & layout
       self.setGeometry(0, 0, 500, 500)

    #  Window icons don't work with basic X11.
       self.setWindowIcon(QIcon("dragon.png"))# windows icon

def main(): 
    app = QApplication(sys.argv) # app object
    window = MainWindow() # window object
    window.show()
    sys.exit(app.exec_()) # app's executes method - waits around for user input and handles events 

# sys.argv - allows PyQt5 to pass any command line arguments (future proofing)

if __name__ == "__main__":
    main()