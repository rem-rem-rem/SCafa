'''
Created on 3 thg 5, 2022

@author: A315-56
'''
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import requests


os.system("pyuic5 -x Main.ui -o REM.py")

from REM import *
from style import *
from GUI_PyQt5_Func_1 import *

Counter = 0
     
class MAIN(Ui_MainWindow):
    def __init__(self, mainwindow):
        self.setupUi(mainwindow)

        self.Time_Start()



        # self.Ui_MainWindow.verticalSlider.valueChanged.connect(self.slide_it)
        
        self.Top_stackedWidget.setCurrentWidget(self.Top_ControlPanel)
        self.Bot_stackedWidget.setCurrentWidget(self.Bot_ControlPanel)
        self.Control_btn.setStyleSheet(Control_btn_active)

        self.slider_setting()

        #================ ĐÂT ======================

        self.verticalSlider_3.valueChanged.connect(self.slide_it)
        self.verticalSlider_4.valueChanged.connect(self.slide_it_nhiet_do)
        self.verticalSlider_6.valueChanged.connect(self.slide_it_PH)

        #================ không khí =================

        self.Top_Ctrl_frame2_body_do_am_vertical.valueChanged.connect(self.slide_it_do_am_kk)
        self.Top_Ctrl_frame2_body_nhiet_do_vertical.valueChanged.connect(self.slide_it_nhiet_do_kk)
        self.Top_Ctrl_frame2_body_nong_do_O2_vertical.valueChanged.connect(self.slide_it_PH_kk)

        #=================== Lux ======================

        self.Top_Ctrl_frame3_body_lux_vertical.valueChanged.connect(self.slide_it_LUX)

        #=================== Wh =======================

        self.Top_Ctrl_frame4_body_Wh_vertical.valueChanged.connect(self.slide_it_WH)

        #=================== không khí ================
        self.weather()

        self.verticalSlider_2.valueChanged.connect(self.PH)

        self.Menu_btn.clicked.connect(lambda: UIFunctions.ToggleMenu      (self, 50, 250))
        self.Control_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 1))
        self.Parameter_btn.clicked.connect(lambda: UIFunctions.Select_Menu(self, 2))
        self.Setting_btn.clicked.connect(lambda: UIFunctions.Select_Menu  (self, 3))

    def slider_setting(self):
        self.verticalSlider_3.setMinimum(0)
        self.verticalSlider_3.setMaximum(100)
        self.verticalSlider_4.setMinimum(0)
        self.verticalSlider_4.setMaximum(100)
        self.verticalSlider_6.setMinimum(0)
        self.verticalSlider_6.setMaximum(100)
        self.verticalSlider_2.setMinimum(0)
        self.Top_Ctrl_frame2_body_do_am_vertical.setMinimum(0)
        self.Top_Ctrl_frame2_body_do_am_vertical.setMaximum(100)
        self.Top_Ctrl_frame2_body_nhiet_do_vertical.setMinimum(0)
        self.Top_Ctrl_frame2_body_nhiet_do_vertical.setMaximum(100)
        self.Top_Ctrl_frame2_body_nong_do_O2_vertical.setMinimum(0)
        self.Top_Ctrl_frame2_body_nong_do_O2_vertical.setMaximum(100)
        self.Top_Ctrl_frame3_body_lux_vertical.setMinimum(0)
        self.Top_Ctrl_frame3_body_lux_vertical.setMaximum(100)
        self.Top_Ctrl_frame4_body_Wh_vertical.setMinimum(0)
        self.Top_Ctrl_frame4_body_Wh_vertical.setMaximum(100)
        self.verticalSlider_2.setMinimum(0)
        self.verticalSlider_2.setMaximum(611)

#=========================================================================== TIMER =================================================================================

    def Time_Start(self):
        self.time = QtCore.QTimer()
        self.time.start(1000)
        self.time.timeout.connect(self.timer_Wh)

