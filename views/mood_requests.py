import sqlite3
import json
from models import Mood

MOODS = [
    {
        "id": 1,
        "label": "Dogs"
    }
]


def get_all_moods():
    """get all SQL
    """
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM mood m
        """)

        # Initialize an empty list to hold all entry representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entries class above.
            mood = Mood(
                row['id'], row['label'])

            moods.append(mood.__dict__)

    return moods

def get_single_mood(id):
    """get single mood SQL
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM mood m
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        mood = Mood(data['id'], data['label'])

        return mood.__dict__

def delete_mood(id):
    """
    deletes a row from the DB
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM mood
        WHERE id = ?
        """, (id, ))
