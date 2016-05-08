import sys
from Todotter_ui import *
from Todotter_api import *



class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.listWidget.item(0).setText(_translate("Dialog", "tanomu", None))
    def add(self,text):
        self.ui.addList(text)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    api = Stream(myapp)
    api.start()
    sys.exit(app.exec_())

