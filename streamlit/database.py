import sqlite3
import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

database_path = os.path.join(
    base_path,
    "cart2insights.db"
)

def get_connection():
    return sqlite3.connect(database_path)