import sqlite3
from pathlib import Path

DB_PATH = Path("app/database/orders.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)

    # Return rows like dictionaries
    conn.row_factory = sqlite3.Row

    return conn