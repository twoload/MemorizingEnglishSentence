# MemorizingEnglishSentence
## Libraries
* pandas  
to read from excel  
to write to excel
* fpdf  
to create pdf  
* Korean ttf  
when creating pdf, Korean encoding is needed  
* anaconda  
convenient install considering dependency  
* PyQt5  
for GUI in python  

## WebPages  
* git push not updating files although changes have been made  
https://stackoverflow.com/questions/43505518/git-push-not-updating-files-although-changes-have-been-made  
* PyQt Korean Tutorial 
https://wikidocs.net/35477

## Error  
* No module named pandas  
pip install --upgrade pandas  
pip install pandas  
* excel column text : lowercase  
** horizontalHeaderItem.text() : lowercase  
* to_excel : index = False  
** index column will be skipped  
* data doesn't show up even though setItem in qtTableWidget.  
** row.append is needed  
*
