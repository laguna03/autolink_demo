#!/usr/bin/env python3


# linked list node to store a queue entry
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


# A class to represent a queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Method to add an item to the queue
    def EnQueue(self):
        item = input("Enter the element to be added to the queue: ")
        new_node = Node(item)
        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Method to remove a specific item from the queue
    def DeQueue(self, x):
        if self.front is None:
            print("Queue is empty")
        else:
            if self.front.data == x:  # Check if the front item is the one to be dequeued
                print("Dequeued item is: ", self.front.data)
                print("-------------------------")
                self.front = self.front.next
                if self.front is None:  # If the queue is now empty, update the rear pointer
                    self.rear = None
            else:
                prev = self.front
                temp = self.front.next
                while temp is not None and temp.data != x:
                    prev = temp
                    temp = temp.next
                if temp is None:
                    print("Item not found in queue")
                else:
                    print("Dequeued item is: ", temp.data)
                    print("-------------------------")
                    prev.next = temp.next
                    if temp == self.rear:  # If the dequeued item was the rear, update the rear pointer
                        self.rear = prev


    # Method to display the queue
    def Display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Queue is: ")
            temp = self.front
            while temp:
                print(temp.data, end="\n")
                temp = temp.next
            print("front:", self.front.data, end="\n")
            print("rear:", self.rear.data, end="\n")
            print("-------------------------", end="\n")


# Driver code
q = Queue()
while 1:
    try:
        print("Enter option: ")
        print("1-Enqueue\n2-Dequeue\n3-Display\n4-Exit\n")
        print("-------------------------")
        option = int(input())
        if option == 1:
            print("Enqueued")
            print("-------------------------")
            q.EnQueue()
        elif option == 2:
            item = input("Enter the element to be removed from the queue: ")
            print("Dequeued")
            print("-------------------------")
            q.DeQueue(item)
        elif option == 3:
            print("Display")
            q.Display()
        elif option == 4:
            break
        else:
            print("Invalid option")
            print("-------------------------")
    except Exception as e:
        print("An error occurred: ", e)
