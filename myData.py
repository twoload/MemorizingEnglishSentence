import pandas as pd
from myExcel import *

MAINPAGE_FILENAME = './mainPage.xlsx'
MAINPAGE_SHEETNAME = 'mainPage'

class mainPageDatabase:

    def __init__(self):
        self.df = pd.DataFrame([], columns=['date', 'title', 'sub'])
        self.init()

    def init(self):
        read_df = self.load()
        if read_df.empty:
            #print('read_df empty')
            self.create()
            return True
        else:
            #print('copy read_df into self.df')
            num_matched_column = self.df.columns.intersection(read_df.columns).size
            if num_matched_column == len(self.df.columns):
                self.df = read_df
                #print(self.df)
                return True
            else:
                print('not match column head')
                return False

    def create(self):
        print('mainPageDatabase create')
        dataframe2excel(self.df, MAINPAGE_FILENAME, MAINPAGE_SHEETNAME)

    def load(self):
        print('mainPageDatabase load: %s' % MAINPAGE_FILENAME)
        ret = excel2dataframe(MAINPAGE_FILENAME, MAINPAGE_SHEETNAME)
        return ret

    def print_data_lists_by_row(self):
        for row in range(len(self.df)):
            row_list = []
            for col in range(len(self.df.columns)):
                row_list.append(self.df.iloc[row][col])
            print(row_list)

    def get_data_frame(self):
        return self.df

    def add_empty_row(self, item):
        self.df.loc[len(self.df.index)] = []

    def remove_row(self, row_index):
        self.df.drop(self.df.index[row_index])

    def update_item(self, row_index, col_name, value):
        self.df.loc[row_index, [col_name]] = [value]
        #print(self.df)

    def save(self):
        dataframe2excel(self.df, MAINPAGE_FILENAME, MAINPAGE_SHEETNAME)

class subPageDatabase:

    def __init__(self):
        self.dataframes #= pd.DataFrame([], columns=['English', 'Korean'])
    def create(self, index):
        print('subPageDatabase %d create' % index)
        dataframe2excel(self.df, MAINPAGE_FILENAME, str(index))

    def sheetnames(self):
        xls = pd.ExcelFile(MAINPAGE_FILENAME)
        sheet_list = xls.sheet_names

    def load(self, excelfile):
        print('mainPageDatabase load: %s' % excelfile)
        self.df = excel2dataframe(excelfile, MAINPAGE_SHEETNAME)
        #print(self.df)

    def printDataListsByRow(self):
        for row in range(len(self.df)): #row
            row_list = []
            for col in range(len(self.df.columns)): #col
                row_list.append(self.df.iloc[row][col])
            print(row_list)

    def getDataFrame(self):
        return self.df

tc = mainPageDatabase()
tc.init()
tc.update_item(1, 'Date', 220701)