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
    db.execute("PRAGMA foreign_keys = ON")
    return db


def init_db():
    db = get_db()
    c = db.cursor()
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS thread(
            board_id TEXT NOT NULL,
            _id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            created_on DATETIME NOT NULL,
            bumped_on DATETIME NOT NULL,
            reported BOOLEAN NOT NULL,
            delete_password TEXT NOT NULL
        ) WITHOUT ROWID;

        CREATE UNIQUE INDEX IF NOT EXISTS thread_idx ON thread(board_id, _id);
        CREATE INDEX IF NOT EXISTS thread_bump ON thread(board_id, _id, bumped_on);

        CREATE TABLE IF NOT EXISTS reply(
            _id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            created_on DATETIME NOT NULL,
            delete_password TEXT NOT NULL,
            reported BOOLEAN NOT NULL,
            board_id TEXT,
            thread_id TEXT,
            FOREIGN KEY(thread_id, board_id)
                REFERENCES thread(_id, board_id)
                ON DELETE CASCADE
        ) WITHOUT ROWID;

        CREATE UNIQUE INDEX IF NOT EXISTS reply_idx ON reply(board_id, thread_id, _id);
        CREATE INDEX IF NOT EXISTS reply_created
        ON reply(board_id, thread_id, _id, created_on);
        """
    )
    db.commit()
