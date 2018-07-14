import unittest


def binary(num):
	arr=[0,0,0,0,0,0,0,0]
	count=7
	while num!=0:
		r=num%2
		num=num//2
		arr[count]=arr[count]+r
		count=count-1
		# print(arr)
	return arr

def hamming_distance(x,y):
	x_binary=binary(x)
	y_binary=binary(y)
	count=0
	# print(x_binary)
	# print(y_binary)
	for i in range(0,8):
		if x_binary[i]!=y_binary[i]:
			count=count+1
			# print(count)
	return count







class Test(unittest.TestCase):

    def testcase_1(self):
        actual = hamming_distance(25,30)
        expected = 3
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = hamming_distance(1,4)
        expected = 2
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = hamming_distance(25,30)
        expected = 3
        self.assertEqual(actual, expected)

    def testcase_4(self):
        actual = hamming_distance(100,250)
        expected = 5
        self.assertEqual(actual, expected)

    def testcase_5(self):
        actual = hamming_distance(1,30)
        expected = 5
        self.assertEqual(actual, expected)

    def testcase_6(self):
        actual = hamming_distance(0,255)
        expected = 8
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)