import storage
from habit import Habit
from datetime import datetime

class HabitTracker:
    def __init__(self):
        storage.initialize_db()

    def create_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        storage.insert_habit(habit)
        return habit

    def complete_habit(self, name):
        timestamp = datetime.now()
        storage.insert_checkoff(name, timestamp)

    def get_all_habits(self):
        return storage.load_all_habits()

    def get_checkoffs(self, name):
        return storage.get_checkoffs_for_habit(name)
    
if __name__ == "__main__":
    print("✅ tracker.py runs successfully!")
