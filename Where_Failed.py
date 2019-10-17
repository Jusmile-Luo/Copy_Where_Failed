import pandas as pd
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dfModel import pandasModel

from Where_Units import Ui_Where_Units


#conn = pymssql.connect(host='10.206.158.21', user='ProdAdmin', password='ProdAdmin', database='Production', charset='utf8')
#db = pd.read_sql("select  * from RMATSwwrdbBI",con=conn)


db = pd.read_excel('C:/Users/jusmileluo/Documents/Project/SQL/TBFA.xlsx')

class Where_Failed_PN(QWidget):
    def __init__(self):
        super(Where_Failed_PN, self).__init__()
        self.ui = Ui_Where_Units()
        self.ui.setupUi(self)

        # 装载所有初始数据
        modeldf = pandasModel(db)
        self.ui.dataTable.setModel(modeldf)


        #在label上显示输入PN
        self.ui.PNedit.textEdited.connect(self.showText)
        input_text=self.ui.PNedit.sender()
        self.ui.PNlable.setText(input_text)

        #self.ui.PNedit.editingFinished.connect(self.enterText)
        self.ui.getBtn.clicked.connect(self.enterText)

    def showText(self,Text):
        self.ui.PNlable.setText(Text)
        self.ui.PNlable.adjustSize()

    def enterText(self):
        getText = self.ui.PNlable.text()
        print(getText)

        PNdata = db[(db['PartNum'] == str(getText))]
        print(PNdata)

        modeldf = pandasModel(PNdata)
        self.ui.dataTable.setModel(modeldf)
        return()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Where_Failed_PN()
    main.show()
    sys.exit(app.exec_())
