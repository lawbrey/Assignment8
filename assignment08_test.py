"""
Luke Awbrey
CS3B, Assignment #8, Local Dictionary
6/3/2020
"""

import unittest

from assignment08 import *


class LocalDictionaryTestCase(unittest.TestCase):
    def test_loading(self):
        self.assertTrue(LocalDictionary("dictionary.json"))
        self.assertTrue(hasattr(LocalDictionary, 'search'))
        with self.assertRaises(Exception):
            LocalDictionary().search("cat")
        with self.assertRaises(Exception):
            LocalDictionary("dog.json")

    def test_lookup(self):
        self.assertEqual(LocalDictionary().dictionary["ace"].word, "ace")
        self.assertEqual(LocalDictionary().dictionary["fly"].example, "he was sent flying by the tackle")
        self.assertEqual(LocalDictionary().dictionary["brag"].part_of_speech, "verb")


class DictionaryEntryCacheTestCase(unittest.TestCase):
    def test_add(self):
        self.entry_1 = LocalDictionary().search("ace")
        self.entry_2 = LocalDictionary().search("fly")
        self.assertIsNone(DictionaryEntryCache().add(self.entry_1))

    def test_search(self):
        self.entry_1 = LocalDictionary().search("brag")
        self.entry_2 = LocalDictionary().search("fly")
        self.entry_3 = LocalDictionary().search("ace")
        self.test_cache = DictionaryEntryCache(2)
        self.test_cache.add(self.entry_1)
        self.test_cache.add(self.entry_2)
        self.assertEqual(self.test_cache.search("brag").word, "brag")
        self.assertEqual(self.test_cache.search("fly").word, "fly")
        self.test_cache.add(self.entry_3)
        with self.assertRaises(Exception):
            self.test_cache.search("brag")

        self.test_cache = DictionaryEntryCache(2)
        self.test_cache.add(self.entry_1)
        self.test_cache.add(self.entry_2)
        self.test_cache.search("brag")
        self.test_cache.add(self.entry_3)
        self.assertEqual(self.test_cache.search("brag").word, "brag")
        with self.assertRaises(Exception):
            self.test_cache.search("fly")


class DictionaryTest(unittest.TestCase):
    def test_lookup(self):
        self.dictionary_instance = Dictionary()
        self.assertEqual(self.dictionary_instance.search("ace")[1], DictionarySource.LOCAL)
        self.assertEqual(self.dictionary_instance.search("ace")[1], DictionarySource.CACHE)
        self.assertEqual(self.dictionary_instance.search("ace")[1], DictionarySource.CACHE)
        with self.assertRaises(Exception):
            self.dictionary_instance.search("ball")


if __name__ == '__main__':
    unittest.main()
