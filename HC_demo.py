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


class ImageWidget(QtGui.QLabel):
	@QtCore.pyqtSlot()
	def resizeImage(self):
		print "resize" 
	
   
class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
	#self.filedata = str()
	self.filename1_src = str()
	#self.text = str()
    def setupUi(self, MainWindow):
	MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 640)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 220, 530))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

################################################################################
#	TOOLBOX OBJECT
#	
#
##########
        self.toolBox = QtGui.QToolBox(self.frame)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 190, 500))
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))

################################################################################
###### Tolbox page 1
################################################################################
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 190, 330))
        self.page.setObjectName(_fromUtf8("page"))

        self.textEdit1_src = SourceTextEdit(self.page)
        self.textEdit1_src.setGeometry(QtCore.QRect(0, 30, 190, 140))
        self.textEdit1_src.setObjectName(_fromUtf8("textEdit"))
	self.textEdit1_src.connect(self.textEdit1_src,QtCore.SIGNAL("textChanged()"),self.textEdit1_src,QtCore.SLOT("slotTextChanged()"))

        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(0, 180, 190, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.comboBox = QtGui.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(0, 230, 190, 30))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))

        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 180, 20))
        self.label.setObjectName(_fromUtf8("label"))

        self.toolBox.addItem(self.page, _fromUtf8(""))

################################################################################
###### Tolbox page 2
################################################################################
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 190, 330))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        
	self.textEdit3_msg = MessageTextEdit(self.page_2)
        self.textEdit3_msg.setGeometry(QtCore.QRect(0, 30, 190, 140))
        self.textEdit3_msg.setObjectName(_fromUtf8("textEdit_3"))
 	self.textEdit3_msg.connect(self.textEdit3_msg,QtCore.SIGNAL("textChanged()"),self.textEdit3_msg,QtCore.SLOT("slotTextChanged()"))

	self.toolBox.addItem(self.page_2, _fromUtf8(""))

################################################################################
###### Tolbox page 3
################################################################################
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.toolBox.addItem(self.page_3, _fromUtf8(""))

################################################################################
###### Tolbox page 4
################################################################################
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.toolBox.addItem(self.page_4, _fromUtf8(""))

################################################################################
###### Tolbox page 1
################################################################################
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.toolBox.addItem(self.page_5, _fromUtf8(""))

