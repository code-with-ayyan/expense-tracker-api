<<<<<<< HEAD
# 📊 Expense Tracker API (FastAPI + SQLAlchemy)

A backend API for managing expenses with full CRUD support, filtering, sorting, search, and pagination.

---

## 📁 Project Structure

.
├── expenses
│   ├── controllers.py     # Business logic (CRUD + filters)
│   ├── models.py          # Database models (SQLAlchemy)
│   ├── router.py          # API routes
│   ├── schemas.py         # Pydantic validation
│
├── utils
│   ├── db.py             # Database connection
│   ├── setting.py        # Configuration (env, DB URL)
│
├── main.py              # FastAPI entry point
├── .gitignore
├── venv/ (ignored)

---

## ⚙️ Features

- Create expense
- Get all expenses
- Search by title
- Filter by category
- Sort by amount (asc/desc)
- Pagination support
- Proper error handling (404 if not found)

---

## 🚀 Installation

### 1. Clone repo
git clone <repo-url>
cd <project-folder>

### 2. Create virtual environment
python -m venv venv

Activate:

Linux/Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

---

## ▶️ Run Project

uvicorn main:app --reload

Open:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

### ➤ Create Expense
POST /expenses

Request Body:
{
  "title": "Milk",
  "amount": 200,
  "category": "food"
}

---

### ➤ Get All Expenses
GET /expenses

---

### ➤ Get Single Expense
GET /expenses/{id}

---

### ➤ Update Expense
PUT /expenses/{id}

Request Body:
{
  "title": "Updated Milk",
  "amount": 250,
  "category": "food"
}

---

### ➤ Delete Expense
DELETE /expenses/{id}

---

## 🔍 Query Parameters (GET /expenses)

| Param    | Type   | Description              |
|----------|--------|--------------------------|
| search   | string | Search by title          |
| category | string | Filter by category       |
| sort     | string | asc / desc by amount     |
| page     | int    | Page number              |
| limit    | int    | Items per page          |

---

### 🧠 Example Request

GET /expenses?search=milk&category=food&sort=asc&page=1&limit=5

---

## 📤 Example Response

```json
[
  {
    "id": 1,
    "title": "Milk",
    "amount": 200,
    "category": "food"
  }
]

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL

---

## 🚫 Important Notes

- venv/ is ignored using .gitignore
- __pycache__ is ignored
- Use .env for secrets (never commit)

---

## 📈 Future Improvements

- JWT Authentication
- Docker support
- User-based expense system
- Analytics dashboard
=======
# expense-tracker-api
FastAPI-based Expense Tracker API with CRUD operations, filtering, pagination, and SQLAlchemy ORM integration. Designed for learning backend development and API structure.
>>>>>>> 21851d527882535d6f91b3d13cdd8f4b6c1590c3
