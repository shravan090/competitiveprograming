import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        self.arr=[]
        self.dict={}

    def insert(self, temperature):
        self.arr.append(temperature)
        if temperature in self.dict:
            self.dict[temperature]+=1
        else:
            self.dict[temperature]=1
        pass

    def get_max(self):
        return max(self.arr)
        pass

    def get_min(self):
        return min(self.arr)
        pass

    def get_mean(self):
        return sum(self.arr)/len(self.arr)
        pass

    def get_mode(self):
        count=max(self.dict.values())
        return self.dict.keys()[self.dict.values().index(count)]
        
        pass

    # arr=[]














# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)