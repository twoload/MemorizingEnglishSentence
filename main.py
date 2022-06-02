import pandas as pd

def inputSubTitlePage():
    pass

def inputMainPage():
    mainPage = pd.read_excel('mainPage.xlsx')
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
            index = int(input())

        elif choose == 5:
            mainPage.to_excel('./mainPage.xlsx')
            pass
        elif choose == 0:
            break
        else:
            print("wrong input")

    return

    '''
    df = pd.DataFrame(
        {
            'date': ['220601',
                       '220602',
                       '220603'],
            'title': ['Oxford Reading Tree',
                         'Oxford Reading Tree',
                         'Daisy'],
            'subTitle': ['Tip Top',
                           'Watch Your Step',
                           'Book1']
        }
    )
    df.to_excel('./mainPage.xlsx')
    '''
    return

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
    showMainMenu()

if __name__ == "__main__":
    main()