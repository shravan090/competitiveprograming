import unittest

def my_anagram(s,t):
	temp=s.split()
	s=''
	for i in temp:
		s=s+i
	temp=t.split()
	t=''
	for i in temp:
		t=t+i
	l1=list(s)
	list1=[i.lower() for i in l1]; l1
	l2=list(t)
	list2=[i.lower() for i in l2]; l2
	dict1={}
	dict2={}
	for i in list1:
		if i in dict1.keys():
			dict1[i]=dict1[i]+1
		else:
			dict1[i]=1
	for i in list2:
		if i in dict2.keys():
			dict2[i]=dict2[i]+1
		else:
			dict2[i]=1
	return dict1==dict2

class Test(unittest.TestCase):

    def testcase_1(self):
        actual = my_anagram('anagram','nagaram')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = my_anagram('Keep', 'Peek')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = my_anagram('Mother In Law', 'Hitler Woman')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_4(self):
        actual = my_anagram('School Master', 'The Classroom')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_5(self):
        actual = my_anagram('ASTRONOMERS', 'NO MORE STARS')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_6(self):
        actual = my_anagram('Toss', 'Shot')
        expected = False
        self.assertEqual(actual, expected)

    def testcase_7(self):
        actual = my_anagram('joy', 'enjoy')
        expected = False
        self.assertEqual(actual, expected)

    def testcase_8(self):
        actual = my_anagram('Debit Card', 'Bad Credit')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_9(self):
        actual = my_anagram('SiLeNt CAT', 'LisTen AcT')
        expected = True
        self.assertEqual(actual, expected)

    def testcase_10(self):
        actual = my_anagram('Dormitory', 'Dirty Room')
        expected = True
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)