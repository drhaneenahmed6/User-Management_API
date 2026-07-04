<p align="center">
  <h1 align="center"> User Management API</h1>
  <p align="center">
    A RESTful API built with FastAPI, SQLAlchemy & SQLite
  </p>
</p>



A RESTful API built with **FastAPI**, **SQLAlchemy**, and **SQLite** for managing users with full CRUD operations and data validation.

---

#  Features

-  Create a new user
-  Get all users
-  Get a user by ID
-  Update user information
-  Delete a user
-  Prevent duplicate email addresses
-  Automatic request validation using Pydantic
-  Interactive API documentation with Swagger UI

---

#  Tech Stack

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Uvicorn**

---

#  Project Structure

```text
User-Management_API/
│
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── users.db
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users` | Create a new user |
| GET | `/users` | Get all users |
| GET | `/users/{user_id}` | Get user by ID |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Delete user |

---

#  Installation

### Clone the repository

```bash
git clone https://github.com/your-username/User-Management_API.git
```

### Navigate to the project

```bash
cd User-Management_API
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python -m uvicorn main:app --reload
```

---

#  API Documentation

After starting the server, open:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

#  Validation

The API validates incoming data using **Pydantic** and prevents duplicate email addresses before saving data into the database.

---

#  What I Learned

- Building REST APIs with FastAPI
- Working with SQLAlchemy ORM
- Database CRUD operations
- Dependency Injection using `Depends`
- Data validation with Pydantic
- Exception handling with HTTPException
- Organizing backend projects into separate modules

---

#  Author

**Developed by Haneen Ahmed AbdElazeem**

Backend Development Training Project 
