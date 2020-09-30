# Python message board

[![Run on Repl.it](https://repl.it/badge/github/tywmick/message-board-python)](https://repl.it/github/tywmick/message-board-python)

This is a Python port of my [Node.js exercise tracker](https://ty-message-board.glitch.me/), built with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLite](https://sqlite.org/index.html). The front end API tests on the home page also uses [Bootstrap](https://getbootstrap.com/), [jQuery](https://jquery.com/), and [highlight.js](https://highlightjs.org/). The API fulfills the following user stories:

1.  I can **POST** a thread to a specific message board by passing form data `text` and `delete_password` to `/api/threads/{board}`. (Recomend `res.redirect` to board page `/b/{board}`) Saved will be `_id`, `text`, `created_on` (date&time), `bumped_on` (date&time, starts same as created_on), `reported` (boolean), `delete_password`, & `replies` (array).
2.  I can **POST** a reply to a thead on a specific board by passing form data `text`, `delete_password`, & `thread_id` to `/api/replies/{board}` and it will also update the `bumped_on` date to the comment's date. (Recomend `res.redirect` to thread page `/b/{board}/{thread_id}`) In the thread's `replies` array will be saved `_id`, `text`, `created_on`, `delete_password`, & `reported`.
3.  I can **GET** an array of the most recent 10 bumped threads on the board with only the most recent 3 replies from `/api/threads/{board}`. The `reported` and `delete_password` fields will not be sent.
4.  I can **GET** an entire thread with all its replies from `/api/replies/{board}?thread_id={thread_id}`. Also hiding the same fields.
5.  I can delete a thread completely if I send a **DELETE** request to `/api/threads/{board}` and pass along the `thread_id` & `delete_password`. (Text response will be `"incorrect password"` or `"success"`)
6.  I can delete a post (just changing the text to `"[deleted]"`) if I send a **DELETE** request to `/api/replies/{board}` and pass along the `thread_id`, `reply_id`, & `delete_password`. (Text response will be `"incorrect password"` or `"success"`)
7.  I can report a thread and change its `reported` value to `true` by sending a **PUT** request to `/api/threads/{board}` and passing along the `thread_id`. (Text response will be `"success"`)
8.  I can report a reply and change its `reported` value to `true` by sending a **PUT** request to `/api/replies/{board}` and passing along the `thread_id` & `reply_id`. (Text response will be `"success"`)
