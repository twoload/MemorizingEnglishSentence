import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic
from main import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("mainPage.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 연결하는 코드
        self.button_main_add.clicked.connect(self.HandlerButton_Main_Add)
        self.button_main_remove.clicked.connect(self.HandlerButton_Main_Remove)
        self.button_main_save.clicked.connect(self.HandlerButton_Main_Save)
        self.button_sub_add.clicked.connect(self.HandlerButton_Sub_Add)
        self.button_sub_remove.clicked.connect(self.HandlerButton_Sub_Remove)
        self.button_sub_save.clicked.connect(self.HandlerButton_Sub_Save)
        self.button_sub_load.clicked.connect(self.HandlerButton_Sub_Load)
        self.button_study.clicked.connect(self.HandlerButton_Study)

        #main table init display
        #sub table init display

    def HandlerButton_Main_Add(self):
        print("button_main_add Clicked")

    def HandlerButton_Main_Remove(self):
        print("button_main_remove Clicked")

    def HandlerButton_Main_Save(self):
        print("button_main_save Clicked")

    def HandlerButton_Sub_Add(self):
        print("button_sub_add Clicked")

    def HandlerButton_Sub_Remove(self):
        print("button_sub_remove Clicked")

    def HandlerButton_Sub_Save(self):
        print("button_sub_save Clicked")

    def HandlerButton_Sub_Load(self):
        print("button_sub_load Clicked")

    def HandlerButton_Study(self):
        print("button_study Clicked")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()