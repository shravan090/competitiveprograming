import unittest
def words(arr):
	d=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	temp=[]
	for i in arr:
		l=list(i)
		a=''
		for j in l:
			a=a+d[ord(j)-97]
		if a not in temp:
			temp.append(a)
	return len(temp)




























class Test(unittest.TestCase):

    def testcase_1(self):
        actual = words(["gin", "zen", "gig", "msg"])
        expected = 2
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = words(["a", "z", "g", "m"])
        expected = 4
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = words(["bhi", "vsv", "sgh", "vbi"]  )
        expected = 3
        self.assertEqual(actual, expected)

    def testcase_4(self):
        actual = words(["a", "b", "c", "d"]  )
        expected = 4
        self.assertEqual(actual, expected)

    def testcase_5(self):
        actual = words(["hig", "sip", "pot"]  )
        expected = 2
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)