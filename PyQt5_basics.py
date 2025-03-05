#PyQt5 intro
# PyQt5 layouts
#PyQt5 BUTTONS
# PyQt5 Checkboxes



#PyQt5 intro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5. QtCore import Qt   #to allign the text
from PyQt5. QtGui import QPixmap #import an image to our gui

class MainWindow(QMainWindow):                       #inherit from QMainWindow  #this is the starting line for the constructor
    def __init__(self):
        super().__init__()                           #we use super in case we need to pass argument to the parent    #the three lines are constructor
        self.setWindowTitle("MY FIRST GUI")
        self.setGeometry(750,300,500,500)
        self.setWindowIcon(QIcon("mcdonalds-logo.webp"))

        label = QLabel("Hello!",self)                #self refers to the window object
        label.setFont(QFont("Arial,40"))
        label.setGeometry(0,0,500,100)                #sets the placement of text
        label.setStyleSheet("color:red;"
                            "background-color: #ab1b34;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline; ")             #sets the font color
        
        label = QLabel(self)                           #this is for importing an image
        label.setGeometry(0, 0, 250, 250)
        
        
        pixmap = QPixmap("mcdonalds-logo.webp")
        label. setPixmap(pixmap)

        label. setScaledContents (True)
        label. setGeometry((self.width() - label.width()) // 2,  #we put minus so that the image doesnt appear behind or hidden
                            self.height() - label.height(),
                            label.width(),
                            label.height())
        
        # label. setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label. setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label. setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        # label. setAlignment(Qt.AlignRight)# HORIZONTALLY RIGHT
        # label. setAlignment(Qt.AlignHCenter)# HORIZONTALLY CENTER
        # label. setAlignment(Qt.AlignLeft)# HORIZONTALLY LEFT
        # label.setAlignment(Qt.AlignHCenter| Qt.AlignTop) # CENTER & TOP
        # label. setAlignment(Qt.AlignHCenter|Qt. AlignBottom) # CENTER & BOTTOM
        # label. setAlignment(Qt.AlignHCenter| Qt. AlignVCenter) # CENTER & CENTER
        label. setAlignment(Qt.AlignCenter) # CENTER & CENTER

def main():
    app= QApplication(sys.argv)                     #inside the argument, we can just pass in an empty list [] but we put sys.argv which is argumments,not realy important now
    window= MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()                                          #in case we nee to run this program directly,then just invoke the function main



# PyQt5 layouts
import sys
from PyQt5. QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)


class MainWindow(QMainWindow) :
    def __init__(self):
        super() .__init__()
        self.setGeometry(700, 300, 500, 500) 
        self.initUI()


    def initUI (self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)
        label4=QLabel("#4",self)
        label5=QLabel("#5",self)

        vbox=QVBoxLayout()       #vbox means vertical box, hbox horizontal, grid gives grid but must insert row and collumn
    

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget . setLayout (vbox)

        label1. setStyleSheet ("background-color: red; ")
        label2. setStyleSheet ( "background-color: yellow; ")
        label3. setStyleSheet ("background-color: green;")
        label4. setStyleSheet ( "background-color: blue; ")
        label5 . setStyleSheet ("background-color: purple; ")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window. show()
    sys. exit (app.exec_())
if __name__ == "__main__":
    main()





#PyQt5 BUTTONS

import sys
from PyQt5. QtWidgets import QMainWindow, QApplication, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me!",self)
        self.label = QLabel("HELLO!!",self)
        self.initUI()


    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)        ##MAIN this is signal.connect(slot)  we take a button then . then list the type of signal, in this case which is clicked and the conect to a slot which is a method, and we invoke the on click funcyion from below

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")
    
    
    def on_click(self):
        self.label.setText("Goodbye")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
sys. exit (app.exec())









# PyQt5 Checkboxes
import sys
from PyQt5. QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5. QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?",self)
        self.initUI()

    def initUI (self) :
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet ("font-size: 30px; "
                                        "font-family: Arial; ")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect (self.checkbox_changed)
    def checkbox_changed (self, state) :
        if state == Qt. Checked:
            print("You like food")
        else:
            print("You DO NOT like food")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
sys. exit (app.exec_())
