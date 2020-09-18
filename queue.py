from node import Node


class Queue:
    def __init__(self):
        """
        Set first element on queue
        """
        self.first = None

    def enqueue(self, item):
        """
        Push items to queue

        If there's none, it becomes the first element
        If there are items, it goes to the end of the queue
        """
        if self.first == None:
            self.first = Node(load=item)
        else:
            last = self.first
            while last.next:
                last = last.next
            last.next = Node(load=item)

    def dequeue(self):
        """
        Pop items from stack

        If there's none, raises an error
        If there are items, pop the first one, and the next (second) becomes the first
        """
        if self.is_empty():
            raise QueueDequeueException()
        else:
            pop = self.first
            self.first = self.first.next
            return pop.load

    def is_empty(self):
        """
        Return True if there are no items on the queue and False if there are
        """
        return True if self.first == None else False

    def size(self):
        """
        Return how many elements there are on the queue
        """
        count = 0
        node = self.first
        while node:
            count += 1
            node = node.next
        return count

    def get_all(self):
        """
        Get elements on the queue interactively to serve on __str__
        """
        node = self.first
        while node:
            yield node
            node = node.next

    def __str__(self):
        """
        Return elements from queue separated by ->
        """
        return ' -> '.join(map(str, self.get_all()))


class QueueDequeueException(Exception):
    def __str__(self):
        """
        Return error message when dequeue is called and there are no items on queue
        """
        return "No item to dequeue!"


