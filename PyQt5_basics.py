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
