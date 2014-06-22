# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HCgui.ui'
#
# Created: Fri May 16 00:31:49 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import pydot

import huff_algorithm

from PyQt4 import QtCore, QtGui

#global filedata
#global filename

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SourceTextEdit(QtGui.QTextEdit):
	@QtCore.pyqtSlot()
  	def slotTextChanged(self): #
		print self.toPlainText() + "\nSRC_Signal"   	
	#@QtCore.pyqtSlot()
  	#def generateHCBinTree(self): 
	#	print "Generating BT..."
	#	NodeStorage = huff_algorithm.TBinTree_NodeGenerator(str(self.toPlainText()))
	#	NodeStorage.SortData()
	#	#Grader.DictPrint()
	#	NodeStorage.ListPrint()
	#	NodeStorage.SortedLeafGen()
	#	#print Grader.GetNodeList()
	#	Generator = huff_algorithm.TBinTree_Tree(NodeStorage)
		

class MessageTextEdit(QtGui.QTextEdit):
	@QtCore.pyqtSlot()
  	def slotTextChanged(self): 
		print self.toPlainText() + "\nMSG_Signal"

class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
	self.filename1_Src = str()
	self.filename2_Msg = str()
	self.Generator = None

    def setupUi(self, MainWindow):
	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1180, 840)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

	
        self.leftFrame = QtGui.QFrame(self.centralwidget)
        self.leftFrame.setGeometry(QtCore.QRect(10, 10, 232, 740))
        self.leftFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.leftFrame.setObjectName(_fromUtf8("frame"))
	
	self.innerLeftWidget = QtGui.QWidget(self.leftFrame)
	self.innerLeftWidget.setGeometry(QtCore.QRect(10, 10, 232, 720))

################################################################################
###### Toolbox page 1
################################################################################

        self.page = QtGui.QWidget(self.innerLeftWidget)
        self.page.setGeometry(QtCore.QRect(10, 10, 190, 440))
        self.page.setObjectName(_fromUtf8("page"))

        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 180, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.textEdit1_Src = SourceTextEdit(self.page)
        self.textEdit1_Src.setGeometry(QtCore.QRect(0, 30, 190, 140))
        self.textEdit1_Src.setObjectName(_fromUtf8("textEdit"))
	self.textEdit1_Src.connect(self.textEdit1_Src,QtCore.SIGNAL("textChanged()"),self.textEdit1_Src,QtCore.SLOT("slotTextChanged()"))

        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(0, 180, 190, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.comboBox = QtGui.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(0, 230, 190, 30))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
	self.comboBox.addItem(_fromUtf8("Top-down method"))
        self.comboBox.addItem(_fromUtf8("Bottom-up method"))

	self.pushButton_3 = QtGui.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 270, 190, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(0, 320, 100, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))

	self.lcdNumber = QtGui.QLCDNumber(self.page)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 340, 75, 20))
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.001)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))

	self.label_9 = QtGui.QLabel(self.page)
        self.label_9.setGeometry(QtCore.QRect(85, 320, 100, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))

	self.lcdNumber_2 = QtGui.QLCDNumber(self.page)
        self.lcdNumber_2.setGeometry(QtCore.QRect(85, 340, 75, 20))
        self.lcdNumber_2.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_2.setLineWidth(2)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 0.001)
        self.lcdNumber_2.setProperty("intValue", 0)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))

	self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(0, 365, 110, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))

	self.lcdNumber_3 = QtGui.QLCDNumber(self.page)
        self.lcdNumber_3.setGeometry(QtCore.QRect(0, 385, 75, 20))
        self.lcdNumber_3.setFrameShape(QtGui.QFrame.Box)
        self.lcdNumber_3.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdNumber_3.setLineWidth(2)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_3.setProperty("value", 0.001)
        self.lcdNumber_3.setProperty("intValue", 0)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))

	self.checkbox_2 = QtGui.QCheckBox(self.page)
	self.checkbox_2.setGeometry(QtCore.QRect(0, 410, 21, 21))
	self.checkbox_2.setObjectName(_fromUtf8("checkbox_2"))
	
	self.label_11 = QtGui.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(30, 410, 160, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.line = QtGui.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(0, 430, 190, 20))
	self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

	

