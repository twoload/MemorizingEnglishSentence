import sys
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5 import uic
from myExcel import *
from myPdf import *
from myData import mainPageDatabase
import numpy as np
import time

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
        self.button_main_prev.clicked.connect(self.HandlerButton_Main_Prev)
        self.button_main_next.clicked.connect(self.HandlerButton_Main_Next)
        self.button_sub_add.clicked.connect(self.HandlerButton_Sub_Add)
        self.button_sub_remove.clicked.connect(self.HandlerButton_Sub_Remove)
        self.button_sub_save.clicked.connect(self.HandlerButton_Sub_Save)
        self.button_sub_prev.clicked.connect(self.HandlerButton_Sub_Prev)
        self.button_sub_next.clicked.connect(self.HandlerButton_Sub_Next)
        self.button_study.clicked.connect(self.HandlerButton_Study)

        self.tableWidget_main.itemChanged.connect(self.HandlerMainItem_Changed)

        # main table init display
        self.df_main_class = mainPageDatabase()
        if not self.df_main_class.df.empty:
            df_main_numpy = self.df_main_class.df.to_numpy()
            rows, columns = df_main_numpy.shape
            #print(rows, columns)
            for row_index in range(rows):
                # insert row
                self.tableWidget_main.insertRow(self.tableWidget_main.rowCount())
                for col_index in range(columns): # skip index row
                    item = df_main_numpy[row_index, col_index]
                    #print(row_index, col_index, item)
                    self.tableWidget_main.setItem(row_index, col_index, QTableWidgetItem(str(item)))

        print(self.df_main_class.df)
        '''
        print('tableWidget_main col num: %d' %(self.tableWidget_main.columnCount()))
        print('tableWidget_main row num: %d' %(self.tableWidget_main.rowCount()))
        for i in range(0, rowcount):
            for j in range(0, colcount):
                data = self.tableWidget.item(i, j)
        '''

        #layout = QVBoxLayout()
        #layout.addWidget(self.tableWidget)
        #self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()
        #sub table init display

    # inner function

    # Event
    def HandlerButton_Main_Add(self):
        #print("button_main_add Clicked")
        selectionModel = self.tableWidget_main.selectionModel()
        if not selectionModel.hasSelection():
            self.tableWidget_main.insertRow(self.tableWidget_main.rowCount())
        else:
            for index in selectionModel.selectedIndexes():
                self.tableWidget_main.insertRow(index.row())

    def HandlerButton_Main_Remove(self):
        print("button_main_remove Clicked")
        selectionModel = self.tableWidget_main.selectionModel()
        if not selectionModel.hasSelection():
            self.tableWidget_main.removeRow(self.tableWidget_main.rowCount() - 1)
            # update dataframe
            self.df_main_class.remove_row(self.tableWidget_main.rowCount() - 1)
        else:
            for index in selectionModel.selectedIndexes():
                self.tableWidget_main.removeRow(index.row())
                # update dataframe
                self.df_main_class.remove_row(index.row())


    def HandlerButton_Main_Save(self):
        print("button_main_save Clicked")
        self.df_main_class.save()

    def HandlerButton_Main_Prev(self):
        print("button_main_prev Clicked")
        scrollBar = self.tableWidget_main.verticalScrollBar()
        scrollBar.setValue(scrollBar.value() - scrollBar.pageStep())

    def HandlerButton_Main_Next(self):
        print("button_main_next Clicked")
        scrollBar = self.tableWidget_main.verticalScrollBar()
        scrollBar.setValue(scrollBar.value() + scrollBar.pageStep())

    def HandlerMainItem_Changed(self, item):
        #print('HandlerMainItem_Changed (%d %d)' %(item.row(), item.column()))
        data = self.tableWidget_main.item(item.row(), item.column())
        col_label = self.tableWidget_main.horizontalHeaderItem(item.column()).text()
        #print('changed : (%d %s %s)' %(item.row(), col_label, data.text()))
        self.df_main_class.update_item(item.row(), col_label, data.text())
        #print(self.df_main_class.df)

    def HandlerButton_Sub_Add(self):
        print("button_sub_add Clicked")
        selectionModel = self.tableWidget_sub.selectionModel()
        if not selectionModel.hasSelection():
            self.tableWidget_sub.insertRow(self.tableWidget_sub.rowCount())
        else:
            for index in selectionModel.selectedIndexes():
                self.tableWidget_sub.insertRow(index.row())

    def HandlerButton_Sub_Remove(self):
        print("button_sub_remove Clicked")
        selectionModel = self.tableWidget_sub.selectionModel()
        if not selectionModel.hasSelection():
            self.tableWidget_sub.removeRow(self.tableWidget_sub.rowCount() - 1)
        else:
            for index in selectionModel.selectedIndexes():
                self.tableWidget_sub.removeRow(index.row())

    def HandlerButton_Sub_Save(self):
        print("button_sub_save Clicked")

    def HandlerButton_Sub_Prev(self):
        print("button_sub_prev Clicked")
        scrollBar = self.tableWidget_sub.verticalScrollBar()
        scrollBar.setValue(scrollBar.value() - scrollBar.pageStep())

    def HandlerButton_Sub_Next(self):
        print("button_sub_next Clicked")
        scrollBar = self.tableWidget_sub.verticalScrollBar()
        scrollBar.setValue(scrollBar.value() + scrollBar.pageStep())

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