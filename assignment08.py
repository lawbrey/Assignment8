from datalist import *
import json
from enum import Enum


class DictionaryEntry:
    COLON = ": "
    NEWLINE = "\n"

    def __init__(self, word, part_of_speech, definition, example=None):
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

    def __str__(self):
        line = ""
        entry = self.__dict__
        for key in entry:
            line += key.capitalize() + self.COLON + str(entry[key]) + self.NEWLINE
        return line


class LocalDictionary:
    def __init__(self, dictionary_json_name="dictionary.json"):
        self.dictionary = {}
        with open(dictionary_json_name) as file:
            json.load(file, object_hook=self.my_decode)

    def my_decode(self, o):
        if "word" in o:
            self.dictionary[o["word"]] = DictionaryEntry(**o)

    def search(self, word):
        return self.dictionary[word]


class DictionaryEntryCache(DataList):
    def __init__(self, capacity=10):
        # self.local_dictionary = LocalDictionary()
        super().__init__()
        self.count = 0
        if capacity >= 1:
            self.capacity = capacity
        else:
            raise ValueError

    def add(self, entry):
        if not isinstance(entry, DictionaryEntry):
            raise TypeError
        self.reset_current()
        if self.count < self.capacity:
            self.count += 1
        else:
            while True:
                node = self.iterate()
                if node.next is None:
                    self.remove(node.data)
                    break
        self.add_to_head(entry)

    def search(self, word):
        self.reset_current()
        while True:
            node = self.iterate()
            try:
                if word == node.data.word:
                    self.remove(node.data)
                    self.add_to_head(node.data)
                    return node.data
                if node.data is None:
                    raise KeyError("Word is not in Cache")
            except AttributeError:
                raise KeyError("Word is not in Cache") from None


class DictionarySource(Enum):
    LOCAL = 1
    CACHE = 2

    def __str__(self):
        return f"(Found in {self.name})"


class Dictionary:

    def __init__(self):
        self.loc_dict = LocalDictionary()
        self.dict_entry_cache = DictionaryEntryCache(1)

    def search(self, word):
        try:
            cache_entry = self.dict_entry_cache.search(word)
            return cache_entry, DictionarySource.CACHE
        except KeyError:
            try:
                local_entry = self.loc_dict.search(word)
                self.dict_entry_cache.add(local_entry)
                return local_entry, DictionarySource.LOCAL
            except Exception:
                raise KeyError("Word not found") from None


def main():
    NEWLINE = "\n"
    dictionary = Dictionary()
    while True:
        query = input("Enter a word to look up: ")
        try:
            for output in dictionary.search(query):
                print(output)
        except KeyError:
            print(f"Error when searching {query}")


if __name__ == '__main__':
    #main()
    print(type(LocalDictionary().search("ace").word))
    print(hasattr(LocalDictionary, "search"))
    print(LocalDictionary("dictionary.json").dictionary)