################################################################################
#	TAB OBJECT
#	
#
##########
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(240, 10, 550, 530))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
################################################################################
###### TAB page 1
################################################################################
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(4, 4, 180, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(4, 26, 180, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.textEdit2_srclist = QtGui.QTextEdit(self.tab)
        self.textEdit2_srclist.setGeometry(QtCore.QRect(4, 52, 170, 400))
        self.textEdit2_srclist.setObjectName(_fromUtf8("textEdit_2"))
	self.textEdit2_srclist.setReadOnly(True)
	#self.textEdit2_srclist.connect(self.textEdit1_src,QtCore.SIGNAL("textChanged()"),self.textEdit1_src,QtCore.SLOT("slotTextChanged()"))
################################################################################
###### TAB page 2
################################################################################
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

	self.picture = QtGui.QPixmap("example1_graph.png")

        #self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        #self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Ignored,
        #        QtGui.QSizePolicy.Ignored)


	self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
	self.scrollArea.setGeometry(QtCore.QRect(10, 10, 520, 470))

	self.graphicsView = ImageWidget(self.scrollArea)
        self.graphicsView.setBackgroundRole(QtGui.QPalette.Base)
	self.graphicsView.setPixmap(self.picture)
#	self.graphicsView.connect(self.graphicsView,QtCore.SIGNAL("pressed()"),self.graphicsView, QtCore.SLOT("resizeImage()"))

        self.scrollArea.setWidget(self.graphicsView)
	self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        MainWindow.setCentralWidget(self.centralwidget)

################################################################################
#	MENUBAR OBJECT
#	
#
##########
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
################################################################################
###### MENU1 OBJECT
################################################################################
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
	MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #self.actionLoad_source = QtGui.QAction(MainWindow)
        #self.actionLoad_source.setObjectName(_fromUtf8("actionLoad_source"))
        #self.menuMenu.addAction(self.actionLoad_source)
        
###
        self.newAction = QtGui.QAction('New', MainWindow)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('Create new file')
        self.newAction.triggered.connect(self.newFile)
        
        self.saveAction = QtGui.QAction('Save', MainWindow)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save current file')
        self.saveAction.triggered.connect(self.saveFile)
	self.saveAction.setDisabled(True)
	
	self.saveAsAction = QtGui.QAction('Save as...', MainWindow)
        self.saveAsAction.setShortcut('Ctrl+W')
        self.saveAsAction.setStatusTip('Save current as file')
        self.saveAsAction.triggered.connect(self.saveAsFile)
        
        self.openAction = QtGui.QAction('Open...', MainWindow)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open a file')
        self.openAction.triggered.connect(self.openFile)
        
        self.closeAction = QtGui.QAction('Close', MainWindow)
        self.closeAction.setShortcut('Ctrl+Q')
        self.closeAction.setStatusTip('Close Demo App')
        self.closeAction.triggered.connect(MainWindow.close)

	self.testAction = QtGui.QAction('Test', MainWindow)
        self.testAction.triggered.connect(self.test)

        #self.menubar = self.menuBar()
        #self.fileMenu = menubar.addMenu('&File')
        self.menuMenu.addAction(self.newAction)
        self.menuMenu.addAction(self.saveAction)
	self.menuMenu.addAction(self.saveAsAction)
        self.menuMenu.addAction(self.openAction)
        self.menuMenu.addAction(self.closeAction)
	self.menuMenu.addAction(self.testAction)

	#####
	self.menubar.addAction(self.menuMenu.menuAction())
        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
	QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generateHCBinTree)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


################# Menu Actions ##################################################################

################################################################################
#	File Operations
################################################################################

    def newFile(self):
	#newFileSelect = dict()
	#python switch-case quivalent...
	newFileSelect = { 0 : self.newFile1_Src, \
		1 : self.newFile2_Msg, \
		2 : self.newFile2_Msg, \
		3 : self.newFile2_Msg, \
		4 : self.newFile2_Msg, \
		5 : self.newFile2_Msg}  
	toolboxIndex = self.toolBox.currentIndex()
	newFileSelect[toolboxIndex]()

    def newFile1_Src(self):
     	self.textEdit1_src.clear()
	self.filename1_src = ""
	self.saveAction.setDisabled(True)
	print "newFile1"

    def newFile2_Msg(self):
     	self.textEdit1_src.clear()
	self.filename1_msg = ""
	self.saveAction.setDisabled(True)
        print "newFile2"

    def saveFile(self):
	activeToolbox = self.toolBox.currentIndex()
	try:	
		if(self.filename1_src):		
			f = open(self.filename1_src, 'w')
	except IOError:
		print "Exc(0x04): No access to file. Check file permission attributes. Aborting  save..."
		return
	filedata = self.textEdit1_src.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x02): File pathway variable not initialized. Aborting file load..."		
		return 
	#self.saveAction.setDisabled(False)
	f.close()

    def saveAsFile(self):
	filename = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', os.getenv('PWD'))
	try:	
		#print "\\%s\\ " %(filename)
		if (filename):
			f = open(filename, 'w')
	except IOError:
		print "Exc(0x01): No access to file. Check file permission attributes. Aborting file save..."
		return
	filedata = self.textEdit1_src.toPlainText()
	try:
		f.write(filedata)	
	except UnboundLocalError:
		print "Exc(0x03): File pathway variable not initialized. Aborting file load..."		
		return
	self.filename1_src = filename[:]
	self.saveAction.setDisabled(False)
	f.close()
        
        
    def openFile(self):
	openFileSelect = { 0 : self.openFile1_Src,\
		1 : self.openFile2_Msg,\
		2 : self.openFile1_Src,\
		3 : self.openFile1_Src,\
		4 : self.openFile1_Src,\
		5 : self.openFile1_Src}
	toolboxIndex = self.toolBox.currentIndex()
	openFileSelect[toolboxIndex]()

    def openFile1_Src(self):
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
	self.filename1_src = filename[:]
	self.saveAction.setDisabled(False)
	self.textEdit1_src.setText(filedata)
	f.close()


