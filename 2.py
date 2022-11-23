import heapq

class Node():
    def __init__(self, char, freq, left=None, right=None, code=''):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.code = code
        
    def __lt__(self, other):
        return self.freq < other.freq

    
chars = ['a','b','c','d','e','f','g']
freqs = [5,6,1,9,3,2,9]
nodes = []

for i in range(len(chars)):
    newnode = Node(chars[i], freqs[i])
    heapq.heappush(nodes, newnode)
    
while len(nodes) > 1:
    nn1 = heapq.heappop(nodes)
    nn2 = heapq.heappop(nodes)
    nn1.code = '0'
    nn2.code = '1'
    newnode = Node(nn1.char + nn2.char, nn1.freq + nn2.freq, nn1, nn2)
    heapq.heappush(nodes, newnode)
    
def printnodes(root,code=''):
    code += root.code
    if root.left:
        printnodes(root.left, code)
    if root.right:
        printnodes(root.right, code)
    elif (not root.left) and (not root.right):
        print(root.char,":", root.freq, ":", code)
        
printnodes(nodes[0])