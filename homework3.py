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
        node1 = Node(10)
        node2 = Node(20, node1, None)
        node3 = Node(30, node2, None)
        node4 = Node(40, node3, None)
        node5 = Node(50, node4, None)
        node6 = Node(60, node5, None)
        node7 = Node(70, node6, None)
        node8 = Node(80, node7, None)
        node9 = Node(90, node8, None)
        
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node7
        node7.next = node8
        node8.next = node9
        
        self.linkedlist = LinkedList(node1, node9)
        
    
    def tearDown(self):
        del node1, node2, node3, node4, node5,