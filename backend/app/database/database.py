import sqlite3
from pathlib import Path

DB_PATH = Path("app/database/orders.db")


def get_connection():
    """
    Returns a SQLite connection.
    """

    return sqlite3.connect(DB_PATH)