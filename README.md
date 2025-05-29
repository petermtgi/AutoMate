# AutoMate

AutoMate is a CLI app for managing customers, their vehicles, and vehicle service records in a car repair shop.

## Features

- Add and manage customers
- Add and manage vehicles (linked to customers)
- Add service records (linked to vehicles)
- Search for a vehicle by license plate
- View all vehicles for a customer, with service history
- Calculate total cost of services for a vehicle
- Find the top-spending customer

## Requirements

- Python 3.11+
- Pipenv

## Setup

```bash
pipenv install
pipenv run python seed.py   # Populate the database with sample data
pipenv run python cli.py    # Start the CLI app
```

## Project Structure

- `models/` — SQLAlchemy models
- `db.py` — Database setup
- `cli.py` — Main CLI logic
- `utils.py` — Helper functions
- `seed.py` — Populate database with sample data
