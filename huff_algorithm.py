#############################################################################
# @file    
# @author 
# @version 
# @date    03.05.2014
# @brief   
#############################################################################

import pydot
global graphenn
graphenn = pydot.Dot(graph_type='digraph')

global 	gBT_IdNumber
global 	population
gBT_IdNumber=0;
global nodeCount
nodeCount=int(0)
global tempNodeLst
tempNodeLst=list()
global tempEdgeLst
tempEdgeLst=list()





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
	#def __str__(self):
	#	return "%.3d=%c : %.3d" % (self.symbol,self.symbol,self.prob)

# @brief  Object instance behaviour if "print" is used with it

	def __repr__(self):
		return ("id:%0.3d : %d (%d)<<" \
		% (self.id, self.prob,self.lvl) )

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

# @brief  Leaf instance behaviour if "print" is used with it
	
	def __repr__(self):
		if (self.lvl ==None):
			return "\t%.3d=%c id:%0.3d : %.3d\r\n" % (self.symbol, self.symbol,\
			self.id,self.prob)
		else :
			return "\t%.3d=%c id:%0.3d : %.3d (%d)\r\n" % (self.symbol,self.symbol,\
			self.id,self.prob, self.lvl)
	#def GetStr(self):
	#	if (self.lvl ==None):
	#		return "\t%.3d=%c id:%0.3d : %.3d\r\n" % (self.symbol, self.symbol,\
	#		self.id,self.prob)
	#	else :
	#		return "\t%.3d=%c id:%0.3d : %.3d (%d)\r\n" % (self.symbol,self.symbol,\
	#		self.id,self.prob, self.lvl)


# @brief  Binary tree leaf constructor specific class prototype contains symbol_val field and does 
#	    not need any fields for descending nodes (dead end, None on default)
# @param  Symbol value -> character which is represented by this node
# @param  Symbol probability -> how many times the specific symbol occured in the sourcedata.
# @param  Node level -> designated during BT generation (None on default).
	

class TBinTree_NodeGenerator:
  # @brief  
  # @param  Symbol value -> character which is represented by this node
	def __init__(self, filedata): 	#constructor which accepts string as arg and uses it to generate
					#dictionary to store input source data (arg -> filedata string 
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

	def SortData(self): # creates list by sorting symbols along probability
		for key, value in sorted(self.pSymbolsDict.iteritems(), key=lambda (k,v): (v,k),reverse=False):
		    	self.pSymbolsList_sorted.append((key,value))

	def SortedLeafGen(self):
		for leaf_no in range(0, len(self.pSymbolsList_sorted)):
			self.pBTLeafList.append(TBinTree_Leaf(self.pSymbolsList_sorted[leaf_no][0],self.pSymbolsList_sorted[leaf_no][1]))
			
	def DictPrint(self):
		print ("\r\nIn total = %d" % self.pPopulation)
		for key in range(self.S_LOW_VALUE, self.S_HIGH_VALUE+1):
			if (self.pSymbolsDict.has_key(key)):
				print "%.3d='%c' -> %.2d (%.2f)" % (key, key, self.pSymbolsDict[key], \
				float(self.pSymbolsDict[key])/self.pPopulation )

	def ListPrint(self):
		print ("\r\nIn total = %d" % self.pPopulation)
		
		for i in range(0,len(self.pSymbolsList_sorted)):
			print("%.3d=%c : %.3d" % (self.pSymbolsList_sorted[i][0],self.pSymbolsList_sorted[i][0], \
			self.pSymbolsList_sorted[i][1]))
	
	def GetPopulation(self):
		return self.pPopulation
	def GetSortedList(self):
		return self.pSymbolsList_sorted
	def GetNodeList(self):
		return self.pBTLeafList

class TBinTree_Tree:
	def __init__(self, Leaves):
		self.pPopulation = Leaves.GetPopulation()
		self.LeavesList = Leaves.GetNodeList()
		self.All_leaves = list()
		self.All_edges = list()
		#self.
	def __call__(self):
		# old self.root = fBinaryTreeBuilder(self.LeavesList,self.pPopulation, 0)
		self.root = fBinaryTreeBuilder(self.LeavesList, 0)
	def ShowBT(self):
		fBinaryTreeNodeFinder(self.root)
	def GraphGen(self):
		#global graphen
		print "Starting graph generating..."
		fBinaryTreeNodeCartograph(self.root)
		graphenn.write_png('example1_graph.png')
		print "Graph complete."
		

