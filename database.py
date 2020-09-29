from flask import g
import sqlite3

DATABASE = "message_board.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def init_db():
    db = get_db()
    c = db.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS Thread(
            _id TEXT UNIQUE NOT NULL,
            board_id TEXT NOT NULL,
            text TEXT NOT NULL,
            created_on DATETIME NOT NULL,
            bumped_on DATETIME NOT NULL,
            reported BOOLEAN NOT NULL,
            delete_password TEXT NOT NULL
        )
        """
    )
    c.execute("CREATE INDEX IF NOT EXISTS idx_board ON Thread(board_id)")

    db.commit()
