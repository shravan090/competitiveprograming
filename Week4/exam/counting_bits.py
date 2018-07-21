import unittest


def onecount(n):
	b=bin(n)
	count=0
	for i in b[2:]:
		if (i=="1"):
			count=count+1
	return count

		

def count(num):
	a=[]
	for i in range(num+1):
		a.append(onecount(i))
	return a




class Test(unittest.TestCase):

    def testcase1(self):
        actual = count(15)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        self.assertEqual(actual, expected)

    def testcase2(self):
        actual = count(16)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]
        self.assertEqual(actual, expected)

    def testcase3(self):
        actual = count(1)
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def testcase4(self):
        actual = count(25)
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3]
        self.assertEqual(actual, expected)

    def testcase5(self):
        actual = count(5)
        expected = [0, 1, 1, 2, 1, 2]
        self.assertEqual(actual, expected)

    def testcase6(self):
        actual = count(6)
        expected = [0, 1, 1, 2, 1, 2, 2]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)