########################################## Test for replacement of images inside tab2 TODO resize and scrolladjustment problems 
    def openFile2_Msg(self):
	print "openFile2 ongoing..."
	#fileName = str()
	fileName = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', os.getenv('PWD'))
	if fileName:
		image = QtGui.QImage(fileName)
		if image.isNull():
			print "wrong image file"
			return	
		self.picture = QtGui.QPixmap(fileName)
		self.graphicsView.resize(self.picture.size())
		self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image))
		
	        self.graphicsView.setBackgroundRole(QtGui.QPalette.Base)
      		self.graphicsView.setSizePolicy(QtGui.QSizePolicy.Ignored,
                	QtGui.QSizePolicy.Ignored)

		self.scrollArea.setWidget(self.graphicsView)
########################################## ########################################## ########################################## 


    def test(self):
	#print self.page.isVisible()
	print self.toolBox.currentIndex()

################################################################################
#	RETRANSLATE QT OBJECTS' NAMES 
################################################################################
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Huffman's Code Demo by J.Kiec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Generate BT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Top-down method", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Huffman's Code binary tree generation", None, QtGui.QApplication.UnicodeUTF8))
	self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Source Statistics:", None, QtGui.QApplication.UnicodeUTF8))
	self.label_3.setText(QtGui.QApplication.translate("MainWindow", "ASCII='char' : population", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("MainWindow", "Coded message", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("MainWindow", "Decoded message", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QtGui.QApplication.translate("MainWindow", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Binary Tree View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "&Menu", None, QtGui.QApplication.UnicodeUTF8))
        #self.actionLoad_source.setText(QtGui.QApplication.translate("MainWindow", "Load source", None, QtGui.QApplication.UnicodeUTF8))

################################################################################
#	HC'S OPERATIONS 
################################################################################    

    def generateHCBinTree(self): 
	print "Generating BT..."
	huff_algorithm.clearGlobaVariables()
	tempText = str(self.textEdit1_src.toPlainText())
	tempText = tempText.replace(":", " ")
	tempText = tempText.replace("\\", " ")	
	tempText = tempText.replace(";", " ")
	tempText = tempText.replace("\n", " ")
	tempText = tempText.replace("\r", " ")
	tempText = tempText.replace(">", " ")
	tempText = tempText.replace("<", " ")	
	tempText = tempText.replace("/", " ")
	tempText = tempText.replace("?", " ")
	tempText = tempText.replace("\"", " ")

	self.textEdit1_src.setText(tempText)
	if ((len(tempText)<2) | (tempText=="")):	
		self.textEdit2_srclist.setText("Empty!!")
		return
	NodeStorage = huff_algorithm.TBinTree_NodeGenerator(tempText)
	NodeStorage.SortData()
	NodeStorage.ListPrint()
	NodeStorage.SortedLeafGen()
	Generator = huff_algorithm.TBinTree_Tree(NodeStorage)
	Generator()
	Generator.GraphGen()
	self.textEdit2_srclist.setText(NodeStorage.pListString)
	image = QtGui.QImage("BT_graph.png")
	if image.isNull():
		print "wrong image file"
		return	
	self.picture = QtGui.QPixmap("BT_graph.png")
	self.graphicsView.resize(self.picture.size())
	self.graphicsView.setPixmap(QtGui.QPixmap.fromImage(image))
	
        self.graphicsView.setBackgroundRole(QtGui.QPalette.Base)
	self.graphicsView.setSizePolicy(QtGui.QSizePolicy.Ignored,
        	QtGui.QSizePolicy.Ignored)

	self.scrollArea.setWidget(self.graphicsView)

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())



