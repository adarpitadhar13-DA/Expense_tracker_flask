# Expense Tracker (Flask + SQL)

A full-stack web app to record daily expenses and see where your money goes. The Flask back end exposes a REST API backed by an SQL database, and a JavaScript front end talks to it with `fetch` and `async/await`, so the page updates without reloading.

<img width="1302" height="821" alt="image" src="https://github.com/user-attachments/assets/6af1bae3-d1b8-4bdd-8246-56b1f6601dfd" />


## Features

- Add, view, and delete expenses (title, amount, category, date)
- Category-wise and monthly spending summaries using SQL `GROUP BY`, `SUM`, and `COUNT`
- Input validation on both the client (JavaScript) and the server (Flask)
- Data layer organised with Python classes (OOP)
- Responsive layout that works on desktop and mobile
- Updates the page without a reload using `fetch` and `async/await`

## Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Front end  | HTML, CSS, JavaScript     |
| Back end   | Python, Flask (REST API)  |
| Database   | SQLite, SQL               |

## Project Structure

```
expense_tracker_flask/
├── app.py              # Flask app and API routes
├── requirements.txt    # Python dependencies
├── public/             # Front end files (HTML, CSS, JS)
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/adarpitadhar13-DA/expense-tracker.git
cd expense-tracker

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## API Endpoints

> Update this table so the routes match the ones defined in `app.py`.

| Method | Endpoint             | Description                      |
|--------|----------------------|----------------------------------|
| GET    | `/api/expenses`      | List all expenses                |
| POST   | `/api/expenses`      | Add a new expense                |
| DELETE | `/api/expenses/<id>` | Delete an expense                |
| GET    | `/api/summary`       | Category-wise and monthly totals |

Example request body for adding an expense:

```json
{
  "title": "Lunch",
  "amount": 150,
  "category": "Food",
  "date": "2026-10-01"
}
```

## What I Learned

- Designing a REST API with Flask and connecting it to a SQL database
- Writing aggregate SQL queries (`GROUP BY`, `SUM`, `COUNT`) for summaries
- Structuring code with classes (OOP) instead of loose functions
- Validating input on both the client and the server
- Using `fetch` and `async/await` to build a front end that updates without reloads

## Future Improvements

- User login and per-user expense data
- Charts for monthly and category spending
- Edit existing expenses
- Export expenses to CSV

## Author

**Arpita Dhar**
[LinkedIn](https://www.linkedin.com/in/arpita-dhar-69570388) · [GitHub](https://github.com/adarpitadhar13-DA)
