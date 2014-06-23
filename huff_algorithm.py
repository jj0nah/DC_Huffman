# -*- coding: utf-8 -*-
#############################################################################
# @file    huff_algorithm.py
# @author  J.Kiec
# @version 1.0
# @date    03.05.2014
# @brief   Huffman's Code operational code
# 
#############################################################################

import pydot
import numpy as np
global BTGraph
BTGraph = pydot.Dot(graph_type='digraph')

global 	gBT_IdNumber
gBT_IdNumber=0;
global nodeCount
nodeCount=int(0)

# @brief  General Binary tree node class prototype 
class TBinTree_Node(object):
    def __init__(self, symbol_prob, bin_zero=None, bin_one=None, node_lvl=None):
	global gBT_IdNumber
	self.id=gBT_IdNumber
	gBT_IdNumber=gBT_IdNumber+1
	self.prob = symbol_prob
	self.lvl = node_lvl
	self.b_one = bin_one
	self.b_zero = bin_zero
# @brief  Object instance behaviour if "print" is used with it
    def __repr__(self):
	return ("id:%0.3d : %f (%d)<<" % (self.id, self.prob, self.lvl) )

# @brief  BT node method to obtain ID
# @retval Node's ID
	 
    def GetID(self):
	return self.id

# @brief  BT node method to obtain its probability, how many times given symbol (in leaf) 
# 	    or sum of probabilities of connected and downstream to this one
# @retval Probability
	 
    def GetProb(self):
	return self.prob

# @brief  Method used to update node's level field during BT generation

    def UpdateLvl(self, level):
	self.lvl=level
	#def GetStr(self):
	#	return ("id:%s : %s" % (self.id, self.prob) )

# @brief  Leaf Binary tree node class prototype which inherites from general class of BT node

class TBinTree_Leaf(TBinTree_Node):
# @brief  Binary tree leaf constructor specific class prototype contains symbol_val field and does 
#	    not need any fields for descending nodes (dead end, None on default)
# @param  Symbol value -> character which is represented by this node
# @param  Symbol probability -> how many times the specific symbol occured in the sourcedata.
# @param  Node level -> designated during BT generation (None on default).
	
    def __init__(self, symbol_val, symbol_prob,  node_lvl=None):
	global gBT_IdNumber
	self.id=gBT_IdNumber
	gBT_IdNumber=gBT_IdNumber+1
	self.symbol = symbol_val
	self.prob = symbol_prob
	self.lvl = node_lvl
	self.b_zero = None
	self.b_one = None
	self.code = None

# @brief  Leaf instance behaviour if "print" is used with it
	
    def __repr__(self):
	if (self.lvl ==None):
		return "\t%.3d=%c id:%0.3d : %.3f\r\n" % (self.symbol, self.symbol,\
		self.id,self.prob)
	else :
		return "\t%.3d=%c id:%0.3d : %.3f (%d)\r\n" % (self.symbol,self.symbol,\
		self.id,self.prob, self.lvl)


# @brief  Binary tree leaf constructor specific class prototype contains symbol_val field and does 
#	    not need any fields for descending nodes (dead end, None on default)
# @param  Symbol value -> character which is represented by this node
# @param  Symbol probability -> how many times the specific symbol occured in the sourcedata.
# @param  Node level -> designated during BT generation (None on default).
	

