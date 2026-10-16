import unittest
import main


class TestTasks(unittest.TestCase):

    def setUp(self):

        main.tasks.clear()

    def test_add_task(self):

        success, message = main.add_task(
            "Python Assignment",
            "Computer",
            "10-09-2026",
            "High"
        )

        self.assertTrue(success)
        self.assertEqual(
            len(main.tasks),
            1
        )

        self.assertEqual(
            main.tasks[0]["title"],
            "Python Assignment"
        )

        self.assertEqual(
            main.tasks[0]["subject"],
            "Computer"
        )

        self.assertEqual(
            main.tasks[0]["due date"],
            "10-09-2026"
        )

        self.assertEqual(
            main.tasks[0]["priority"],
            "High"
        )

        self.assertEqual(
            main.tasks[0]["status"],
            "pending"
        )

    def test_complete_task(self):

        main.add_task(
            "Python Assignment",
            "Computer",
            "10-09-2026",
            "High"
        )

        success, message = main.complete_task(
            "Python Assignment"
        )

        self.assertTrue(success)

        self.assertEqual(
            main.tasks[0]["status"],
            "completed"
        )

    def test_complete_non_existing_task(self):

        success, message = main.complete_task(
            "Not Available"
        )

        self.assertFalse(success)

        self.assertEqual(
            len(main.tasks),
            0
        )


if __name__ == "__main__":
    unittest.main()