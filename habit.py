from datetime import datetime

class Habit:
    def __init__(self, name, periodicity, created_at=None):
        self.name = name
        self.periodicity = periodicity  # 'daily' or 'weekly'
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_at': self.created_at.isoformat()
        }