################################################################################
###### Toolbox page 2
################################################################################

        self.page_2 = QtGui.QWidget(self.innerLeftWidget)
        self.page_2.setGeometry(QtCore.QRect(10, 460, 190, 330))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        
	self.label_4 = QtGui.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 180, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
	
        self.pushButton_2 = QtGui.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 180, 190, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))

	self.textEdit3_Msg = MessageTextEdit(self.page_2)
        self.textEdit3_Msg.setGeometry(QtCore.QRect(0, 30, 190, 140))
        self.textEdit3_Msg.setObjectName(_fromUtf8("textEdit_3"))
 	self.textEdit3_Msg.connect(self.textEdit3_Msg,QtCore.SIGNAL("textChanged()"),self.textEdit3_Msg,QtCore.SLOT("slotTextChanged()"))
	
	self.label_7 = QtGui.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(25, 230, 180, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))

	self.checkbox = QtGui.QCheckBox(self.page_2)
	self.checkbox.setGeometry(QtCore.QRect(0, 230, 21, 21))
	self.checkbox.setObjectName(_fromUtf8("checkbox"))

	#self.toolBox.addItem(self.page_2, _fromUtf8(""))


################################################################################
#	TAB OBJECT
#	
#
##########

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(254, 10, 910, 740))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

################################################################################
###### TAB page 1
################################################################################

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(14, 14, 180, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(14, 38, 180, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.textEdit2_Srclist = QtGui.QTextEdit(self.tab)
        self.textEdit2_Srclist.setGeometry(QtCore.QRect(14, 66, 170, 622))
        self.textEdit2_Srclist.setObjectName(_fromUtf8("textEdit_2"))
	self.textEdit2_Srclist.setReadOnly(True)

	self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(198, 14, 180, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))

      	self.textEdit4_Msgcoded = QtGui.QTextEdit(self.tab)
        self.textEdit4_Msgcoded.setGeometry(QtCore.QRect(198, 66, 350, 200))
        self.textEdit4_Msgcoded.setObjectName(_fromUtf8("textEdit_4"))
	self.textEdit4_Msgcoded.setReadOnly(True)

	self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(198, 276, 180, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))

      	self.textEdit5_decoded = QtGui.QTextEdit(self.tab)
        self.textEdit5_decoded.setGeometry(QtCore.QRect(198, 322, 350, 180))
        self.textEdit5_decoded.setObjectName(_fromUtf8("textEdit_5"))
	self.textEdit5_decoded.setReadOnly(True)
	#self.textEdit2_Srclist.connect(self.textEdit1_Src,QtCore.SIGNAL("textChanged()"),self.textEdit1_Src,QtCore.SLOT("slotTextChanged()"))

################################################################################
###### TAB page 2
################################################################################
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

	self.picture = QtGui.QPixmap("")
	self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
	self.scrollArea.setGeometry(QtCore.QRect(14, 14, 880, 674))

	self.graphicsView = QtGui.QLabel(self.scrollArea)
        self.graphicsView.setBackgroundRole(QtGui.QPalette.Base)
	self.graphicsView.setPixmap(self.picture)
        self.graphicsView.setSizePolicy(QtGui.QSizePolicy.Ignored,
	        QtGui.QSizePolicy.Ignored)
        self.graphicsView.setScaledContents(True)	

        self.scrollArea.setWidget(self.graphicsView)
	self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        MainWindow.setCentralWidget(self.centralwidget)

################################################################################
#	MENUBAR OBJECT
#
################################################################################

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

