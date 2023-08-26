#!/usr/bin/env python3

import io
import sys
import unittest
from count_sentences import MyString

class TestMyString(unittest.TestCase):
    '''Test MyString in count_sentences.py'''

    def test_not_a_string(self):
        '''prints "The value must be a string." if not string.'''
        value = MyString(123)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        value.is_string()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "The value must be a string.\n")

    def test_ends_with_period(self):
        '''returns True if value ends with a period and False otherwise.'''
        value = MyString("Hello world.")
        self.assertTrue(value.ends_with_period())
        value = MyString("Hello world")
        self.assertFalse(value.ends_with_period())

    def test_ends_with_question_mark(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        value = MyString("How are you?")
        self.assertTrue(value.ends_with_question_mark())
        value = MyString("How are you")
        self.assertFalse(value.ends_with_question_mark())

    def test_ends_with_exclamation_mark(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        value = MyString("Wow!")
        self.assertTrue(value.ends_with_exclamation_mark())
        value = MyString("Wow")
        self.assertFalse(value.ends_with_exclamation_mark())

    def test_count_sentences(self):
        '''returns the number of sentences in the value.'''
        value = MyString("This is a sentence. And another one!")
        self.assertEqual(value.count_sentences(), 2)

if __name__ == '__main__':
    unittest.main()
