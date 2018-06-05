# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:06:21 2018

@author: shaurmanchic
"""
import unittest


class LinkedList(object):
    def __init__(self, tail=None, head=None):
        self.head = head
        self.tail = tail
    
    def get(self, i):
        current_node = self.tail
        
        for index in range(1, i):
            current_node = current_node.next
            
        return current_node.value
    
    def put(self, i, val):
        current_node = self.tail
        
        for index in range(1, i):
            current_node = current_node.next
        
        previous_node = current_node.prev
        new_node = Node(val, previous_node, current_node)
        current_node.prev = new_node
        previous_node.next = new_node
    
    def delete(self, i):
        current_node = self.tail
        
        for index in range(1, i):
            current_node = current_node.next
        
        previous_node = current_node.prev
        current_node = current_node.next
        
        previous_node.next = current_node
        current_node.prev = previous_node
    
    def indexOf(self, el):
        current_node = self.tail
        current_index = 1        
        
        while current_node.value != el and current_node.next != None:
            current_index += 1
            current_node = current_node.next
        
        return current_index
    
    def size(self):
        current_node = self.tail
        size = 1
        
        while current_node.next != None:
            current_node = current_node.next
            size += 1
        
        return size

class Node(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.value)
        
        
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(10)
        self.node2 = Node(20, self.node1, None)
        self.node3 = Node(30, self.node2, None)
        
        self.node1.next = self.node2
        self.node2.next = self.node3
        
        self.linkedlist = LinkedList(self.node1, self.node3)
        
    
    def tearDown(self):
        del self.node1, self.node2, self.node3
        del self.linkedlist
    
    
    def testGet(self):
        self.assertEqual(self.linkedlist.get(1), 10)
        self.assertEqual(self.linkedlist.get(2), 20)
        self.assertEqual(self.linkedlist.get(3), 30)
    
    
    def testPut(self):
        self.linkedlist.put(2, 666)
        self.assertEqual(self.linkedlist.get(1), 10)
        self.assertEqual(self.linkedlist.get(2), 666)
        self.assertEqual(self.linkedlist.get(3), 20)
        self.assertEqual(self.linkedlist.get(4), 30)
        
    def testDelete(self):
        self.linkedlist.delete(2)
        self.assertEqual(self.linkedlist.get(1), 10)
        self.assertEqual(self.linkedlist.get(2), 30)
        
    def testIndexOf(self):
        self.assertEqual(self.linkedlist.indexOf(10), 1)
        self.assertEqual(self.linkedlist.indexOf(20), 2)
        self.assertEqual(self.linkedlist.indexOf(30), 3)
        
    def testSize(self):
        self.assertEqual(self.linkedlist.size(), 3)
        self.linkedlist.put(2, 666)
        self.assertEqual(self.linkedlist.size(), 4)
        self.linkedlist.delete(2)
        self.assertEqual(self.linkedlist.size(), 3)
    
if __name__ == '__main__':
    unittest.main()