################################################################################
###### MENU1 OBJECT - Source
################################################################################

        self.menuMenu1_Src = QtGui.QMenu(self.menubar)
        self.menuMenu1_Src.setObjectName(_fromUtf8("menuMenu1_Src"))

        self.newAction_Src = QtGui.QAction('New', MainWindow)
        self.newAction_Src.setShortcut('Ctrl+N')
        self.newAction_Src.setStatusTip('Create new source')
        self.newAction_Src.triggered.connect(self.newFile1_Src)
        
        self.saveAction_Src = QtGui.QAction('Save', MainWindow)
        self.saveAction_Src.setShortcut('Ctrl+S')
        self.saveAction_Src.setStatusTip('Save current source in file')
        self.saveAction_Src.triggered.connect(self.saveFile1_Src)
	self.saveAction_Src.setDisabled(True)
	
	self.saveAsAction_Src = QtGui.QAction('Save as...', MainWindow)
        self.saveAsAction_Src.setShortcut('Ctrl+W')
        self.saveAsAction_Src.setStatusTip('Save source as file')
        self.saveAsAction_Src.triggered.connect(self.saveAsFile1_Src)
        
        self.openAction_Src = QtGui.QAction('Open...', MainWindow)
        self.openAction_Src.setShortcut('Ctrl+O')
        self.openAction_Src.setStatusTip('Load source from file')
        self.openAction_Src.triggered.connect(self.openFile1_Src)
        
        self.closeAction_Src = QtGui.QAction('Close', MainWindow)
        self.closeAction_Src.setShortcut('Ctrl+Q')
        self.closeAction_Src.setStatusTip('Close Demo App')
        self.closeAction_Src.triggered.connect(MainWindow.close)

	self.testAction_Src = QtGui.QAction('Test', MainWindow)
        self.testAction_Src.triggered.connect(self.test)

        self.menuMenu1_Src.addAction(self.newAction_Src)
        self.menuMenu1_Src.addAction(self.saveAction_Src)
	self.menuMenu1_Src.addAction(self.saveAsAction_Src)
        self.menuMenu1_Src.addAction(self.openAction_Src)
        self.menuMenu1_Src.addAction(self.closeAction_Src)
	self.menuMenu1_Src.addAction(self.testAction_Src)

################################################################################
###### MENU2 OBJECT - Message
################################################################################

        self.menuMenu2_Msg  = QtGui.QMenu(self.menubar)
        self.menuMenu2_Msg.setObjectName(_fromUtf8("menuMenu2_Msg"))

        self.newAction_Msg = QtGui.QAction('New', MainWindow)
        self.newAction_Msg.setShortcut('Ctrl+Alt+N')
        self.newAction_Msg.setStatusTip('Create new message')
        self.newAction_Msg.triggered.connect(self.newFile2_Msg)
        
        self.saveAction_Msg = QtGui.QAction('Save', MainWindow)
        self.saveAction_Msg.setShortcut('Ctrl+Alt+S')
        self.saveAction_Msg.setStatusTip('Save current message in file')
        self.saveAction_Msg.triggered.connect(self.saveFile2_Msg)
	self.saveAction_Msg.setDisabled(True)
	
	self.saveAsAction_Msg = QtGui.QAction('Save as...', MainWindow)
        self.saveAsAction_Msg.setShortcut('Ctrl+Alt+W')
        self.saveAsAction_Msg.setStatusTip('Save current message as file')
        self.saveAsAction_Msg.triggered.connect(self.saveAsFile2_Msg)
        
        self.openAction_Msg = QtGui.QAction('Open...', MainWindow)
        self.openAction_Msg.setShortcut('Ctrl+Alt+O')
        self.openAction_Msg.setStatusTip('Load message from file')
        self.openAction_Msg.triggered.connect(self.openFile2_Msg)

	self.testAction_Msg = QtGui.QAction('Test', MainWindow)
        self.testAction_Msg.triggered.connect(self.test2)

        self.menuMenu2_Msg.addAction(self.newAction_Msg)
        self.menuMenu2_Msg.addAction(self.saveAction_Msg)
	self.menuMenu2_Msg.addAction(self.saveAsAction_Msg)
        self.menuMenu2_Msg.addAction(self.openAction_Msg)
	self.menuMenu2_Msg.addAction(self.testAction_Msg)

