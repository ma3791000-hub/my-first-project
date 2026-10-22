import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import storage
import tasks


class TestTasks(unittest.TestCase):

    def setUp(self):

        storage.tasks.clear()
        patcher = patch("storage.save_data")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_add_task(self):

        success, message = tasks.add_task(
            "Python Assignment",
            "Computer",
            "10-09-2026",
            "High"
        )

        self.assertTrue(success)
        self.assertEqual(
            len(storage.tasks),
            1
        )

        self.assertEqual(
            storage.tasks[0]["title"],
            "Python Assignment"
        )

        self.assertEqual(
            storage.tasks[0]["subject"],
            "Computer"
        )

        self.assertEqual(
            storage.tasks[0]["due date"],
            "10-09-2026"
        )

        self.assertEqual(
            storage.tasks[0]["priority"],
            "High"
        )

        self.assertEqual(
            storage.tasks[0]["status"],
            "pending"
        )

    def test_complete_task(self):

        tasks.add_task(
            "Python Assignment",
            "Computer",
            "10-09-2026",
            "High"
        )

        success, message = tasks.complete_task(
            "Python Assignment"
        )

        self.assertTrue(success)

        self.assertEqual(
            storage.tasks[0]["status"],
            "completed"
        )

    def test_complete_non_existing_task(self):

        success, message = tasks.complete_task(
            "Not Available"
        )

        self.assertFalse(success)

        self.assertEqual(
            len(storage.tasks),
            0
        )

    def test_search_task(self):
        tasks.add_task("Python Assignment", "Computer", "10-09-2026", "High")
        self.assertEqual(len(tasks.search_tasks("python")), 1)

    def test_invalid_date(self):
        success, message = tasks.add_task("A", "B", "2026-09-10", "High")
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()