#============================================================================ ĐẤT ==================================================================================
    def progressBarValue(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0
        
        progress = (100-value)
        # Láy giá trị mới
        # stop_1 = str(progress - 0.001)
        # stop_2 = str(progress)

        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.label_29.setStyleSheet(newStylsheet)

    def slide_it(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.verticalSlider_3.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue(100 - int(value))
        self.label_31.setText(newRem)

    def progressBarValue_PH(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value)
        # Láy giá trị mới
        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.label_39.setStyleSheet(newStylsheet)

    def slide_it_PH(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.verticalSlider_6.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_PH(100 - int(value))
        self.label_35.setText(newRem)

    def progressBarValue_nhiet_do(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value)
        # Láy giá trị mới
        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.label_33.setStyleSheet(newStylsheet)

    def slide_it_nhiet_do(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.verticalSlider_6.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_nhiet_do(100 - int(value))
        self.label_34.setText(newRem)

#============================================================================ Không khí ==================================================================================

    def progressBarValue_do_am_kk(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value)
        # Láy giá trị mới
        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.Top_Ctrl_frame2_body_do_am_1.setStyleSheet(newStylsheet)

    def slide_it_do_am_kk(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.Top_Ctrl_frame2_body_do_am_vertical.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_do_am_kk(100 - int(value))
        self.Top_Ctrl_frame2_body_do_am_4.setText(newRem)

    def progressBarValue_nhiet_do_kk(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value)
        # Láy giá trị mới
        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.Top_Ctrl_frame2_body_nhiet_do_1.setStyleSheet(newStylsheet)

    def slide_it_nhiet_do_kk(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.Top_Ctrl_frame2_body_nhiet_do_vertical.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_nhiet_do_kk(100 - int(value))
        self.Top_Ctrl_frame2_body_nhiet_do_4.setText(newRem)

    def progressBarValue_PH_kk(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:110px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(0, 0, 42, 255), stop:{STOP_2} rgba(0, 0, 42, 0))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value)
        # Láy giá trị mới
        stop_1 = str(0.876423 - 0.0074707*progress)
        stop_2 = str(0.878799 - 0.0074707*progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.Top_Ctrl_frame2_body_nong_do_O2_1.setStyleSheet(newStylsheet)

    def slide_it_PH_kk(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.Top_Ctrl_frame2_body_nong_do_O2_vertical.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_PH_kk(100 - int(value))
        self.Top_Ctrl_frame2_body_nong_do_O2_4.setText(newRem)

#============================================================================ LUX ==================================================================================

    def progressBarValue_LUX(self, value):
        #biểu diễn thanh tiến trình
        styleSheet = """
            border-radius:125px;
            background-color:  qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(0, 0, 42, 0), stop:{STOP_2} rgba(0, 0, 42, 255))
        """
        #láy giá trị của thanh tiến trình, chuyển đổi nó thành kiểu FLOAT
        # dừng giá trị từ 1 đến 0

        progress = (100 - value) / 100.0
        # Láy giá trị mới
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        #Ungứ dụng giá trị mới vào styleSheet
        self.Top_Ctrl_frame3_body_lux_4.setStyleSheet(newStylsheet)

    def slide_it_LUX(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.Top_Ctrl_frame2_body_nong_do_O2_vertical.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_LUX(100 - int(value))
        self.Top_Ctrl_frame3_body_lux_3.setText(newRem)

#=========================================================================== WH =============================================================================================

    def progressBarValue_WH(self, value):
  
        styleSheet_rem = """
           border-radius: 115px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1_1} rgba(0, 0, 42, 0), stop:{STOP_2_2} rgba(255, 0, 0, 255), stop:{STOP_3_3} rgba(255, 0, 0, 255), stop:{STOP_4_4} rgba(0, 0, 42, 0));
        """

        # dừng giá trị từ 1 đến 0
        progress = (value)
        # Láy giá trị mới

        stop_1_1 = str(0.791045 - 0.00597015*progress)
        stop_2_2 = str(0.797098 - 0.00597015*progress)
        stop_3_3 = str(0.803044 - 0.00597015*progress)
        stop_4_4 = str(0.806767 - 0.00597015*progress)

        print("stop_1_1 = ", stop_1_1)


        #Đặc giá trị đó vào cái STYLESHEET mới
        newStylsheet_rem = styleSheet_rem.replace("{STOP_1_1}", stop_1_1).replace("{STOP_2_2}", stop_2_2).replace("{STOP_3_3}",stop_3_3).replace("{STOP_4_4}",stop_4_4)

        #Ungứ dụng giá trị mới vào styleSheet
 
        self.Top_Ctrl_frame4_body_Wh_4.setStyleSheet(newStylsheet_rem)

    def slide_it_WH(self, value):
        Rem =""" <p><span style=" font-size:28pt; color:#ffffff;">{VALUE}</span><span style=" font-size:28pt;color:#ffffff; vertical-align:super;">%</span></p>"""
        print(self.Top_Ctrl_frame4_body_Wh_vertical.value())
        newRem = Rem.replace("{VALUE}", str(value))
        self.progressBarValue_WH(int(value))
        self.Top_Ctrl_frame4_body_Wh_1.setText(newRem)

    def timer_Wh(self):
        global Counter

        if Counter > 100000:
            Counter = 0
        Counter += 1
        if Counter <= 10:
            self.Top_Ctrl_frame4_body_metter.setText("00000"+str(Counter))
        elif Counter > 10 and Counter <= 100:
            self.Top_Ctrl_frame4_body_metter.setText("0000"+str(Counter))
        elif Counter > 100 and Counter <= 1000:
            self.Top_Ctrl_frame4_body_metter.setText("000"+str(Counter))
        elif Counter > 1000 and Counter <= 10000:
            self.Top_Ctrl_frame4_body_metter.setText("0"+str(Counter))
        elif Counter > 10000 and Counter <= 100000:
            self.Top_Ctrl_frame4_body_metter.setText(str(Counter))

#=========================================================================================== thời tiết ================================================================================

    def weather(self):
        # api_address='http://api.openweathermap.org/data/2.5/weather?q=bienhoa&appid=59e434bde2d8ff7f30cfdb363d79aa61'
        api_address='https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=59e434bde2d8ff7f30cfdb363d79aa61&lang=vi'
        json_data = requests.get(api_address).json()
        format_add = json_data['main']

        rem = json_data['main']['humidity']
        ram = json_data['weather'][0]['description']

        # for i,j in enumerate(ram):
        #     print(i,j)
        print("rem",ram)
        self.label_47.setText(ram)
        if json_data['weather'][0]['icon'] == '04d':
            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("../image/nhieu_may-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon10)

            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("../image/nang_-_Copy-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)




        #print(json_data)
        print("Thời Tiết thì  {0} Nhiệt độ thấp nhất là {1} Nhiệt độ cao nhất là {2} Độ C".format(
            json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-273)))



    def PH(self, value):
        x = (62/61)*value + (2400/61)
        self.p2.setGeometry(QtCore.QRect(x, 140, 91, 81))
        self.p1.setGeometry(QtCore.QRect(x+60, 150, 101, 71))
        test = "ĐỘ PH: " + str(x/(305/7))
        self.p1.setText(test)