################################################################################

	self.aboutAction = QtGui.QAction("&About", MainWindow)
	self.aboutAction.setShortcut('Ctrl+Alt+A')
        self.aboutAction.setStatusTip('About project')
        self.aboutAction.triggered.connect(self.about)

################################################################################

	self.menubar.addAction(self.menuMenu1_Src.menuAction())
	self.menubar.addAction(self.menuMenu2_Msg.menuAction())
	self.menubar.addAction(self.aboutAction)

	MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)

################################################################################
#	Signal handlers
################################################################################

	
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test2)
	QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.codeMessage)
	QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generateHCBinTree)
	QtCore.QObject.connect(self.checkbox_2, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), self.zoomTree)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

################# Menu Actions ##################################################################


################################################################################
#	File Operations
################################################################################
# SRC
################################################################################

    def newFile1_Src(self):
     	self.textEdit1_Src.clear()
	self.textEdit1_Src.setFocus()
	self.filename1_Src = ""
	self.saveAction_Src.setDisabled(True)
	print "newFile1"


    def saveFile1_Src(self):
	try:	
		if(self.filename1_Src):		
			f = open(self.filename1_Src, 'w')
	except IOError:
		print "Exc(0x04): No access to file. Check file permission attributes. Aborting  save..."
		return
	filedata = self.textEdit1_Src.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x02): File pathway variable not initialized. Aborting file load..."		
		return 
	f.close()

    def saveAsFile1_Src(self):
	filename = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', os.getenv('PWD'))
	try:	
		#print "\\%s\\ " %(filename)
		if (filename):
			f = open(filename, 'w')
	except IOError:
		print "Exc(0x01): No access to file. Check file permission attributes. Aborting file save..."
		return
	filedata = self.textEdit1_Src.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x03): File pathway variable not initialized. Aborting file load..."		
		return
	self.filename1_Src = filename[:]
	self.saveAction_Src.setDisabled(False)
	f.close()

    def saveAsFile1_Src(self):
	filename = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', os.getenv('PWD'))
	try:	
		#print "\\%s\\ " %(filename)
		if (filename):
			f = open(filename, 'w')
	except IOError:
		print "Exc(0x01): No access to file. Check file permission attributes. Aborting file save..."
		return
	filedata = self.textEdit1_Src.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x03): File pathway variable not initialized. Aborting file load..."		
		return
	self.filename1_Src = filename[:]
	self.saveAction_Src.setDisabled(False)
	f.close()

    def openFile1_Src(self):
	#filename = 'sourcedata.txt'
	filename = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', os.getenv('PWD'))
	try:
		if (filename):		
			f = open(filename, 'r')
	except IOError:
		print "Exc(0x02): None file picked or no permission. Aborting file load..."
		return

	try:
		filedata = f.read()
	except UnboundLocalError:
		print "Exc(0x04): File pathway variable not initialized. Aborting file load..."		
		return 
	self.filename1_Src = filename[:]
	self.saveAction_Src.setDisabled(False)
	self.textEdit1_Src.setText(filedata)
	self.textEdit1_Src.setFocus()
	f.close()

