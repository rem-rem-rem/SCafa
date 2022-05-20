from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

os.system("pyuic5 -x load.ui -o LOGIN.py ")

from LOGIN import *

class LOGIN_Main(Ui_MainWindow, QMainWindow):
    def __init__(self, mainwindow):
        QMainWindow.__init__(self)
        self.setupUi(mainwindow)
        mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.close_button.clicked.connect(lambda: self.close())
        # self.setWindowTitle("rem")
        self.BoxButton.clicked.connect(lambda: self.BoxButtonn())
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.close_button.clicked.connect(lambda: self.close())
        # self.setCentralWidget(self.close_button)
        self.comboboxx()

    def comboboxx(self):
        self.comboBox.currentTextChanged.connect(self.laygiatri)

    def  laygiatri(self):
        self.User.setText(self.comboBox.currentText())

    def close(self):
        sys.exit()

    def BoxButtonn(self):
        self.comboBox.showPopup()