import unittest


def reconstruct(list):
    list=sorted(list)
    list.reverse()
    for i in range(len(list)-1):
        if(list[i][0]==list[i+1][0]):
            if(list[i][1]>list[i+1][1]):
                list[i],list[i+1]=list[i+1],list[i]
                i=0
    result = []
    for people in list:
        result.insert(people[1], people)
    return result
    pass
















class Test(unittest.TestCase):

    def testcase_1(self):
        actual = reconstruct([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
        expected = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        self.assertEqual(actual, expected)

    def testcase_2(self):
        actual = reconstruct([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
        expected = [[12,0],[11,1],[9,2],[6,3],[3,4],[1,5]]
        self.assertEqual(actual, expected)

    def testcase_3(self):
        actual = reconstruct([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])
        expected = [[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)