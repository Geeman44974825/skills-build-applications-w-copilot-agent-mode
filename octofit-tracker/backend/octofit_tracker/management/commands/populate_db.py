from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import datetime

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Create test users
        users_data = [
            {'username': 'coach_smith', 'email': 'smith@merington.edu', 'role': 'coach'},
            {'username': 'sarah_student', 'email': 'sarah@merington.edu', 'role': 'student'},
            {'username': 'mike_student', 'email': 'mike@merington.edu', 'role': 'student'},
            {'username': 'lisa_student', 'email': 'lisa@merington.edu', 'role': 'student'}
        ]

        users = []
        for user_data in users_data:
            user = User.objects.create(
                username=user_data['username'],
                email=user_data['email'],
                role=user_data['role']
            )
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')

        # Create test teams
        teams_data = [
            {'name': 'Track Stars', 'description': 'Track and Field Team'},
            {'name': 'Swimming Eagles', 'description': 'Swimming Team'},
            {'name': 'Basketball Heroes', 'description': 'Basketball Team'}
        ]

        teams = []
        for team_data in teams_data:
            team = Team.objects.create(
                name=team_data['name'],
                description=team_data['description']
            )
            teams.append(team)
            self.stdout.write(f'Created team: {team.name}')

        # Add users to teams
        teams[0].members.add(users[1], users[2])  # Track Stars
        teams[1].members.add(users[2], users[3])  # Swimming Eagles
        teams[2].members.add(users[1], users[3])  # Basketball Heroes

        # Create test activities
        activities_data = [
            {'name': 'Running', 'description': '5K run', 'duration': 30, 'distance': 5.0},
            {'name': 'Swimming', 'description': 'Freestyle laps', 'duration': 45, 'distance': 1.5},
            {'name': 'Basketball Practice', 'description': 'Team drills', 'duration': 60, 'distance': 0.0}
        ]

        for activity_data in activities_data:
            activity = Activity.objects.create(
                user=users[1],  # sarah_student
                name=activity_data['name'],
                description=activity_data['description'],
                duration=activity_data['duration'],
                distance=activity_data['distance'],
                date=datetime.date.today()
            )
            self.stdout.write(f'Created activity: {activity.name}')

        # Create test workouts
        workouts_data = [
            {'name': '5K Training', 'description': 'Endurance building workout for runners'},
            {'name': 'Swim Practice', 'description': 'Swimming technique improvement'},
            {'name': 'Basketball Drills', 'description': 'Basic basketball skills practice'}
        ]

        for workout_data in workouts_data:
            workout = Workout.objects.create(
                name=workout_data['name'],
                description=workout_data['description']
            )
            self.stdout.write(f'Created workout: {workout.name}')

        # Create leaderboard entries
        leaderboard_data = [
            {'user': users[1], 'points': 100, 'rank': 1},
            {'user': users[2], 'points': 85, 'rank': 2},
            {'user': users[3], 'points': 75, 'rank': 3}
        ]

        for leaderboard_entry in leaderboard_data:
            entry = Leaderboard.objects.create(
                user=leaderboard_entry['user'],
                points=leaderboard_entry['points'],
                rank=leaderboard_entry['rank']
            )
            self.stdout.write(f'Created leaderboard entry for: {entry.user.username}')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data'))
