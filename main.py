import pandas as pd
from openpyxl import load_workbook

def isWorkSheet(excelname, worksheet):
    wb = load_workbook(excelname, read_only=True)
    if worksheet in wb.sheetnames:
        #print(f'exist {worksheet}')
        return True
    else:
        #print(f'no exist {worksheet}')
        return False

def inputSubTitlePage(index):
    if isWorkSheet('mainPage.xlsx', str(index)):
        subPage = pd.read_excel('mainPage.xlsx', str(index))
    else:
        subPage = pd.to_excel('./mainPage.xlsx', sheet_name=str(index))
    print(subPage)
    while 1:
        print("==========================")
        print(f'Edit Contents ({str(index)})')
        print("==========================")
        print("1.add")
        print("2.remove")
        print("3.display")
        print("4.edit contents")
        print("5.save to excel")
        print("0.exit")
        print("==========================")
        print("choose>")
        choose = int(input())

        if choose == 1: #add
            print('input English >')
            english = input()
            print('input Korean >')
            korean = input()
            subPage.loc[len(subPage.index)] = [english, korean]
            print(subPage)
        elif choose == 2: #remove
            print("choose index to remove>")
            index = int(input())
            subPage = subPage.drop(subPage.index[index])
            print(subPage)
        elif choose == 3: #display
            print(subPage)
        elif choose == 4: #edit
            print(subPage)
            print("edit index to edit>")
            index = int(input())
            print(subPage.loc[[index]])
            print("Do you want to change English? > (y/n)")
            ans = input()
            if ans == 'y':
                print('input English>')
                english = input()
            print("Do you want to change Korean? > (y/n)")
            ans = input()
            if ans == 'y':
                print('input Korean>')
                korean = input()
            subPage.loc[[index]] = [english, korean]
            print(subPage)
        elif choose == 5: #save to excel
            subPage.to_excel('./mainPage.xlsx', sheet_name=str(index))
        elif choose == 0:
            break
        else:
            print('wrong input')


def inputMainPage():
    mainPage = pd.read_excel('mainPage.xlsx', 'mainPage')
    print(mainPage)

    choose = 0
    while 1:
        print("==========================")
        print("Edit Title")
        print("==========================")
        print("1.add")
        print("2.remove")
        print("3.display")
        print("4.edit sub title")
        print("5.save to excel")
        print("0.exit")
        print("==========================")
        print("choose>")
        choose = int(input())

        if choose == 1:
            print("input date(ex.220501)")
            date = input()
            print("input title(ex.Oxford Reading Tree)")
            title = input()
            print("input subTitle(ex.book1)")
            subTitle = input()
            mainPage.loc[len(mainPage.index)] = [date, title, subTitle]
            print(mainPage)

        elif choose == 2:
            print("choose index to remove>")
            index = int(input())
            mainPage = mainPage.drop(mainPage.index[index])
            print(mainPage)
        elif choose == 3:
            print(mainPage)
        elif choose == 4:
            print(mainPage)
            print('choose index>')
            index = int(input())
            inputSubTitlePage(index)
        elif choose == 5:
            mainPage.to_excel('./mainPage.xlsx', sheet_name='mainPage')
            pass
        elif choose == 0:
            break
        else:
            print("wrong input")

    return

def showWelcome():
    print("==========================")
    print(' Welcome to M.E.S')
    print("==========================")

def showMainMenu():
    while 1:
        numMainMenu = 0
        print("==========================")
        print(" Main Menu ")
        print("==========================")
        print("1.input English sentences")
        print("2.upload answers (excel files)")
        print("3.study")
        print("0.exit")
        print("==========================")
        print("choose number > ")
        numMainMenu = int(input())

        if numMainMenu == int(1):
            inputMainPage()
            pass
        elif numMainMenu == int(2):
            pass
        elif numMainMenu == int(3):
            pass
        elif numMainMenu == int(0):
            break
        else:
            print("wrong number")

    return


def main():
    showWelcome()
    showMainMenu()

if __name__ == "__main__":
    main()