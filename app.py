import sqlite3
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="public", static_url_path="")


# OOP: all SQL lives in one class
class ExpenseRepository:
    def __init__(self, file):
        self.file = file
        with self._connect() as db:
            db.execute(
                """CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL CHECK (amount > 0),
                    category TEXT NOT NULL,
                    spent_on TEXT NOT NULL
                )"""
            )

    def _connect(self):
        db = sqlite3.connect(self.file)
        db.row_factory = sqlite3.Row
        return db

    def _query(self, sql, params=()):
        db = self._connect()
        try:
            return [dict(row) for row in db.execute(sql, params).fetchall()]
        finally:
            db.close()

    def all(self):
        return self._query("SELECT * FROM expenses ORDER BY spent_on DESC, id DESC")

    def add(self, title, amount, category, spent_on):
        with self._connect() as db:
            cur = db.execute(
                "INSERT INTO expenses (title, amount, category, spent_on) VALUES (?, ?, ?, ?)",
                (title, amount, category, spent_on),
            )
            return cur.lastrowid

    def remove(self, expense_id):
        with self._connect() as db:
            return db.execute("DELETE FROM expenses WHERE id = ?", (expense_id,)).rowcount

    def by_category(self):
        return self._query(
            "SELECT category, SUM(amount) AS total, COUNT(*) AS count "
            "FROM expenses GROUP BY category ORDER BY total DESC"
        )

    def by_month(self):
        return self._query(
            "SELECT strftime('%Y-%m', spent_on) AS month, SUM(amount) AS total "
            "FROM expenses GROUP BY month ORDER BY month DESC"
        )


repo = ExpenseRepository("expenses.db")


@app.get("/")
def home():
    return send_from_directory("public", "index.html")


@app.get("/api/expenses")
def list_expenses():
    return jsonify(repo.all())


@app.post("/api/expenses")
def add_expense():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    category = data.get("category")
    spent_on = data.get("spent_on")
    try:
        amount = float(data.get("amount"))
    except (TypeError, ValueError):
        amount = 0
    if not title or not category or not spent_on or amount <= 0:
        return jsonify(error="Title, category, date and an amount above 0 are required."), 400
    return jsonify(id=repo.add(title, amount, category, spent_on)), 201


@app.delete("/api/expenses/<int:expense_id>")
def delete_expense(expense_id):
    removed = repo.remove(expense_id)
    return jsonify(removed=removed), (200 if removed else 404)


@app.get("/api/summary")
def summary():
    by_category = repo.by_category()
    return jsonify(
        total=sum(c["total"] for c in by_category),
        byCategory=by_category,
        byMonth=repo.by_month(),
    )


if __name__ == "__main__":
    app.run(port=3000, debug=True)
