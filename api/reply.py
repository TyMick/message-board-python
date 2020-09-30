from flask import request, redirect, jsonify
from database import get_db
from datetime import datetime, timezone
import nanoid
import sqlite3


def add_new_reply(board_id):
    try:
        db = get_db()
        c = db.cursor()

        now_timestamp = datetime.now(timezone.utc).timestamp()
        thread_id = request.form["thread_id"]
        text = request.form["text"]
        delete_password = request.form["delete_password"]
        c.execute(
            """
            INSERT INTO reply(
                board_id, thread_id, _id, text, created_on, delete_password, reported
            )
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (
                board_id,
                thread_id,
                nanoid.generate(),
                text,
                now_timestamp,
                delete_password,
                False,
            ),
        )
        c.execute(
            "UPDATE thread SET bumped_on = ? WHERE board_id == ? AND _id == ?",
            (now_timestamp, board_id, thread_id),
        )
        return redirect(f"/b/{board_id}/{thread_id}")
    
    except sqlite3.IntegrityError as e:
        if "FOREIGN KEY constraint failed" in e.args[0]:
            return {"error": "No such thread _id"}

    except:
        return {"error": "Database error"}


def get_thread_and_replies(board_id):
    pass


def report_reply(board_id):
    pass


def delete_reply(board_id):
    pass
