#sử dụng run để chạy nhưngx trương trình muốn sử lý liên kết giữa các file với nhai

# from turtle import title thư viên đồ họa con rùa

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import*
import imp
from load import LOGIN_Main
from main import MAIN
import sys



class UI():#biến sử dụng trong class thì phải có self đầu tiên
    def __init__(self) :
        self.login_uic = QMainWindow()
        self.login = LOGIN_Main(self.login_uic)
        self.login_uic.show()
        self.login.EnterButton.clicked.connect(lambda: self.changeUI("main"))#sử lý sự kiện cho nút login
        # từ login chuyển sang main thì truyền trong cái self,.changUI một tham số muốn truyền qua
        # self.main = MAIN()
        self.main_uic = QMainWindow()
        self.main = MAIN(self.main_uic)
        self.main.Login_return.clicked.connect(lambda: self.changeUI("load"))

    def changeUI(self, i):
        if i == "main":#nếu tham số truyền vào là main thì load main lên ẩn login đi
            self.main.UserName = self.login.User.text()
            self.login_uic.hide()
            self.main_uic.show()
            self.main.label.setText("%s"%self.main.UserName)

        elif i == "load":
            self.main_uic.hide()
            self.login_uic.show()
    # LOGIN 



if __name__ == "__main__":
    app =  QApplication([])
    app.setWindowIcon(QIcon("D:/qt5/rem/image/TR.jpg"))
    ui = UI()
    app.exec_()

