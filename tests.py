# -*- coding: utf-8 -*-

import unittest

from stack import Stack, StackPopException
from queue import Queue, QueueDequeueException


class StackTestCase(unittest.TestCase):

    def test_is_empty(self):
        stack = Stack()
        assert stack.is_empty() is True

        stack.push(1)
        assert stack.is_empty() is False

        stack.pop()
        assert stack.is_empty() is True

    def test_size(self):
        stack = Stack()
        assert len(stack) == 0

        stack.push(1)
        assert len(stack) == 1

        stack.pop()
        assert len(stack) == 0

    def test_push_items(self):
        stack = Stack()

        tests = [1, '0', Stack, lambda x: x, {}, [], None]

        for test in tests:
            stack.push(test)

        assert len(tests) == len(stack)

    def test_pop_items(self):
        stack = Stack()

        with self.assertRaises(StackPopException):
            stack.pop()

        one = 1
        two = 2

        stack.push(one)
        stack.push(two)

        assert len(stack) == 2

        assert stack.pop() == two
        assert stack.pop() == one

        assert len(stack) == 0

    def test_print(self):
        stack = Stack()

        assert str(stack) == ''

        stack.push(3)
        stack.push(1)
        stack.push(2)

        assert str(stack) == '2 -> 1 -> 3'


class QueueTestCase(unittest.TestCase):

    def test_is_empty(self):
        queue = Queue()
        assert queue.is_empty() is True

        queue.enqueue(1)
        assert queue.is_empty() is False

        queue.dequeue()
        assert queue.is_empty() is True

    def test_size(self):
        queue = Queue()
        assert len(queue) == 0

        queue.enqueue(1)
        assert len(queue) == 1

        queue.dequeue()
        assert len(queue) == 0

    def test_enqueue(self):
        queue = Queue()

        tests = [1, '0', Queue, lambda x: x, {}, [], None]

        for test in tests:
            queue.enqueue(test)

        assert len(tests) == len(queue)

    def test_dequeue(self):
        queue = Queue()

        with self.assertRaises(QueueDequeueException):
            queue.dequeue()

        one = 1
        two = 2

        queue.enqueue(one)
        queue.enqueue(two)

        assert len(queue) == 2

        assert queue.dequeue() == one
        assert queue.dequeue() == two

        assert len(queue) == 0

    def test_print(self):
        queue = Queue()

        assert str(queue) == ''

        queue.enqueue(3)
        queue.enqueue(1)
        queue.enqueue(2)

        assert str(queue) == '3 -> 1 -> 2'
