import unittest

def water(arr):
    n=len(arr)
    left=[0]*n
    right=[0]*n
    left[0]=arr[0]
    for i in range(1,n):
        left[i]=max(left[i-1],arr[i])
    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],arr[i])
    water=0
    for i in range(0,n):
        water+=min(left[i],right[i])-arr[i]
    return water










class Test(unittest.TestCase):

    def testcase_1(self):
        actual = water([0, 1, 0, 2, 1, 0, 1])
        expected = 2
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        expected = 6
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = water([0, 1, 0, 2, 1, 0, 5, 1, 0, 2])
        expected = 7
        self.assertEqual(actual, expected)

    def testcase_4(self):
        actual = water([0, 1, 0, 5, 1, 0, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def testcase_5(self):
        actual = water([0, 5, 1, 3, 4, 0, 1])
        expected = 5
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)