
##  Tour-Company-Web CLI Application

**Tour-Company-Web** is a command-line interface (CLI) application built in Python to help manage an ecotourism business. The system allows you to oversee tours, tour companies, customers, tour guides, and bookings with full CRUD operations. This project uses SQLAlchemy ORM and Alembic for database handling and follows clean architecture and modular best practices.

---

##  Project Structure

```

tour\_company\_web/
├── cli/
│   ├── main.py              # Main CLI interaction
│   ├── tour\_menu.py         # Tour-related functions
│   ├── guide\_menu.py        # Guide management
│   └── booking\_menu.py      # Booking operations
│
├── models/
│   ├── **init**.py
│   ├── tour\_company.py      # TourCompany model
│   ├── tour.py              # Tour model
│   ├── customer.py          # Customer model
│   ├── booking.py           # Booking model
│   ├── tour\_guide.py        # TourGuide model
│   └── tour\_tour\_guide.py   # Many-to-many association
│
├── database/
│   └── engine.py            # DB engine and session
│
├── seed.py                  # Populate DB with initial data
├── run.py                   # App entry point
├── Pipfile                  # Pipenv dependencies
├── alembic/                 # Migration folder
└── README.md

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

- Python 3.11+
- SQLAlchemy
- Alembic (for schema migrations)
- Pipenv (for environment management)

---

##  Setup Instructions

### 1. Clone the Repository


git clone https://github.com/Mitche-44/Tour-Company-Web

cd Tour-Company-Web

### 2.Create and Activate Virtual Environment
pipenv install
pipenv shell

### 3. Run Database Migrations

alembic upgrade head

Or, if initializing manually:

python
from models import Base
from database.engine import engine

Base.metadata.create_all(engine)


### 4. Seed the Database (Optional)

python seed.py


### 5. Launch the CLI Application


python run.py

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
