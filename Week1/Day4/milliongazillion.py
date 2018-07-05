
import unittest

class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.EndofWord = False


class Trie(object):

    def __init__(self):
        self.root = self.getNode()
    # Implement a trie and use it to efficiently store strings

    def add_word(self, word):
        return False

    def getNode(self):
        return TrieNode()
    def _chartoindex(self,ch):
        return ord(ch)-ord('a')
    def add_word(self,word):
        if self.search(word):
            return False
        else :
            crawl = self.root
            word_length = len(word)
            for i in range(word_length):
                index = self._chartoindex(word[i])
                if not crawl.child[index]:
                    crawl.child[index]=self.getNode()
                crawl = crawl.child[index]
            crawl.EndofWord=True
            return True
    def search(self,word):
        crawl = self.root
        word_length = len (word)
        for i in range(word_length):
            index = self._chartoindex(word[i])
            if not crawl.child[index]:
                return False
            crawl = crawl.child[index]
        return crawl!=None and crawl.EndofWord







# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)