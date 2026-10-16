import unittest
from unittest.mock import patch
import main


class TestSubjects(unittest.TestCase):

    def test_add_subject(self):
        main.subjects.clear()

        with patch("builtins.input", return_value="Math"):
            main.add_subject()

        self.assertIn("Math", main.subjects)


def test_duplicate_subject(self):
    main.subjects.clear()
    main.subjects.append("Math")

    with patch("builtins.input", return_value="Math"):
        main.add_subject()
    self.assertEqual(main.subjects.count("Math"), 1)


if __name__ == "__main__":
    unittest.main()
