import unittest
def check(dict1,list,num):
    if num>=len(list):
        return
    if dict1[num]==1:
        return
    else:
        dict1[num]=1
    for j in list[num]:
        check(dict1,list,j)

def keys_and_rooms(list):
    dict1={}
    for i in range(len(list)):
        if i==0:
            dict1[i]=1
        else:
            dict1[i]=0
    for i in list[0]:
        check(dict1,list,i)
    if 0 in dict1.values():
        return False
    else:
        return True





class Test(unittest.TestCase):

    def testcase_1(self):
        actual = keys_and_rooms([[1], [0,2], [3]])
        expected = True
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = keys_and_rooms([[1,3], [3,0,1], [2], [0]])
        expected = False
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = keys_and_rooms([[1,2,3], [0], [0], [0]])
        expected = True
        self.assertEqual(actual, expected)

    def testcase_4(self):
        actual = keys_and_rooms([[1], [0,2,4], [1,3,4], [2], [1,2]])
        expected = True
        self.assertEqual(actual, expected)

    def testcase_5(self):
        actual = keys_and_rooms([[1], [2,3], [1,2], [4], [1], [5]])
        expected = False
        self.assertEqual(actual, expected)

    def testcase_6(self):
        actual = keys_and_rooms([[1], [2], [3], [4], [2]])
        expected = True
        self.assertEqual(actual, expected)

    def testcase_7(self):
        actual = keys_and_rooms([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]])
        expected = False
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)