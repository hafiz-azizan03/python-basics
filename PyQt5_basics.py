#PyQt5 intro 10
# PyQt5 layouts 70
#PyQt5 BUTTONS 130
# PyQt5 Checkboxes 180
#PyQt5 Radio Button 220
# PyQt5LineEdit 290
# PyQt5 setStyleSheet() 330


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










#PyQt5 Radio Button

import sys
from PyQt5. QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)               #defining the buttons

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)                  #grouping the buttons
        self.initUI()


    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)                    #setting the position of the buttons
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self. setStyleSheet("QRadioButton{"
                            "font-size: 40px;"
                            "font-family: Arial;"
                            "padding: 10px;"
                            "}")                                #decorating the fonts
        
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)             #dividing buton 1-3 and 4,5 into two separate groups
        
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)     

    def radio_button_changed(self): 
        radio_button = self.sender()                    #sending the signal
    
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())











# PyQt5LineEdit            #in other words, text boxes

import sys
from PyQt5. QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)              #call the self.line.edit method
        self.button = QPushButton("Submit",self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                        "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px; "
                                    "font-family: Arial")
        self.line_edit.setPlaceholderText("Enter your name")    #the place holder is the shadow text 
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())








# PyQt5 setStyleSheet()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a horizontal layout
        hbox = QHBoxLayout()

        # Add buttons to the layout
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Set the layout for the central widget
        central_widget.setLayout(hbox)

        # Set object names for the buttons to apply custom styles
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Apply styles to the buttons
        self.setStyleSheet("""
            /* Global style for all QPushButton widgets */
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px; /* Top/Bottom, Left/Right */
                margin: 25px; /* Margin between buttons */
                border: 3px solid; /* Solid border */
                border-radius: 15px; /* Rounded corners */
            }
            
            /* Custom styles for individual buttons by object name */
            QPushButton#button1:hover {
                background-color: red;
            }
            QPushButton#button2:hover {
                background-color: green;
            }
            QPushButton#button3:hover {
                background-color: blue;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



