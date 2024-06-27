# Yummy Sweet Restaurant CLI App

This project is for users who are able to browser menu and book a table with CRUD operations, such as `View bookings`, `Add a booking`, `Update a booking` and `Delete a booking`

## Technical use

I develop an application use skills below:

```console
- Python 
- SQL
- SQLAlchemy
- SQLite
- Migration with Alembic
```

***

## Getting Started

1. First of all, you need to install dependency

```
pipenv install
```

2. Run the application, you need to start a main entry point. You will see some of questions to ask you to do next step

```
python3 main.py 
```

## How to set up database

1. Set up Database

```
alembic init 
```

2. install Alembic with pipenv

```
pipenv install alembic
```

3. initialize Alembic 
```
alembic init alembic
```

4. Configure Alembic in the `alambic.ini`
```
sqlalchemy.url = sqlite:///your_database.db
```

## Learning Resources

- [Faker](https://pypi.org/project/Faker/0.7.4/)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
