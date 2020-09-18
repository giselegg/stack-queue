from node import Node


class Stack:
    def __init__(self):
        """
        Set first element on stack
        """
        self.first = None

    def push(self, item):
        """
        Push items to stack

        If there's none, it becomes the first element
        If there are items, the new becomes the first, and the previous first becomes the second
        """
        if self.first == None:
            self.first = Node(load=item)
        else:
            new = Node(load=item)
            new.next = self.first
            self.first = new

    def pop(self):
        """
        Pop items from stack

        If there's none, raises an error
        If there are items, pop the first one, and the next (second) becomes the first
        """
        if self.is_empty():
            raise StackPopException()
        else:
            pop = self.first
            self.first = self.first.next
            return pop.load

    def is_empty(self):
        """
        Return True if there are no items on the stack and False if there are
        """
        return True if self.first == None else False

    def size(self):
        """
        Return how many elements there are on the stack
        """
        count = 0
        node = self.first
        while node:
            count += 1
            node = node.next
        return count

    def get_all(self):
        """
        Get elements on the stack interactively to serve on __str__
        """
        node = self.first
        while node:
            yield node
            node = node.next

    def __str__(self):
        """
        Return elements from stack separated by ->
        """
        return ' -> '.join(map(str, self.get_all()))


class StackPopException(Exception):
    def __str__(self):
        """
        Return error message when pop is called and there are no items on stack
        """
        return "No item to pop from stack!"



