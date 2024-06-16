#!/usr/bin/env python3


#linked list node to store a queue entry
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class for queue
class Queue:

    #constructor for queue
    def __init__(self):
        self.front = self.rear = None

    # method to check if the queue is empty
    def isEmpty(self):
        return self.front == None

    #method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item) #create a new LL node

        if self.rear == None: #check if the queue is empty
            self.front = self.rear = temp #if the queue is empty, then both front and rear are the new node
            return
        self.rear.next = temp #add the new node to the rear of the queue
        self.rear = temp #update the rear of the queue

    #method to remove an item from the queue
    def DeQueue(self):
        if self.isEmpty(): #check if the queue is empty
            return
        temp = self.front #store the front node
        self.front = temp  = temp.next #update the front node and remove the previous front node

        if (self.front == None): #check if the queue is empty after removing the front node
            self.rear = None #if the queue is empty, update the rear node

#driver code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue("Luis")
    q.EnQueue("Miguel")
    q.EnQueue("Carlos")
    q.EnQueue("Juan")

    print("Queue Front: " + str(q.front.data if q.front != None else -1))
    print("Queue Rear: " + str(q.rear.data if q.rear != None else -1))
