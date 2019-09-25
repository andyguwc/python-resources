import unittest

from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def tearDown(self):
        pass

    @unittest.skip("bad example")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob","12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob","12345")

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary","12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary","12345")
        self.assertFalse(self.phonebook.is_consistent())