class TBinTree_NodeGenerator:
  # @brief  
  # @param  Symbol value -> character which is represented by this node
    def __init__(self, filedata): 	#constructor which accepts string as arg and uses it to generate dictionary to store input source data (arg -> filedata string 
	self.S_LOW_VALUE=32 #space
	self.S_HIGH_VALUE=125 # }- character
	self.pPopulation = 0 #total character count
	#create empty list as property pBTLeafList -> for fresh data
	self.pBTLeafList = list()	
	#create empty list as property pSymbolsList_sorted -> for sorted fresh data
	self.pSymbolsList_sorted = list()
	#create empty dictionary as property pSymbolsDict	
	self.pSymbolsDict = dict()
	#fill list with symbol data (character with their probability)		
	for ascii_code in range(self.S_LOW_VALUE, self.S_HIGH_VALUE+1): # for every ASCII code from LOW_VALUE to HIGH_VALUE 
		x = filedata.count(chr(ascii_code))			# count number of characters in string 
		if (x>0) :						# if character appears in string at least once
			self.pSymbolsDict.update({ascii_code:x})	# put it into dictionary with ASCII code as key and no. of appearences as value
			self.pPopulation +=x				# all counted symbols are added to total source data population
	self.pListString = str()


    def SortData(self): # creates list by sorting symbols along probability
	for key, value in sorted(self.pSymbolsDict.iteritems(), key=lambda (k,v): (v,k),reverse=False):
	    	self.pSymbolsList_sorted.append((key,value))
		

    def Pop2Prob(self): # takes total population into consideration and tranlates it into probability
	for x in range(0,len(self.pSymbolsList_sorted)):
		tempItem = list(self.pSymbolsList_sorted.pop(x))
		tempItem[1]=float(tempItem[1])/self.pPopulation
		print tempItem
		self.pSymbolsList_sorted.insert(x,tempItem)
		
	    	#self.pSymbolsList_sorted[x]=self.pSymbolsList_sorted[x]/self.pPopulation
	print self.pSymbolsList_sorted
	
    def setNewSymbolsDict(self, newDict):
	self.pSymbolsDict = newDict

    def SortedLeafGen(self):
	for leaf_no in range(0, len(self.pSymbolsList_sorted)):
		self.pBTLeafList.append(TBinTree_Leaf(self.pSymbolsList_sorted[leaf_no][0],self.pSymbolsList_sorted[leaf_no][1]))
	self.LeafPopulation = len(self.pBTLeafList)

		
	
    def DictPrint(self):
	print ("\r\nIn total = %d" % self.pPopulation)
	for key in range(self.S_LOW_VALUE, self.S_HIGH_VALUE+1):
		if (self.pSymbolsDict.has_key(key)):
			print "%.3d='%c' -> %.3f " % (key, key, self.pSymbolsDict[key], \
			float(self.pSymbolsDict[key])/self.pPopulation )

    def ListPrint(self):
	print ("\r\nIn total = %d" % self.pPopulation)
	for i in range(0,len(self.pSymbolsList_sorted)):
		print("%.3d=%c : %.3f" % (self.pSymbolsList_sorted[i][0],self.pSymbolsList_sorted[i][0], \
			self.pSymbolsList_sorted[i][1]))
		self.pListString = self.pListString + ("%.3d='%c' : %.3f\n" % (self.pSymbolsList_sorted[i][0],self.pSymbolsList_sorted[i][0], \
			self.pSymbolsList_sorted[i][1]))

    def GetPopulation(self):
	return self.pPopulation
    def GetSortedList(self):
	return self.pSymbolsList_sorted
    def GetNodeList(self):
	return self.pBTLeafList
    def	GetSourceEntropy(self):
	Entropy = 0
	temp = 0
	for x in range(0,len(self.pSymbolsList_sorted)):
		temp = self.pSymbolsList_sorted[x][1]
		Entropy+= temp*np.log2(1.0/temp)
		print temp
		print "Source entropy:\t%f" % (Entropy)
	return Entropy

class TBinTree_Tree:
    def __init__(self, Leaves):
	self.pPopulation = Leaves.GetPopulation()
	self.LeavesList = Leaves.GetNodeList()
	self.All_leaves = list()
	self.All_edges = list()
	self.CodeList = dict()
    def __call__(self,option=None): #by default top-down method of defininf binary tree, if parameters is present- bottom-up
	if (option==None):
		self.root = fBinaryTreeBuilder(self.LeavesList, 0)
	else :
		self.root = fBinaryTreeBuilderBU(self.LeavesList, 0)		
	self.AvgCL = fMECalc(self.root)

    def ShowBT(self):
	fBinaryTreeNodeFinder(self.root)
    def GraphGen(self):
	#global graphen
	print "Starting Source tree graph generation..."
	fBinaryTreeNodeCartograph(self.root)
	BTGraph.write_png('SourceTree.png')
	print "Graph complete."
    def CodingListGenerator(self):
	global gCodingDict		
	print "Generating symbol coding list..."
	fBinaryTreeNodeFinder(self.root,Action=1)
# print dictionary with symbol coding
	dictKeys = gCodingDict.keys()
	for x in range(0,len(gCodingDict)):
		print  "%02d)\'%c\' -> %s"% (x,dictKeys[x],gCodingDict[dictKeys[x]])
    def CodeMessage(self,MessageContent, Action=None):
	global gCodingDict
	if (Action==None):
		codedMsg = ""
		print len(MessageContent)
		for x in range(0,len(MessageContent)): #TODO try KeyError -> dictionary unspecified key handling - done
			if (gCodingDict.has_key(ord(MessageContent[x]))==False):
				return None
			codedMsg = codedMsg + gCodingDict[ord(MessageContent[x])] + "|"
		return codedMsg
	elif (Action==1):
		codedMsg = list()
		for x in range(0,len(MessageContent)):
			if (gCodingDict.has_key(ord(MessageContent[x]))==False):
				return None
			codedMsg.append(gCodingDict[ord(MessageContent[x])])
		return codedMsg
    def GetAvgCL(self):
	return self.AvgCL