################################################################################
# MSG
################################################################################
 
    def newFile2_Msg(self):
     	self.textEdit3_Msg.clear()
	self.textEdit3_Msg.setFocus()
	self.filename2_Msg = ""
	self.saveAction_Msg.setDisabled(True)
        print "newFile2"

    def saveFile2_Msg(self):
	try:	
		if(self.filename2_Msg):		
			f = open(filename2_Msg, 'w')
	except IOError:
		print "Exc(0x04): No access to file. Check file permission attributes. Aborting  save..."
		return
	filedata = self.textEdit3_Msg.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x02): File pathway variable not initialized. Aborting file load..."		
		return 
	f.close()

    def saveAsFile2_Msg(self):
	filename = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', os.getenv('PWD'))
	try:	
		#print "\\%s\\ " %(filename)
		if (filename):
			f = open(filename, 'w')
	except IOError:
		print "Exc(0x01): No access to file. Check file permission attributes. Aborting file save..."
		return
	filedata = self.textEdit3_Msg.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x03): File pathway variable not initialized. Aborting file load..."		
		return
	self.filename2_Msg = filename[:]
	self.saveAction_Msg.setDisabled(False)
	f.close()


    def openFile2_Msg(self):
	filename = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', os.getenv('PWD'))	
	try:
		if (filename):		
			f = open(filename, 'r')
	except IOError:
		print "Exc(0x02): None file picked or no permission. Aborting file load..."
		return

	try:
		filedata = f.read()
	except UnboundLocalError:
		print "Exc(0x04): File pathway variable not initialized. Aborting file load..."		
		return 
	self.filename2_Msg = filename[:]
	self.saveAction_Msg.setDisabled(False)
	self.textEdit3_Msg.setText(filedata)
	self.textEdit3_Msg.setFocus()
	f.close()

    def about(self):
        QtGui.QMessageBox.about(MainWindow, "Huffman's Code Demo project",
                "<p><b>This application implements and demonstrates some "
                "basic performance of Huffman's coding algorithm.</b></p>"
                "<p>User may specify the source and the message to be encoded"
                "Two methods of Huffman's tree generation have been implemented:</p>"
                "<p> - suboptimal top-down method,</p>"
                "<p> - optimal bottom-up method.</p>"
                "<p>Basic parameters like entropy, average codelength "
                "and coding efficiency are visible on indicators below "
                "<b>Start coding </b> button. Application accepts mostly "
		"alphabetical symbols. Unacceptable ones are exchanged with spaces.</p>"
                "<p><b>Project Assessment related to Digital Communications course.</p>"
                "<p><b>Jarek Kiec, Electronics and Telecommunications, 3rd Year</p>"
		"<p><b>AGH University of Science and Technology, June 2014"
                "</p>")
########################################## ########################################## ########################################## 


    def test(self):
	self.adjustImage()	

    def test2(self):
	self.graphicsView.resize(self.graphicsView.size()*1.2)
	print self.comboBox.currentIndex()
	print self.checkbox.isChecked()


	
	

################################################################################
#	RETRANSLATE QT OBJECTS' NAMES 
################################################################################

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Huffman's Code Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Specify symbols", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Start coding", None, QtGui.QApplication.UnicodeUTF8))
	self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Create coding List", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
	self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Source:", None, QtGui.QApplication.UnicodeUTF8))
	self.label_3.setText(QtGui.QApplication.translate("MainWindow", "ASCII='char' : population", None, QtGui.QApplication.UnicodeUTF8))
	self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
	self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Coded message:", None, QtGui.QApplication.UnicodeUTF8))
	self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Decoded message:", None, QtGui.QApplication.UnicodeUTF8))
	self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Separate coded symbols", None, QtGui.QApplication.UnicodeUTF8))
	self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Entropy", None, QtGui.QApplication.UnicodeUTF8))
	self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Efficiency", None, QtGui.QApplication.UnicodeUTF8))
	self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Avg.codelength", None, QtGui.QApplication.UnicodeUTF8))
	self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Zoom Source View", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Overall", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Source View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu1_Src.setTitle(QtGui.QApplication.translate("MainWindow", "&Source", None, QtGui.QApplication.UnicodeUTF8))
	self.menuMenu2_Msg.setTitle(QtGui.QApplication.translate("MainWindow", "&Message", None, QtGui.QApplication.UnicodeUTF8))

