
##  Tour-Company-Web CLI Application

**Tour-Company-Web** is a command-line interface (CLI) application built in Python to help manage an ecotourism business. The system allows you to oversee tours, tour companies, customers, tour guides, and bookings with full CRUD operations. This project uses SQLAlchemy ORM and Alembic for database handling and follows clean architecture and modular best practices.

---

##  Project Structure

```
 tour_company_web/
 ├── database/
 │   └── engine.py          # SQLAlchemy engine and Session setup
 ├── models.py              # All SQLAlchemy ORM models in one file
 ├── seed.py                # Populate the database with initial data
 ├── run.py                 # Main CLI interface for managing the system
 |__tour_company.db
 
 ├── Pipfile                # Pipenv dependencies
 ├── alembic/               # Database migrations 
 └── README.md              # Project description and usage

````

---

##  Features

  **Create, read, update, and delete:**
  - Tour companies
  - Tours
  - Customers
  - Tour guides
  - Bookings
  - Assign tour guides to multiple tours (many-to-many)
  - View and manage customer bookings
  - Update or cancel bookings with confirmation prompts
  - Modular CLI with input validation and error handling

---

##  Technologies Used

- Python
- SQLAlchemy
- Alembic (for schema migrations)
- Pipenv (for environment management)

---

##  Setup Instructions

### 1. Clone the Repository
```

git clone https://github.com/Mitche-44/Tour-Company-Web

cd Tour-Company-Web
```
### 2.Create and Activate Virtual Environment
```
pipenv install

pipenv shell
```
### 3.Install Required Dependencies
If using Pipenv, dependencies should be installed automatically.
If using pip, install the core packages manually:

```
pip install alembic

alembic init alembic/ alembic init migrations

alembic revision --autogenerate -m "Initial migration"      #This  will create a table

```
### 4. Run Database Migrations
```
alembic upgrade head

Or, if initializing manually:

python

from models import Base
from database.engine import engine

Base.metadata.create_all(engine)
```

### 5. Seed the Database 
```
python seed.py
```

### 6. Launch the CLI Application

```
python run.py

You’ll see a menu like:
=== Ecotours CLI ===
1. List Tour Packages
2. Add Tour Package
3. Delete Tour Package
4. List Bookings
5. Add Booking
6. Delete Booking
7. Update Booking
8. Exit
```

## Learning Objectives Met

* Designed a CLI app that solves a real-world business problem.
* Implemented a fully normalized relational database using SQLAlchemy ORM.
* Used Alembic for version-controlled schema migrations.
* Built a modular, PEP8-compliant Python codebase.
* Integrated practical data structures (lists, dicts, tuples) for scalable logic.

---
### Author
Name: Mitchelle Ngetich

Email: mitchellngetich24@gmail.com

GitHub: @Mitche-44

### License
This project is licensed under the MIT License.