# @brief  Decoding function as a method of Binary tree class which cooperates with indepednent
#	  fDecodeBit function which is repeteadly called until the end of coded message.
#	  Global variable which temporarly stores string is used.
# @param  Encoded as a string.

    def DecodeMessage(self,MessageContent):
	print "Commencing message decoding..."
	global gTempCodedMsg
	gTempCodedMsg = "".join(MessageContent) #copy coded message string into global variable string for further manipulations
	gTempCodedMsg = gTempCodedMsg.replace("|","")
	#print gTempCodedMsg
	tempString = ""
	while (len(gTempCodedMsg)): #while there are bits of the coded message available run decoding of consecutive symbols in loop 		
		symbol = fDecodeBit(self.root, gTempCodedMsg)
		print symbol
		tempString = tempString + chr(symbol) # concatanate character symbol to string			
	return tempString
	print

global gTempCodedMsg
gTempCodedMsg = str()

# @brief  Indepednent function which recursively calls itself to explore binary tree until Leaf is reached
#	  and proper symbol retrieved
# @param  Current - strarting point for exploring.
# @param  Piece of encoded message - the compass to navigate between branches.

def fDecodeBit(CurrentNode,CodedMsg):
	global gTempCodedMsg
	gTempCodedMsg = CodedMsg
	if (CurrentNode.__class__.__name__ == 'TBinTree_Leaf'):
		return CurrentNode.symbol
	elif (CurrentNode.__class__.__name__ == 'TBinTree_Node'):
		#if (len(CodedMsg)):
		#print CodedMsg[0]
		if (CodedMsg[0]=='0') :
			return fDecodeBit(CurrentNode.b_zero, CodedMsg[1:])
		elif (CodedMsg[0]=='1') :
			return fDecodeBit(CurrentNode.b_one, CodedMsg[1:])
		else :
			print "DecodeError 2 Message!"
	else:
		print "DecodeError 1 Message!"



# @brief  Indepednent function with implementation of suboptimal top-down method of source tree generation
#	  algorithm 
# @param  List of BTLeaves representing symbols sorted along probability
# @param  Current level - codelength 

def fBinaryTreeBuilder(LeavesList,Level) : # top-down method
	print "Generating Soure tree implementing top-down algorithm."
	leaves_in_list = len(LeavesList)
	Population=0
	print LeavesList
	for i in LeavesList[:] :
		Population+=i.prob
	print("\tcounted pop=%d,nodes=%d\n" % (Population, leaves_in_list))
	if ( leaves_in_list < 3 ) :
		if (leaves_in_list == 0) : 
			print "ERROR!->leaf node empty"
			return None		
		elif (leaves_in_list == 1) :
			total_leaf_prob = LeavesList[0].prob
			LeavesList[0].UpdateLvl(Level)			
			return LeavesList[0]
		elif  (leaves_in_list == 2) :
			total_leaf_prob = LeavesList[0].prob  + LeavesList[1].prob
			LeavesList[0].UpdateLvl(Level+1)
			LeavesList[1].UpdateLvl(Level+1)
			NewBTNode = TBinTree_Node(total_leaf_prob,LeavesList[0], LeavesList[1], Level)	
			return NewBTNode
	else :
		tempPopulation = float(1.0)#Population
		index = 0
		prob_sum = 0
		while ( 1 ) :
			prob_sum = prob_sum + LeavesList[index].prob
			if ( (prob_sum<(0.5*Population)) and (index<(leaves_in_list)-1) ) : 
				index = index + 1
			else :
				break
		BinaryNodeZero = fBinaryTreeBuilder(LeavesList[:index], Level+1)
		BinaryNodeOne = fBinaryTreeBuilder(LeavesList[index:], Level+1)
		return TBinTree_Node( Population, BinaryNodeZero, BinaryNodeOne, Level)

# @brief  Indepednent function with more efficient implementation of bottom-up method of source tree generation
#	  algorithm. 
# @param  List of BTLeaves representing symbols sorted along probability
# @param  Current level - codelength 

def fBinaryTreeBuilderBU(LeavesList,Level) : # bottom-up method
	print "Generating Soure tree implementing bottom-up algorithm."
	print LeavesList.__class__.__name__
	print LeavesList
	while (len(LeavesList)>1):
		for leafIndex in range(0,len(LeavesList)-1) :
			if (LeavesList[leafIndex].prob>LeavesList[leafIndex+1].prob):
				temp = LeavesList.pop(leafIndex)
				LeavesList.insert(leafIndex+1, temp)
	
		newNode = TBinTree_Node(LeavesList[0].prob+LeavesList[1].prob, LeavesList[0], LeavesList[1], 0)
		LeavesList.insert(0, newNode)
		LeavesList.pop(1)
		LeavesList.pop(1)
	fLvlUpdate(LeavesList[0],0)	
	return LeavesList[0]
	
