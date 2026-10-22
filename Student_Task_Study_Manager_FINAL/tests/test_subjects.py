import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import storage
import subjects


class TestSubjects(unittest.TestCase):

    def setUp(self):
        storage.subjects.clear()
        patcher = patch("storage.save_data")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_add_subject(self):
        success, message = subjects.add_subject("Math")
        self.assertTrue(success)
        self.assertIn("Math", storage.subjects)

    def test_duplicate_subject(self):
        subjects.add_subject("Math")
        success, message = subjects.add_subject("Math")
        self.assertFalse(success)
        self.assertEqual(storage.subjects.count("Math"), 1)

    def test_empty_subject(self):
        success, message = subjects.add_subject("   ")
        self.assertFalse(success)

    def test_delete_subject(self):
        subjects.add_subject("Math")
        success, message = subjects.delete_subject("Math")
        self.assertTrue(success)
        self.assertNotIn("Math", storage.subjects)


if __name__ == "__main__":
    unittest.main()
