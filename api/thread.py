from flask import request, redirect
from database import get_db
from datetime import datetime, timezone
import nanoid


def add_new_thread(board_id):
    try:
        db = get_db()
        now_timestamp = datetime.now(timezone.utc).timestamp()
        db.cursor().execute(
            """
            INSERT INTO Thread(
                _id, board_id, text, created_on, bumped_on, reported, delete_password
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                nanoid.generate(),
                board_id,
                request.form["text"],
                now_timestamp,
                now_timestamp,
                False,
                request.form["delete_password"],
            ),
        )
        db.commit()

        return redirect(f"/b/{board_id}/")

    except:
        return {"error": "Database error"}


def get_recent_threads(board_id):
    pass


def report_thread(board_id):
    pass


def delete_thread(board_id):
    pass