def fLvlUpdate(CurrentNode, CurrentLevel):
	CurrentNode.UpdateLvl(CurrentLevel)
	if ( CurrentNode.__class__.__name__ == 'TBinTree_Node'):
		fLvlUpdate(CurrentNode.b_zero,CurrentLevel+1)
		fLvlUpdate(CurrentNode.b_one,CurrentLevel+1)
	


###################################################################################################################################

global gCodingDict
gCodingDict = dict()

def fBinaryTreeNodeFinder(CurrentNode, Action = None, Code = ""):#, gCodingDict= None):
	global gCodingDict
	if (Action == None):
		print CurrentNode
		if (CurrentNode.__class__.__name__ == 'TBinTree_Node'):
			fBinaryTreeNodeFinder(CurrentNode.b_zero, Action)
			fBinaryTreeNodeFinder(CurrentNode.b_one, Action)
	elif (Action == 1):
		#print "wio!!!"
		tempText = str(Code)
		#tempText = Code
		if (CurrentNode.__class__.__name__ == 'TBinTree_Node'):
			fBinaryTreeNodeFinder(CurrentNode.b_zero, Action,Code = (tempText+'0')) 
			fBinaryTreeNodeFinder(CurrentNode.b_one, Action,Code = (tempText+'1')) 
		elif (CurrentNode.__class__.__name__ == 'TBinTree_Leaf'):
			gCodingDict[CurrentNode.symbol]=Code
		
def fMECalc(CurrentNode): # or weighted average codelength, called recursively
	if (CurrentNode.__class__.__name__ == 'TBinTree_Node'):
		temp = fMECalc(CurrentNode.b_zero) 
		return (temp + fMECalc(CurrentNode.b_one) )
	elif (CurrentNode.__class__.__name__ == 'TBinTree_Leaf'):
		return CurrentNode.prob*CurrentNode.lvl
		


def fBinaryTreeNodeCartograph(thisNode, Action = None):
	if (Action == None):
		global nodeCount
		#print thisNode
		currentNode=int(nodeCount)
		if ( thisNode.__class__.__name__ == 'TBinTree_Leaf'):
			node_parent = makeLeaf(thisNode)
			BTGraph.add_node(node_parent)
			return node_parent
			
		else :

			node_parent = makeNode(thisNode)	
			BTGraph.add_node(node_parent)
	
			node_zero = fBinaryTreeNodeCartograph(thisNode.b_zero)
			node_one = fBinaryTreeNodeCartograph(thisNode.b_one)
			
			draw(node_parent,node_zero)
			draw(node_parent,node_one)
			nodeCount=nodeCount+1
			#print nodeCount
		return node_parent 

def makeNode(thisNode):
	tempStr="{%.3f|<f2>id=%d(%d)}" % (thisNode.b_zero.prob+thisNode.b_one.prob, thisNode.id,thisNode.lvl)
	node_temp = pydot.Node(label=tempStr,shape="record",style="filled", fillcolor="brown")
	node_temp.set_name(str(thisNode.id))
	#print node_temp.to_string()
	return node_temp 
	

def makeLeaf(thisNode):
	tempStr = "<f1>\'%c\'|{%.3f|id=%d(%d)}" % (thisNode.symbol, thisNode.prob, thisNode.id,thisNode.lvl)
	node_temp = pydot.Node(label=tempStr,shape="record",style="filled", fillcolor="green")
	node_temp.set_name(str(thisNode.id))
	#print node_temp.to_string()
	return node_temp 
	print

def draw(node_parent,node_child):
	edge = pydot.Edge(node_parent,node_child)
	#print edge.to_string()
	BTGraph.add_edge(edge)

def clearGlobaVariables():
	global BTGraph
	global nodeCount
	global gBT_IdNumber 
	global gTempCodedMsg  
	global gCodingDict
	BTGraph = pydot.Dot(graph_type='digraph')
	nodeCount=int(0)
	gBT_IdNumber=0
	gTempCodedMsg = ""
	gCodingDict = dict()


def main():
	# open file with source data, read content and save in strSourceData
	filename = 'sourcedata.txt'
	f = open(filename, 'r')
	strSourceData = f.read()
	f.close()
	MessageContent="Tsrrr"

	#initialize instance of Binary tree node generator with string (from file)
	NodeStorage = TBinTree_NodeGenerator(strSourceData)
	
	NodeStorage.SortData()
	#Grader.DictPrint()
	NodeStorage.Pop2Prob()
	NodeStorage.ListPrint()
	NodeStorage.SortedLeafGen()
	#print Grader.GetNodeList()
	Generator = TBinTree_Tree(NodeStorage)
	Generator(option=1)
	print "\n\r"
	Generator.ShowBT()
	Generator.GraphGen();
	#Generator.CodingListGenerator()
	#codedMsg = Generator.CodeMessage(MessageContent)
	#print codedMsg

if __name__ == '__main__':
    main()



