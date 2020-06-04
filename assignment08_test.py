import unittest
from datalist import *

from assignment08 import *
import json
from enum import Enum


class LocalDictionary(unittest.TestCase):
    def test_loading(self):
        self.assertTrue(LocalDictionary("dictionary.json"))
        # self.assertTrue(hasattr(LocalDictionary,'search'))
        with self.assertRaises(Exception):
            LocalDictionary().search("cat")
        with self.assertRaises(Exception):
            LocalDictionary("dog.json")

    # def test_lookup(self):
    # self.assertEqual(LocalDictionary().search("ace").word, "ace")


# for LocalDictionary, test that dictionary.json is loaded correctly, and definition lookup works.


if __name__ == '__main__':
    unittest.main()
