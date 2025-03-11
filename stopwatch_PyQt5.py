#Python PqQt5 Stopwatch

import sys
from PyQt5.QtWidgets import( QApplication,QWidget,QLabel,
                            QPushButton,QVBoxLayout,QHBoxLayout)

from PyQt5.QtCore import QTimer,QTime,Qt

class Stopwatch(QWidget):   #class of stopwatch will inherit from base class Qwidget
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)  #(hrs,min,sec,msec)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("START",self)
        self.stop_button = QPushButton("STOP",self)
        self.reset_button = QPushButton("RESET",self)
        self.timer = QTimer(self)                #we make a timer to emit a signal at any interval
        self.initUI()

    def initUI(self):      #to decorate our UI
        self.setWindowTitle("STOPWATCH")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox =QHBoxLayout()
       
        hbox.addWidget (self. start_button)
        hbox.addWidget (self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
 
        self.setStyleSheet("""              #purely for decoration
                            QPushButton, QLabel{
                                padding: 20px;
                                font-weight: bold;
                                font-family: calibri;
                            }                           
                            QPushButton{
                                font-size: 50px;
                            }
                            QLabel{
                                font-size: 120px;
                                background-color: hsl(200, 100%, 85%);
                                border-radius: 20px;
                           }
""")

        self.start_button.clicked.connect(self.start)     #we connect a signal(clicked) and connect to a slot(start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)   #we connect a signal(timeout) and connect to a slot(starupdate_display)

    def start(self):
        self.timer.start(10)
        
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time =QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):         #we pass the time in the argument to format it, and we return the time as a string
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        miliseconds=time.msec()  //10  #//10 is integer division to convert three digits to two

        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"  #02 means tow leading zeros

    def update_display(self):
        self.time=self.time.addMSecs(10) #we are updating the time with +10 miliseconds
        self.time_label.setText(self.format_time(self.time))

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch =Stopwatch()
    stopwatch.show()          #this is to show the widget or gui by invoking the fx
    sys.exit(app.exec_())      #to handle the exit by manually exiting the widgets or window
