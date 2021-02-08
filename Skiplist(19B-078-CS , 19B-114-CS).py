# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:24:45 2021

@author: DELL
"""

#IMPLEMENTATION OF SKIP LIST

#STEP 1

#Import random (for height of a node)

import random

class Node:
    def __init__(self,key,lev):
        self.key = key
        self.next=[None]*(lev+1)
        
# MAIN CLASS OF SKIP LIST
        
class SkipList:
    def __init__(self,maximum_lev,P):
        #initilizing maximum level for skiplist
        self.maximum_lev = maximum_lev
        #initializing P which denote the fraction node with its level
        self.P = P
        #current level of skiplist 
        self.lev = 0
        # creating header node (sentinal)
        self.header = self.Pre_Node(self.maximum_lev,-1)
        
    # create pre node(sentinal)
    def Pre_Node(self,level,key):
        new = Node(key,level)
        return new
    
    # creating Random level of skip list(Height)
    def Pick_Height(self):
        level = 0
        while random.random() < self.P and level < self.maximum_lev:
            level = level + 1
        return level
    
#OPERATIONS OF SKIPLISTS
    
    #Add (inserting keys in a skiplist)
    def Add(self,key):
        
        #create update and current 
        update = [None]*(self.maximum_lev+1)
        curr = self.header
        
        # it start from highest level ,move the current one next while key is 
        #greater than key of node next to current 
        #otherwise inserted in current update
        #move one level down and again search
        for i in range(self.lev,-1,-1):
            while curr.next[i] and curr.next[i].key < key:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        
        #if current is null that means we have reached to end of the leve;
        
        #or maybe current 's key is not equal to that key 
        #means we have to insert between mode update and current node
        if curr == None or curr.key != key:
            
            #generate a random level for that node
            ram_level = self.Pick_Height()
            if ram_level > self.lev:
                for i in range(self.lev +1,ram_level+1):
                    update[i] = self.header
                self.lev = ram_level
            
            #node with random level 
            new_node = self.Pre_Node(ram_level,key)
            
            for i in range(ram_level+1):
                new_node.next[i] = update[i].next[i]
                update[i].next[i] = new_node
                
            print("Insertion of key: {}".format(key))
    
    
    # find (search operation)        
    def Find(self,key):
        curr = self.header
        
        #Start at the top of the sentinel (curr), 
        #move the curr reference next while key is 
        #greater than key of node next to curr otherwise
        #inserted curr in update and move one level down 
        #and continue the searching.
        for i in range(self.lev, -1 , -1):
            while(curr.next[i] and curr.next[i].key < key):
                curr = curr.next[i]
        
        #Reaching at level 0 and here we get our desired node,
        curr = curr.next[0]
        
        #If curr node have key equal to our desired key,
        if curr and curr.key == key:
            #return key
            print("\nYeah! key is found --> ",key)
        else:
            #Not found statement 
            print("Sorry! Your desired key {} is not found!".format(key))
            
    #remove (delete operation)
    def remove(self,x):
        update = [None]*(self.maximum_lev+1)
        curr = self.header
        
        #search from start highest level move right while key is greater
        #than key of node next to current
        # otherwise inserted current in update and move one level down and search continue
        for i in range(self.lev,-1,-1):
            while(curr.next[i] and curr.next[i].key < x ):
                curr = curr.next[i]
            update[i] = curr
            
        #Reaching at level 0 and here we get our desired node,
        curr = curr.next[0]
        
        # if the curr node is our desire node
        if curr!= None and curr.key== x:
            for i in range(self.lev+1):
                if update[i].next[i] != curr:
                    break
                update[i].next[i]= curr.next[i]
        
        #removing all the levels of that deleted node
        while (self.lev > 0 and self.header.next[self.lev] == None):
            self.lev = self.lev-1
        print("Opps! we have deleted {}".format(x))
        
    #level wise skiplist
    def Print(self):
        print("\nSKIP LIST REPRESENTATION\n")
        h = self.header
        for level in range(self.lev+1):
            print("Level {}:".format(level),end=" ")
            node = h.next[level]
            while (node != None):
                print(node.key,end =" ")
                node = node.next[level]
            print("")
            
            
            
    
#Driver Code        
            
maximum_lev=int(input("Enter the levels : "))               
main = SkipList(maximum_lev,0.5)
print("---------------------------------------------------")
print("\nINSERTION")
main.Add(3)
main.Add(5)
main.Add(7)
main.Add(1)
main.Add(15)
main.Add(25)
main.Add(28)
main.Add(30)
main.Print()
print("---------------------------------------------------")
print("\nSEARCHING")
main.Find(50) 
main.Find(5)  
print("---------------------------------------------------")        
print("\nDELETION")                
main.remove(15)
main.Print()                    
                    
                    
                    
                    
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
        