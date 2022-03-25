class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right=None
    def n(self):
        node = self
        score=0
        while node != None:
            print (node.val) 
            s1=input("answer?") 
            s2=input("Ture or False (T or F)=") 
            if s2=="T":
                node = node.left
                score=score+1
                print("score=",score)
                print("----------------------")
            else:
                node = node.right
                print("score=",score)
                print("--------Finish--------------")
            
            if node==None:
                print("--------Finish--------------")


q1="q1:2+5=?"
q2="q2:2-4=?"
q3="q3:2*3=?"
q4="q4:6/3=?"
q5="q5:(6/2)-2=?"
q6="q5:(6*2)+2=?"
node1=Node(q1)
node2=Node(q2)
node3=Node(q3)
node4=Node(q4)
node5=Node(q5)
node6=Node(q6)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node5
node4.left=node5
node4.right=node6
node5.left=node6
node1.n()