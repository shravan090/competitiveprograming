import random


def shuffle(the_list):

    """in place shuffle of a the_list"""

    n = len(the_list)

    for i in xrange(0, n - 1):
        j = get_random(i, n - 1)
        # print("%s <--> %s" % (i, j))
        the_list[i], the_list[j] = the_list[j], the_list[i]

def get_random(floor, ceiling):
    """return a random number in the closed interval (floor, ceiling)"""
    return random.randint(floor, ceiling) 


sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list