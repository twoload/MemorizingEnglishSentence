import pandas as pd

def inputEnglishSentences():
    mainPage = pd.read_excel('mainPage.xlsx')
    print(mainPage)

    choose = 0
    while 1:
        print("==========================")
        print("Input Page")
        print("==========================")
        print("1.add")
        print("2.remove")
        print("3.display")
        print("0.exit")
        print("==========================")
        print("choose>")
        choose = int(input())

        if choose == 1:
            pass
        elif choose == 2:
            pass
        elif choose == 3:
            print(mainPage)
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
            inputEnglishSentences()
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