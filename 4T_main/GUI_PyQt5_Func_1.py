'''
Created on 7 thg 5, 2022

@author: A315-56
'''

from PyQt5 import QtCore
from PyQt5.QtCore import *

from REM import *
from style import*


class UIFunctions(Ui_MainWindow):
               
    def ToggleMenu(self, minWidth, maxWidth):

        width = self.Slide_menu.width()
        Menu_btn_icon = QtGui.QIcon()
        _translate = QtCore.QCoreApplication.translate
        if width == minWidth:
            newWidth = maxWidth
            self.APP_name.setText      (_translate("Ui_MainWindow", "Nhà kính 4 tỷ"))
            self.User_name.setText     (_translate("Ui_MainWindow", "Đinh Thanh Tùng"))
            self.Control_btn.setText   (_translate("Ui_MainWindow", "Bảng điều khiển     "))
            self.Parameter_btn.setText (_translate("Ui_MainWindow", "Giám sát số liệu     "))
            self.Setting_btn.setText   (_translate("Ui_MainWindow", "Thiết lập hệ thống"))
            self.Properties_btn.setText(_translate("Ui_MainWindow", "Thông tin              "))
            self.Logout_btn.setText    (_translate("Ui_MainWindow", "Đăng xuất             "))
            Menu_btn_icon.addPixmap    (QtGui.QPixmap(":/LBlue_Icon/Icon_LBlue/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Menu_btn.setIcon      (Menu_btn_icon)
        else:
            newWidth = minWidth
            self.APP_name.setText      (_translate("Ui_MainWindow", ""))
            self.User_name.setText     (_translate("Ui_MainWindow", ""))
            self.Control_btn.setText   (_translate("Ui_MainWindow", ""))
            self.Parameter_btn.setText (_translate("Ui_MainWindow", ""))
            self.Setting_btn.setText   (_translate("Ui_MainWindow", ""))
            self.Properties_btn.setText(_translate("Ui_MainWindow", ""))
            self.Logout_btn.setText    (_translate("Ui_MainWindow", ""))
            Menu_btn_icon.addPixmap    (QtGui.QPixmap(":/LBlue_Icon/Icon_LBlue/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.Menu_btn.setIcon      (Menu_btn_icon)
            

        self.animation = QPropertyAnimation(self.Slide_menu, b"maximumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutBack)
        self.animation.start()
        
    def Select_Menu(self, tab):
        if(tab == 1):
            self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
            
            self.Control_btn.setStyleSheet(Control_btn_active)
            self.Parameter_btn.setStyleSheet(Parameter_btn_idle)
            self.Setting_btn.setStyleSheet(Setting_btn_idle)
            self.Properties_btn.setStyleSheet(Properties_btn_idle)
            
        if(tab == 2):
            self.Top_stackedWidget.setCurrentWidget(self.Top_ParameterPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ParameterPanel)
                               
            self.Control_btn.setStyleSheet(Control_btn_idle)
            self.Parameter_btn.setStyleSheet(Parameter_btn_active)
            self.Setting_btn.setStyleSheet(Setting_btn_idle)
            self.Properties_btn.setStyleSheet(Properties_btn_idle)
            
        if(tab == 3):
            self.Top_stackedWidget.setCurrentWidget(self.Top_SettingPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
                                           
            self.Control_btn.setStyleSheet(Control_btn_idle)
            self.Parameter_btn.setStyleSheet(Parameter_btn_idle)
            self.Setting_btn.setStyleSheet(Setting_btn_active)
            self.Properties_btn.setStyleSheet(Properties_btn_idle)
            
        if(tab == 4):
            self.Top_stackedWidget.setCurrentWidget(self.Top_SettingPanel)
            self.Bot_stackedWidget.setCurrentWidget(self.Bot_SettingPanel)
                                                       
            self.Control_btn.setStyleSheet(Control_btn_idle)
            self.Parameter_btn.setStyleSheet(Parameter_btn_idle)
            self.Setting_btn.setStyleSheet(Setting_btn_idle)
            self.Properties_btn.setStyleSheet(Properties_btn_active)



        
        
        

        

        
