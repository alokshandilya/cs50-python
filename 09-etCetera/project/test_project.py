import unittest
from unittest.mock import patch, mock_open
import project


class TestTasker(unittest.TestCase):

    def test_load_tasks(self):
        with patch("builtins.open", mock_open(read_data="[]")):
            tasks = project.load_tasks()
            self.assertEqual(tasks, [])

    @patch("builtins.input", side_effect=["Task 1"])
    def test_add_task(self, mock_input):
        tasks = []
        project.add_task(tasks)
        self.assertEqual(tasks, [{"task": "Task 1", "completed": False}])

    @patch("builtins.input", side_effect=["2"])
    def test_mark_task_completed(self, mock_input):
        tasks = [
            {"task": "Task 1", "completed": False},
            {"task": "Task 2", "completed": False},
        ]
        project.mark_task_completed(tasks)
        self.assertTrue(tasks[1]["completed"])


if __name__ == "__main__":
    unittest.main()
