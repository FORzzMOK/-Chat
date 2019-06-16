#!python2
#!-*-coding: utf-8-*-

import sys
from threading import Thread
from PyQt4 import QtGui, QtCore
from Safe import Tooltip

app = QtGui.QApplication(sys.argv)#создает объект приложения
tooltip = Tooltip()#Создает экземпляр класса

def SendTextToBrowser():
	messedge = tooltip.textEdit.toPlainText()
	tooltip.textEdit.clear()
	tooltip.textBrowser.append(messedge)

def StartWidget():
	tooltip.show()#show() отображает наше окно на экране
	tooltip.pushButton.clicked.connect(SendTextToBrowser)
	app.exec_()#основной цикл нашей программы. Обработка сообщений начинается с этой строчки

thread_1 = Thread(target=StartWidget, args=())
thread_1.start()
