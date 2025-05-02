import unittest
from tracker import HabitTracker
import uuid

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        # Reset DB before each test
        import sqlite3
        conn = sqlite3.connect('data/habits.db')
        c = conn.cursor()
        c.execute("DELETE FROM checkoffs")
        c.execute("DELETE FROM habits")
        conn.commit()
        conn.close()

        self.tracker = HabitTracker()
        self.tracker.create_habit("test_habit", "daily")

    def test_habit_creation(self):
        habits = self.tracker.get_all_habits()
        self.assertTrue(any(h.name == "test_habit" for h in habits))

    def test_complete_habit(self):
        self.tracker.complete_habit("test_habit")
        checkoffs = self.tracker.get_checkoffs("test_habit")
        self.assertGreater(len(checkoffs), 0)

if __name__ == "__main__":
    unittest.main()
