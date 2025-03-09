#PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt                                 #Qt is for allignment



class DigitalClock(QWidget):          #inherit from QWidget to make the clock a widget itself
    def __init__(self):
        super().__init__()
        self.time_label =QLabel(self)
        self.timer=QTimer(self)         #to call the timer
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100) #approximately at the centre
 
        vbox= QVBoxLayout()  #this sets all the widgets vertically
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)  #alligning the time at the centre

        self. time_label. setStyleSheet("font-size: 150px;"                  #this is just to design adn customize the fonts and background
                                        "font-family: Arial;"
                                        "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)      #this connect our TIME WIDGET to our slot of update_time // we trigger a timeout signal every 1000ms=1s  and send the signal to our update_time
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")     #hh mm ss are format specifiers // AP means AM or PM
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    clock= DigitalClock()
    clock.show()
    sys.exit(app.exec_())
