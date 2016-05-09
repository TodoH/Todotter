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
    # def keyPressEvent(self, event):


# class TweetEdit(QtGui.QTextEdit):
#     def __init__(self, *args):
#         QtGui.QTextEdit.__init__(self, *args)
#
#     def keyPressEvent(self, event):
#         key = event.key()
#         if key == QtCore.Qt.Key_C:
#             print("bb")



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    api = Stream(myapp)
    api.setDaemon(True)
    api.start()
    sys.exit(app.exec_())
