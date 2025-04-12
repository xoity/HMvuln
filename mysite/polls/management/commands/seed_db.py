from django.core.management.base import BaseCommand
from django.db import connection
from django.utils import timezone
from polls.models import Question, Choice
import random

class Command(BaseCommand):
    help = 'Seeds the database with questions and creates a hidden flag table'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create some basic questions
        questions = [
            "What is your favorite programming language?",
            "Is Django the best web framework?",
            "How secure is your application?",
            "What is SQL injection?",
            "Can you find hidden tables in a database?"
        ]
        
        # Delete existing questions
        Question.objects.all().delete()
        
        # Create new questions and choices
        for q_text in questions:
            q = Question.objects.create(
                question_text=q_text,
                pub_date=timezone.now()
            )
            
            # Create some choices for each question
            choices = [
                "Yes, absolutely!",
                "No way!",
                "Maybe...",
                "I'm not sure."
            ]
            
            for choice_text in choices:
                Choice.objects.create(
                    question=q,
                    choice_text=choice_text,
                    votes=random.randint(0, 100)
                )
                
        # Create a hidden flag table using raw SQL
        with connection.cursor() as cursor:
            # Drop the table if it exists
            cursor.execute("DROP TABLE IF EXISTS ctf_flags")
            
            # Create the hidden table
            cursor.execute("""
                CREATE TABLE ctf_flags (
                    id INTEGER PRIMARY KEY,
                    flag TEXT,
                    hint TEXT
                )
            """)
            
            # Insert the flags
            cursor.execute("""
                INSERT INTO ctf_flags (flag, hint)
                VALUES 
                ('FLAG{SQLite_1nj3ct10n_m4st3r}', 'Congratulations! You found the main flag!'),
                ('FLAG{ju5t_4_d3c0y_fl4g}', 'This is not the flag you are looking for...'),
                ('FLAG{3num3r4t10n_c0mpl3t3}', 'You have successfully enumerated the database schema!')
            """)
            
        self.stdout.write(self.style.SUCCESS('Database successfully seeded with vulnerable data!'))
        self.stdout.write('Challenge is ready - users need to find hidden tables and extract the real flag.')
