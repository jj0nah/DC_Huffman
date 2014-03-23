global 	BT_IdNumber
global 	population
BT_IdNumber=0

class BT_Node:
	def __init__(self,bin_one,bin_zero, symbol_prob):
		global BT_IdNumber
		self.id=BT_IdNumber
		BT_IdNumber=BT_IdNumber+1
		self.prob = symbol_prob
		self.binary_one = bin_one
		self.binary_zero = bin_zero
	#def __str__(self):
	#	return "%.3d=%c : %.3d" % (self.symbol,self.symbol,self.prob)
	def __repr__(self):
		return "(0's=%.3d, 1's=%.3d) id:%.3d : %.3d\r\n" % \
		(self.binary_zero.GetID(),self.binary_one.GetID(), \
		self.id, self.prob)
	def GetID(self):
		return self.id
	def GetProb(self):
		return self.prob
class BT_Leaf(BT_Node):	
	def __init__(self,symbol_val,symbol_prob):
		global BT_IdNumber
		self.id=BT_IdNumber
		BT_IdNumber=BT_IdNumber+1
		self.symbol = symbol_val
		self.prob = symbol_prob
		self.binary_one = None
		self.binary_zero = None
	def __repr__(self):
		return "%.3d=%c id:%0.3d : %.3d\r\n" % (self.symbol,self.symbol,\
		self.id,self.prob)



#class BT_Tree:
#	def __init__(self,symbol_proba_list):
		


text_string="straszna dupa i w ogolefdkzljc zxcvlzkj czk ajd lkjvlkxjxzlk cjaslk dj"
print(text_string)
LowValSymbol=32 #space
HighValSymbol=125 # }- character
symbols_count=dict()
print len(text_string)
# let's make dictionary ascii code (character) with its count in text_string
# also print the probability (character_count/string's length)
population = len(text_string)
for ascii_code in range(LowValSymbol, HighValSymbol+1):
	x = text_string.count(chr(ascii_code))
	if (x!=0) :
		symbols_count.update({ascii_code:x})

for key in range(LowValSymbol, HighValSymbol+1):
	if (symbols_count.has_key(key)):
		print "%.3d='%c' -> %.2d (%.2f)" % (key,key,symbols_count[key], \
		float(symbols_count[key])/population )


symbols_count_sorted = list()
for key, value in sorted(symbols_count.iteritems(), key=lambda (k,v): (v,k),reverse=False):
    	symbols_count_sorted.append((key,value))
for i in range(0,len(symbols_count_sorted)):
	print("%.3d=%c : %.3d" % (symbols_count_sorted[i][0],symbols_count_sorted[i][0], \
	symbols_count_sorted[i][1]))
print "\r\nBT Construction:"

# Let's rewrite our list as an array (list) of objects
nodeList1 = list() #list() or [] -> defining list
for i in range(len(symbols_count_sorted)):
	nodeList1.append( BT_Leaf (symbols_count_sorted[i][0],symbols_count_sorted[i][1]))
	
print nodeList1

nodek = BT_Node(nodeList1[0],nodeList1[1], nodeList1[0].prob+nodeList1[1].prob)
print nodek 
nodeList1.insert(0,nodek)

print nodeList1
print "\r\n"

nodeList2=[]
for i in range(len(symbols_count_sorted)):
	nodeList2.append( BT_Leaf (symbols_count_sorted[i][0],symbols_count_sorted[i][1]))
	
print nodeList2
# Objects' list sorting test
#nodeList2 = list() #list() or [] -> defining list
#
#nodeList1.insert(2, BT_Leaf(55, 8))
#print nodeList1
#nodeList2 = sorted(nodeList1, key=lambda x: x.prob, reverse=False)
#print nodeList2





