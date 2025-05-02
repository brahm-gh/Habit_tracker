from functools import reduce
from datetime import datetime, timedelta

def get_all_habits(tracker):
    return tracker.get_all_habits()

def filter_by_periodicity(habits, period):
    return list(filter(lambda h: h.periodicity == period, habits))

def calculate_streak(checkoffs, period):
    if period == 'daily':
        delta = timedelta(days=1)
    else:
        delta = timedelta(weeks=1)

    sorted_dates = sorted(checkoffs, reverse=True)
    streak = 0
    today = datetime.now().date()

    for date in sorted_dates:
        if today - date.date() <= delta:
            streak += 1
            today = date.date() - delta
        else:
            break
    return streak

def longest_streak(tracker):
    habits = tracker.get_all_habits()
    return max(
        [calculate_streak(tracker.get_checkoffs(h.name), h.periodicity) for h in habits],
        default=0
    )

def longest_streak_for_habit(tracker, habit_name):
    habit = next(h for h in tracker.get_all_habits() if h.name == habit_name)
    return calculate_streak(tracker.get_checkoffs(habit.name), habit.periodicity)
