from flask import Flask, g, render_template
from database import init_db
from api.thread import add_new_thread, get_recent_threads, report_thread, delete_thread
from api.reply import add_new_reply, get_thread_and_replies, report_reply, delete_reply

app = Flask("app", static_folder="public", template_folder="views")

with app.app_context():
    init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/b/<board_id>")
def board(board_id):
    return render_template("board.html")


@app.route("/b/<board_id>/<thread_id>")
def thread(board_id, thread_id):
    return render_template("thread.html")


app.add_url_rule("/api/threads/<board_id>", view_func=add_new_thread, methods=["POST"])
app.add_url_rule(
    "/api/threads/<board_id>", view_func=get_recent_threads, methods=["GET"]
)
app.add_url_rule("/api/threads/<board_id>", view_func=report_thread, methods=["PUT"])
app.add_url_rule("/api/threads/<board_id>", view_func=delete_thread, methods=["DELETE"])


app.add_url_rule("/api/replies/<board_id>", view_func=add_new_reply, methods=["POST"])
app.add_url_rule(
    "/api/replies/<board_id>", view_func=get_thread_and_replies, methods=["GET"]
)
app.add_url_rule("/api/replies/<board_id>", view_func=report_reply, methods=["PUT"])
app.add_url_rule("/api/replies/<board_id>", view_func=delete_reply, methods=["DELETE"])


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
