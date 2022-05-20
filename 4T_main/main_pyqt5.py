'''
Created on 3 thg 5, 2022

@author: A315-56
'''
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.system("pyuic5 -x Main_ui.ui -o GUI_PYQT5.py")
os.system("pyrcc5 -o Icon_rc.py Icon.qrc")

from GUI_PYQT5 import Ui_MainWindow
from style import *
from GUI_PyQt5_Func import *

            
class MainWindow(Ui_MainWindow):
    def __init__(self):
        self.setupUi(Window)  
        # Window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
        self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
        
        self.Control_btn.setStyleSheet(Control_btn_active)
        
        self.Menu_btn.clicked.connect     (lambda: UIFunctions.ToggleMenu (self, 50, 250))
        self.Control_btn.clicked.connect  (lambda: UIFunctions.Select_Menu(self, 1))
        self.Parameter_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 2))
        self.Setting_btn.clicked.connect  (lambda: UIFunctions.Select_Menu(self, 3))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = MainWindow()
    Window.show()
    sys.exit(app.exec_())






