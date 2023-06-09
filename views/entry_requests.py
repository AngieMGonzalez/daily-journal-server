import sqlite3
import json
from models import Entry, Mood

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
            e.mood_id,
            m.label
        FROM entry e
        JOIN mood m
            ON m.id = e.mood_id
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
            
            mood = Mood(
                row['mood_id'], row['label']
            )

            # Add the dictionary representation of the mood to the entry
            entry.mood = mood.__dict__

            # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)

    return entries

def get_single_entry(id):
    """get single entry SQL
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label
        FROM entry e
        JOIN mood m
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['concept'], data['entry'],
                            data['date'], data['mood_id'])

        mood = Mood(
                data['mood_id'], data['label']
            )

        entry.mood = mood.__dict__

        return entry.__dict__

def delete_entry(id):
    """
    deletes a row from the DB
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))

def get_entries_by_search(search_term):
    """gets each entry by searched parameter
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
        WHERE e.entry LIKE ? OR e.concept LIKE ?
        """, ('%' + search_term + '%', '%' + search_term + '%'))

        # Initialize an empty list to hold all animal representations
        entries = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['mood_id'])

            entries.append(entry.__dict__)

    return entries

def create_entry(new_entry):
    """GET POST new resource
    """
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            ( concept, entry, date, mood_id )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_entry['concept'], new_entry['entry'],
            new_entry['date'], new_entry['mood_id'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id

    return new_entry
