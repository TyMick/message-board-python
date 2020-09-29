from flask import g
import sqlite3

DATABASE = "message_board.db"


def dict_factory(cursor, row):
    """
    Turns rows into dictionaries for easier JSON conversion. Plugs into
    Connection.row_factory.
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = dict_factory
    return db


def init_db():
    db = get_db()
    c = db.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS thread(
            _id TEXT PRIMARY KEY,
            board_id TEXT NOT NULL,
            text TEXT NOT NULL,
            created_on DATETIME NOT NULL,
            bumped_on DATETIME NOT NULL,
            reported BOOLEAN NOT NULL,
            delete_password TEXT NOT NULL
        ) WITHOUT ROWID
        """
    )
    threads = c.fetchall()
    # Create indices

    db.commit()
