import unittest


def is_valid(string):

    # Determine if the input code is valid
    brackets = []
    bracket_map = {
        '(': 0,
        '{': 0,
        '[': 0,
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for ch in string:
        if ch in bracket_map:
            brack = bracket_map[ch]
            if brack == 0:
                brackets.append(ch)
            else:
                if len(brackets) <= 0:
                    return False
                top = brackets.pop()
                if brack != top:
                    return False
    if len(brackets) == 0:
        return True

    return False


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)