################################################################################
#	HC'S OPERATIONS 
################################################################################    

    def generateHCBinTree(self): 
	print "Generating BT..."
	huff_algorithm.clearGlobaVariables()
	tempText = str(self.textEdit1_Src.toPlainText())
	tempText = tempText.replace("\"", " ")
	tempText = tempText.replace(":", " ")
	tempText = tempText.replace("\\", " ")	
	tempText = tempText.replace(";", " ")
	tempText = tempText.replace("\n", " ")
	tempText = tempText.replace("\r", " ")
	tempText = tempText.replace(">", " ")
	tempText = tempText.replace("<", " ")	
	tempText = tempText.replace("/", " ")
	tempText = tempText.replace("?", " ")
	tempText = tempText.replace("\t", " ")
	tempText = tempText.replace("{", " ")
	tempText = tempText.replace("}", " ")
	tempText = tempText.replace("[", " ")
	tempText = tempText.replace("]", " ")

	self.textEdit1_Src.setText(tempText)
	if ((len(tempText)<2) | (tempText=="")):	
		self.textEdit2_Srclist.setText("Source empty!!")
		return

	# from huff_algorithm.py API
	self.NodeStorage = huff_algorithm.TBinTree_NodeGenerator(tempText)
	self.NodeStorage.SortData()
	self.NodeStorage.Pop2Prob()
	self.NodeStorage.ListPrint()
	self.NodeStorage.SortedLeafGen()
	self.Generator = huff_algorithm.TBinTree_Tree(self.NodeStorage)
	if (self.comboBox.currentIndex()==0):
		self.Generator()
	else :
		self.Generator(0)
	self.Generator.GraphGen()
	self.Generator.CodingListGenerator()

	self.SourceEntropy = self.NodeStorage.GetSourceEntropy()
	self.SourceAvgCL = self.Generator.GetAvgCL()
	self.SourceCodEff = self.SourceEntropy/self.SourceAvgCL

	self.lcdNumber.display(self.SourceEntropy)
	self.lcdNumber_2.display(self.SourceCodEff)
	self.lcdNumber_3.display(self.SourceAvgCL)
	print self.SourceCodEff

	self.textEdit2_Srclist.setText(self.NodeStorage.pListString)
	image = QtGui.QImage("BT_graph.png")
	if image.isNull():
		print "wrong image file"
		return	
	self.picture = QtGui.QPixmap("BT_graph.png")
	self.graphicsView.resize(self.picture.size())
	self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image))
	self.adjustImage()

    def adjustImage(self):
	imageHeigh = self.graphicsView.size().height()
	frameHeigh = self.scrollArea.size().height()
	if (imageHeigh<frameHeigh):
		return
	ratio = float(frameHeigh)/int(imageHeigh+50)
	self.graphicsView.resize(self.graphicsView.size()*ratio)

    def zoomTree(self):
	imageHeigh = 2*self.graphicsView.size().height()
	frameHeigh = self.scrollArea.size().height()
	if (imageHeigh<frameHeigh):
		return
	if (self.checkbox_2.isChecked()) :
		ratio =1.6
	else :
		ratio =0.625
 	self.graphicsView.resize(self.graphicsView.size()*ratio)

    def codeMessage(self):
	self.Message = self.textEdit3_Msg.toPlainText()
	if (self.Generator!=None) :
		if (self.checkbox.isChecked()):
			self.codedMessage = self.Generator.CodeMessage(str(self.Message))
		else:
			self.codedMessage = self.Generator.CodeMessage(str(self.Message),1)
		if (self.codedMessage==None):
			self.textEdit4_Msgcoded.setText("Symbol not described in Source!!!")				
			return	
		self.textEdit4_Msgcoded.setText("".join(self.codedMessage))
	else :
		self.textEdit4_Msgcoded.setText("There is no Source!!!") 		
		return

		

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())



