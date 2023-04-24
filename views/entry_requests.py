import sqlite3
import json
from models import Entry

ENTRIES = [
    {
        "id": 1,
        "concept": "Snickers",
        "entry": "Dog",
        "date": 4,
        "mood_id": 1
    }
]


def get_all_entries():
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
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entry e
        """)

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entries class above.
            entry = Entry(
                row['id'], row['concept'], row['entry'], row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    return entries