#########################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###########################################################################
def fBinaryTreeBuilder(LeavesList,Level) : # top-down method
	leaves_in_list = len(LeavesList)
	Population=0
	print LeavesList
	for i in LeavesList[:] :
		Population+=i.prob
	print("\tcounted pop=%d,nodes=%d\n" % (Population, leaves_in_list))
	if ( leaves_in_list <= 3 ) :
		if (leaves_in_list == 0) : 
			print "ERROR!->leaf node empty"
			return None		
		elif (leaves_in_list == 1) :
			print "\t1leaf" 
			total_leaf_prob = LeavesList[0].prob
			#print("\ttotal prob1 %d" % total_leaf_prob)
			#print ("lvl:%d"% Level)
			#print  LeavesList
			LeavesList[0].UpdateLvl(Level)			
			return LeavesList[0]
		elif  (leaves_in_list == 2) :
			print "\t2leaves"
			total_leaf_prob = LeavesList[0].prob  + LeavesList[1].prob
			#print("\ttotal prob2 %d" % total_leaf_prob)
			#print ("lvl:%d"% Level) 
			#print  LeavesList
			LeavesList[0].UpdateLvl(Level+1)
			LeavesList[1].UpdateLvl(Level+1)
			NewBTNode = TBinTree_Node(total_leaf_prob,LeavesList[0], LeavesList[1], Level)	
			return NewBTNode
		elif (leaves_in_list == 3) :
			print "\t3leaves" 
			#if ((LeavesList[0].prob+LeavesList[1].prob)
			LeavesList[0].UpdateLvl(Level+2)
			LeavesList[1].UpdateLvl(Level+2)
			BinaryNodeZero = TBinTree_Node(LeavesList[0].prob+LeavesList[1].prob, LeavesList[0],LeavesList[1],Level+1)
			LeavesList[2].UpdateLvl(Level+1)
			return TBinTree_Node( Population, BinaryNodeZero, LeavesList[2], Level)
			#print LeavesList[index+1:leaves_in_list]
	else :
		tempPopulation = Population
		index = 0
		prob_sum = 0
		while ( 1 ) :
			prob_sum = prob_sum + LeavesList[index].prob
			if ( (prob_sum<(tempPopulation/2)+1) and (index<(leaves_in_list)-1) ) : 
		# TODO update this statement to be more precise in case of list splitting along similiar prob
				#print prob_sum
				index = index + 1
			else :
				#print "\tBREAK"				
				break
		print "zero"
		#print LeavesList[0:index]
		print
		BinaryNodeZero = fBinaryTreeBuilder(LeavesList[:index], Level+1)
		print "one"
		BinaryNodeOne = fBinaryTreeBuilder(LeavesList[index:], Level+1)
		return TBinTree_Node( Population, BinaryNodeZero, BinaryNodeOne, Level) 
###################################################################################################################################


def fBinaryTreeNodeFinder(CurrentNode, Action = None):
	if (Action == None):
		print CurrentNode
		if (CurrentNode.__class__.__name__ == 'TBinTree_Node'):
			fBinaryTreeNodeFinder(CurrentNode.b_zero, Action)
			fBinaryTreeNodeFinder(CurrentNode.b_one, Action)


def fBinaryTreeNodeCartograph(thisNode, Action = None):
	if (Action == None):
		global nodeCount
		#print thisNode
		currentNode=int(nodeCount)
		if ( thisNode.__class__.__name__ == 'TBinTree_Leaf'):
			node_parent = makeLeaf(thisNode)
			graphenn.add_node(node_parent)
			return node_parent
			
		else :

			node_parent = makeNode(thisNode)	
			graphenn.add_node(node_parent)
	
			node_zero = fBinaryTreeNodeCartograph(thisNode.b_zero)
			node_one = fBinaryTreeNodeCartograph(thisNode.b_one)
			

			draw(node_parent,node_zero)
			draw(node_parent,node_one)
			nodeCount=nodeCount+1
			#print nodeCount
		return node_parent 

def makeNode(thisNode):
	tempStr="{%d|<f2>id=%d}" % (thisNode.b_zero.prob+thisNode.b_one.prob, thisNode.id)
	node_temp = pydot.Node(label=tempStr,shape="record",style="filled", fillcolor="brown")
	node_temp.set_name(str(thisNode.id))
	#print node_temp.to_string()
	return node_temp 
	

def makeLeaf(thisNode):
	tempStr = "<f1>\'%c\'|{%d|id-%d}" % (thisNode.symbol, thisNode.prob, thisNode.id)
	node_temp = pydot.Node(label=tempStr,shape="record",style="filled", fillcolor="green")
	node_temp.set_name(str(thisNode.id))
	#print node_temp.to_string()
	return node_temp 
	print

def draw(node_parent,node_child):
	edge = pydot.Edge(node_parent,node_child)
	#print edge.to_string()
	graphenn.add_edge(edge)





def main():
	# open file with source data, read content and save in strSourceData
	filename = 'sourcedata.txt'
	f = open(filename, 'r')
	strSourceData = f.read()
	f.close()
	
	#initialize instance of Binary tree node generator with string (from file)
	NodeStorage = TBinTree_NodeGenerator(strSourceData)
	
	NodeStorage.SortData()
	#Grader.DictPrint()
	NodeStorage.ListPrint()
	NodeStorage.SortedLeafGen()
	#print Grader.GetNodeList()
	Generator = TBinTree_Tree(NodeStorage)
	Generator();
	print "\n\r"
	#Generator.ShowBT();
	Generator.GraphGen();


if __name__ == '__main__':
    main()



