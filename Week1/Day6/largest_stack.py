import unittest


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)
        print(self.items)

    def pop(self):
        """Remove and return last item"""
      
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):
    

    def __init__(self):
        self.stack = Stack()
        self.max_ = -float('inf')

    def push(self, item):
        if self.max_ < item:
            self.stack.push((item, item))
            self.max_ = item
        else:
            self.stack.push((item, self.max_))

    def pop(self):
        return self.stack.pop()[0]

    def get_max(self):
        return self.stack.peek()[1]


# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)