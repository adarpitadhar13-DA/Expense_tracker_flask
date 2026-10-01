# Expense Tracker (JavaScript + Python + SQL)

A full-stack expense tracker. The front end is HTML, CSS and JavaScript. The back end is Python with Flask and a SQLite (SQL) database.

## Run it
1. Install Python 3.9 or later.
2. In this folder run: `pip install -r requirements.txt`
3. Then run: `python app.py`
4. Open http://localhost:3000

## What it shows
- SQL: CREATE TABLE with constraints, INSERT, SELECT, DELETE, GROUP BY with SUM and COUNT, and date grouping with strftime
- JavaScript: fetch with async/await, DOM updates, and form handling
- Python: a class-based data layer (OOP) and a REST API with input validation

## API
- GET /api/expenses
- POST /api/expenses
- DELETE /api/expenses/<id>
- GET /api/summary
