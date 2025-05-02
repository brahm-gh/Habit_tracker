import click
from tracker import HabitTracker
import analytics

tracker = HabitTracker()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('periodicity')
def create(name, periodicity):
    tracker.create_habit(name, periodicity)
    click.echo(f"Habit '{name}' created with periodicity '{periodicity}'.")

@cli.command()
@click.argument('name')
def complete(name):
    tracker.complete_habit(name)
    click.echo(f"Habit '{name}' marked as complete.")

@cli.command(name="list")
def list_habits():
    habits = tracker.get_all_habits()
    for habit in habits:
        click.echo(f"{habit.name} ({habit.periodicity}) created on {habit.created_at}")

@cli.command()
def analyze():
    click.echo(f"Longest overall streak: {analytics.longest_streak(tracker)}")

if __name__ == '__main__':
    cli()