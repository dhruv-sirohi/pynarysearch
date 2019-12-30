import time as timeywimey

class node:

    def __init__(self, cargo = None, left = None, right = None):

            self.left = left
            self.right = right
            self.cargo = cargo
        
    def __str__ (self):
        
            return str(self.cargo)
        
    
    
class bst:


    def __init__(self,root = None):
        self.root = root

    def insert(self,val):
        if self.root == None:
            self.root = val
        else:
            self.insertHelper(self.root,val.cargo)
    def insertHelper(self, current_node, val):
        
        if val < current_node.cargo:
        
            if current_node.left == None:
        
                current_node.left = node(val)
        
            else:
                self.insertHelper(current_node.left,val)
        else:
            if current_node.right == None:
                current_node.right = node(val)
            else:
                self.insertHelper(current_node.right,val)

    def search(self, val):
        t0 = timeywimey.perf_counter()
        result = self.search_helper(self.root,val)
        
        if(result):
            
            t1 = timeywimey.perf_counter()
            dt = t1 - t0
            print('Time elapsed:', dt, 'seconds')
            return True
        else:
            
            t1 = timeywimey.perf_counter()
            dt = t1 - t0
            print('Time elapsed:', dt, 'seconds')
            return False
            
    def search_helper(self,curr_node,val):
        
        if curr_node == None:
            
            return False
        
        elif curr_node.cargo == (val):
            
            return True
        
        elif val > curr_node.cargo and curr_node.left is not None:
            
            return(self.search_helper(curr_node.right,val))
            
        elif val < curr_node.cargo and curr_node.left is not None:
            
            return(self.search_helper(curr_node.left,val))

def constructBST(fname):
    bst1= bst()
    with open(fname, 'r') as data_file:
            for line in data_file:
                text = line.strip()
                nodetoInsert = node(text)
                bst1.insert(nodetoInsert)
    return bst1





def merge(lis,lis2):
    #Want to merge l1 and l2
    #can only input 2 lists
    fulLis=[]
    if len(lis)==0 or len(lis2)==0:
        return fulLis
    else:
        if lis[0]<lis2[0]:
            fulLis.append(lis[0])
            del lis[0]
        else:
            fulLis.append(lis2[0])
            del lis2[0]
        return merge(lis,lis2)

def lisum(lis,total=0):
    if len(lis)==0:
        return total
    if (type(lis[0]) == list):
        for i in lis[0]:
            total += i
        throwaway = lis.pop(0)
        return lisum(lis,total)
    else:
        total+=lis.pop(0)
        return lisum(lis,total)
        





if __name__ == "__main__":
    print('Testing Functions')
