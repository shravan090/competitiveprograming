import unittest

def gap(n):
	b=bin(n)
	# print(b[2:])
	if(n<0):
		b=b[1:]
	count=0
	result=0
	flag=1
	for i in range(len(b[2:])):
		if i!=0:
			if b[2+i]=='0':
				count=count+1
			else:
				count=count+1
				if(result<=count):
					result=count
				flag=0
		if(flag==0):
			count=0
			flag=1
	return result







class Test(unittest.TestCase):

    def testcase1(self):
        actual = gap(0)
        expected = 0
        self.assertEqual(actual, expected)

    def testcase2(self):
        actual = gap(55)
        expected = 2
        self.assertEqual(actual, expected)

    def testcase3(self):
        actual = gap(-5)
        expected = 2
        self.assertEqual(actual, expected)

    def testcase4(self):
        actual = gap(12354)
        expected = 6
        self.assertEqual(actual, expected)

    def testcase5(self):
        actual = gap(6)
        expected = 1
        self.assertEqual(actual, expected)

    def testcase6(self):
        actual = gap(256)
        expected = 0
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)