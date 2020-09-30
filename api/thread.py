from flask import request, redirect, jsonify
from database import get_db
from datetime import datetime, timezone
import nanoid


def add_new_thread(board_id):
    try:
        db = get_db()
        now_timestamp = datetime.now(timezone.utc).timestamp()
        db.cursor().execute(
            """
            INSERT INTO thread(
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

        return redirect(f"/b/{board_id}")

    except:
        return {"error": "Database error"}


def get_recent_threads(board_id):
    try:
        db = get_db()
        c = db.cursor()
        c.execute(
            r"""
            SELECT
                _id,
                text,
                strftime("%Y-%m-%dT%H:%M:%fZ", created_on, "unixepoch") AS created_on,
                strftime("%Y-%m-%dT%H:%M:%fZ", bumped_on, "unixepoch") AS bumped_on
            FROM thread
            WHERE board_id == ?
            ORDER BY bumped_on DESC
            LIMIT 10
            """,
            (board_id,),
        )
        return jsonify(c.fetchall())

    except:
        return {"error": "Database error"}


def report_thread(board_id):
    try:
        db = get_db()
        c = db.cursor()
        c.execute(
            "UPDATE thread SET reported = 1 WHERE board_id == ? AND _id == ?",
            (board_id, request.form["thread_id"]),
        )
        db.commit()

        c.execute("SELECT changes() AS rows_updated")
        if c.fetchone()["rows_updated"] > 0:
            return "Success"
        else:
            return "No such thread _id"

    except:
        return {"error": "Database error"}


def delete_thread(board_id):
    pass
