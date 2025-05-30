from db import Session
from models.customer import Customer
from models.vehicle import Vehicle
from models.service_record import ServiceRecord
from tabulate import tabulate
from utils import input_nonempty, input_float, input_int

def add_customer(session):
    print("\n--- Add Customer ---")
    name = input_nonempty("Name: ")
    phone = input_nonempty("Phone: ")
    email = input("Email (optional): ").strip()
    customer = Customer(name=name, phone=phone, email=email)
    session.add(customer)
    session.commit()
    print(f"Customer '{name}' added.")

def add_vehicle(session):
    print("\n--- Add Vehicle ---")
    customers = session.query(Customer).all()
    if not customers:
        print("No customers found. Add a customer first.")
        return
    print(tabulate([(c.id, c.name) for c in customers], headers=["ID", "Name"]))
    customer_id = input_int("Enter Customer ID: ")
    customer = session.get(Customer, customer_id)
    if not customer:
        print("Customer not found.")
        return
    license_plate = input_nonempty("License Plate: ").upper()
    make = input_nonempty("Make: ")
    model = input_nonempty("Model: ")
    year = input_int("Year: ")
    vehicle = Vehicle(license_plate=license_plate, make=make, model=model, year=year, customer=customer)
    session.add(vehicle)
    session.commit()
    print(f"Vehicle '{license_plate}' added for {customer.name}.")

def add_service_record(session):
    print("\n--- Add Service Record ---")
    vehicles = session.query(Vehicle).all()
    if not vehicles:
        print("No vehicles found. Add a vehicle first.")
        return
    print(tabulate([(v.id, v.license_plate, v.make, v.model) for v in vehicles], headers=["ID", "Plate", "Make", "Model"]))
    vehicle_id = input_int("Enter Vehicle ID: ")
    vehicle = session.get(Vehicle, vehicle_id)
    if not vehicle:
        print("Vehicle not found.")
        return
    description = input_nonempty("Service Description: ")
    cost = input_float("Service Cost: ")
    service = ServiceRecord(description=description, cost=cost, vehicle=vehicle)
    session.add(service)
    session.commit()
    print(f"Service record added for vehicle '{vehicle.license_plate}'.")

def view_vehicles_for_customer(session):
    print("\n--- View Vehicles for Customer ---")
    customers = session.query(Customer).all()
    if not customers:
        print("No customers found.")
        return
    print(tabulate([(c.id, c.name) for c in customers], headers=["ID", "Name"]))
    customer_id = input_int("Enter Customer ID: ")
    customer = session.get(Customer, customer_id)
    if not customer:
        print("Customer not found.")
        return
    vehicles = customer.vehicles
    if not vehicles:
        print("No vehicles found for this customer.")
        return
    for v in vehicles:
        print(f"\nVehicle: {v.license_plate} ({v.make} {v.model}, {v.year})")
        if v.service_records:
            print(tabulate([(s.id, s.description, s.cost, s.date) for s in v.service_records],
                           headers=["ID", "Description", "Cost", "Date"]))
        else:
            print("  No service records.")

def view_service_records_for_vehicle(session):
    print("\n--- View Service Records for Vehicle ---")
    vehicles = session.query(Vehicle).all()
    if not vehicles:
        print("No vehicles found.")
        return
    print(tabulate([(v.id, v.license_plate, v.make, v.model) for v in vehicles], headers=["ID", "Plate", "Make", "Model"]))
    vehicle_id = input_int("Enter Vehicle ID: ")
    vehicle = session.get(Vehicle, vehicle_id)
    if not vehicle:
        print("Vehicle not found.")
        return
    records = vehicle.service_records
    if not records:
        print("No service records for this vehicle.")
        return
    print(tabulate([(s.id, s.description, s.cost, s.date) for s in records], headers=["ID", "Description", "Cost", "Date"]))

def search_vehicle_by_plate(session):
    print("\n--- Search Vehicle by License Plate ---")
    plate = input_nonempty("Enter License Plate: ").upper()
    vehicle = session.query(Vehicle).filter_by(license_plate=plate).first()
    if not vehicle:
        print("Vehicle not found.")
        return
    print(f"Vehicle: {vehicle.license_plate} ({vehicle.make} {vehicle.model}, {vehicle.year})")
    print(f"Owner: {vehicle.customer.name}")

def show_total_service_cost(session):
    print("\n--- Total Service Cost for Vehicle ---")
    vehicles = session.query(Vehicle).all()
    if not vehicles:
        print("No vehicles found.")
        return
    print(tabulate([(v.id, v.license_plate, v.make, v.model) for v in vehicles], headers=["ID", "Plate", "Make", "Model"]))
    vehicle_id = input_int("Enter Vehicle ID: ")
    vehicle = session.get(Vehicle, vehicle_id)
    if not vehicle:
        print("Vehicle not found.")
        return
    total = sum(s.cost for s in vehicle.service_records)
    print(f"Total service cost for {vehicle.license_plate}: ${total:.2f}")

def show_top_spending_customer(session):
    print("\n--- Top-Spending Customer ---")
    customers = session.query(Customer).all()
    spending = []
    for c in customers:
        total = sum(s.cost for v in c.vehicles for s in v.service_records)
        spending.append((c.name, total))
    if not spending:
        print("No customers found.")
        return
    spending.sort(key=lambda x: x[1], reverse=True)
    print(tabulate([spending[0]], headers=["Customer", "Total Spent"]))

def main():
    session = Session()
    menu = [
        ("Add a customer", add_customer),
        ("Add a vehicle to a customer", add_vehicle),
        ("Add a service record to a vehicle", add_service_record),
        ("View all vehicles for a customer", view_vehicles_for_customer),
        ("View all service records for a vehicle", view_service_records_for_vehicle),
        ("Search for a vehicle by license plate", search_vehicle_by_plate),
        ("Show total service cost for a vehicle", show_total_service_cost),
        ("Show top-spending customer", show_top_spending_customer),
        ("Exit program", None)
    ]
    while True:
        print("\n=== AutoMate Menu ===")
        for i, (desc, _) in enumerate(menu, 1):
            print(f"{i}. {desc}")
        choice = input("Choose an option: ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
            print("Invalid choice.")
            continue
        idx = int(choice) - 1
        if menu[idx][1] is None:
            print("Goodbye and thank you for using AutoMate!")
            break
        menu[idx][1](session)
    session.close()

if __name__ == "__main__":
    main()