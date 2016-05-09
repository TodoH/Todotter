# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Todotter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Todotter_api import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    tl_items = [[]]
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(840, 480)
        Dialog.setMaximumSize(QtCore.QSize(840, 25600))
        Dialog.setMouseTracking(False)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 840, 480))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setStyleSheet(_fromUtf8("selection-color: rgb(0, 0, 0);"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(0, 38, 840, 441))
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 9);\n"
"border-color: rgb(61, 61, 61);\n"
""))
        self.listWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget.setLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QtGui.QListView.Free)
        self.listWidget.setFlow(QtGui.QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget.setLayoutMode(QtGui.QListView.Batched)
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setBatchSize(100)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        # self.listWidget.addItem(item)

        self.textEdit_6 = QtGui.QTextEdit(self.tab)
        self.textEdit_6.setGeometry(QtCore.QRect(0, 20, 18, 21))
        self.textEdit_6.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit_6.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 9);"))
        self.textEdit_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setOverwriteMode(False)
        self.textEdit_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(self.tab)
        self.textEdit_7.setGeometry(QtCore.QRect(0, 0, 840, 20))
        self.textEdit_7.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit_7.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 9);"))
        self.textEdit_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setOverwriteMode(False)
        self.textEdit_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        # self.tweetedit = QtGui.QTextEdit(self.tab)
        self.tweetedit = TweetEdit(self.tab)


        self.tweetedit.setGeometry(QtCore.QRect(18, 20, 822, 21))
        self.tweetedit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tweetedit.setStyleSheet(_fromUtf8("color: rgb(0, 255, 9);\n"
"background-color: rgb(0, 0, 0);"))
        self.tweetedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tweetedit.setObjectName(_fromUtf8("tweetedit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textEdit_2 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 840, 441))
        self.textEdit_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 9);"))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setOverwriteMode(True)
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 440, 18, 21))
        self.textEdit_3.setFocusPolicy(QtCore.Qt.TabFocus)
        self.textEdit_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 9);"))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(False)
        self.textEdit_3.setOverwriteMode(True)
        self.textEdit_3.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(self.tab_2)
        self.textEdit_4.setGeometry(QtCore.QRect(18, 440, 822, 21))
        self.textEdit_4.setStyleSheet(_fromUtf8("color: rgb(0, 255, 9);\n"
"background-color: rgb(0, 0, 0);"))
        self.textEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # self.listWidget.item(0).setText(_translate("Dialog", "account1(@id1):tweet1", None))


        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textEdit_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">New Tweet</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "userA", None))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please input UserID</p></body></html>", None))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "AddUser", None))

    def addList(self, item):
        self.tl_items.append([])
        self.item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)

        print(self.listWidget.__len__())
        # self.listWidget.item(self.listWidget.__len__() - 1).setText(_translate("Dialog", text, None))
        self.listWidget.item(self.listWidget.__len__() - 1).set

    #
    # def keyPressEvent(self, qKeyEvent):
    #     print(qKeyEvent.key())
    #     if qKeyEvent.key() == QtCore.Qt.Key_Return:
    #         print('Enter pressed')
    #     else:
    #         super().keyPressEvent(qKeyEvent)

    #
    # def eventFilter(self, source, event):
    #     if (event.type() == QtCore.QEvent.KeyPress
    #         and source is self.tweetedit
    #         and event.key() == QtCore.Qt.Key_Return):
    #         # key = event.key()
    #         # pos = event.pos()
    #         # print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
    #         # if key == QtCore.Qt.Key_Enter:
    #         print("bb")
    #         return (True)
    #     else:
    #         return (False)
    #         # return QtGui.QWidget.eventFilter(self, source, event)
    #

class TweetEdit(QtGui.QTextEdit):
    def __init__(self, *args):
        QtGui.QTextEdit.__init__(self, *args)
    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Return:
            text = (self.toPlainText())
            self.setText("")
            Twitter().tweet(text)
        # つぶやきにどうやって 番号を付加しようかな
        # objectごと受け取って抜き出しもこっちでやろうかな。
        else:
            super().keyPressEvent(event)

    #
    # def eventFilter(self, source, event):
    #
    #     if (event.type() == QtCore.QEvent.KeyPress
    #         and event.key() == QtCore.Qt.Key_Return):
    #         # key = event.key()
    #         # pos = event.pos()
    #         # print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
    #         # if key == QtCore.Qt.Key_Enter:
    #         print("bb")
    #         return(True)
    #     else:
    #         return(False)
    #     # return QtGui.QWidget.eventFilter(self, source, event)
