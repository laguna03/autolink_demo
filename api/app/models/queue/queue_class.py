#!/usr/bin/env python3
class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue" % str(item))

    def DeQueue(self):
        if self.isEmpty():
            return
        print("%s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Front item is", self.Q[self.front])

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


if __name__ == '__main__':
    q = Queue(30)
    q.EnQueue("Luis")
    q.EnQueue("Miguel")
    q.EnQueue("Carlos")
    q.EnQueue("Juan")
    q.DeQueue()
    q.que_front()
    q.que_rear()
