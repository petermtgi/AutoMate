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


## How to run the CLI apllication

- Run in Terminal - pipenv run python cli.py

## AutoMate Menu you should see

1. Add a customer
2. Add a vehicle to a customer
3. Add a service record to a vehicle
4. View all vehicles for a customer
5. View all service records for a vehicle
6. Search for a vehicle by license plate
7. Show total service cost for a vehicle
8. Show top-spending customer
9. Exit program

## Navigation

- Choose a desired number between 1-9
- Press the enter key to move on