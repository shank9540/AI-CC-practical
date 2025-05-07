import time

class AirlineSchedulingExpertSystem:
    def __init__(self):
        self.flight_data = {
            "FL001": {"departure": "10:00 AM", "arrival": "12:00 PM", "status": "Scheduled", "capacity": 200},
            "FL002": {"departure": "2:00 PM", "arrival": "4:00 PM", "status": "Scheduled", "capacity": 150},
            "FL003": {"departure": "6:00 PM", "arrival": "8:00 PM", "status": "Scheduled", "capacity": 180},
        }

    def update_flight_status(self, flight_id, status):
        if flight_id in self.flight_data:
            self.flight_data[flight_id]["status"] = status
            print(f"\n✅ Flight {flight_id} status updated to '{status}'.")
        else:
            print(f"\n❌ Flight {flight_id} not found.")

    def schedule_cargo(self, flight_id, cargo_weight):
        if flight_id not in self.flight_data:
            print(f"\n❌ Flight {flight_id} not found.")
            return

        flight = self.flight_data[flight_id]
        if cargo_weight <= flight["capacity"]:
            print(f"\n✅ Cargo of {cargo_weight} units scheduled for Flight {flight_id}.")
        else:
            print(f"\n⚠️ Cargo exceeds capacity ({flight['capacity']}). Cannot schedule.")

    def show_flight_info(self, flight_id):
        if flight_id in self.flight_data:
            flight = self.flight_data[flight_id]
            print(f"\n✈️ Flight {flight_id} Information:")
            print(f"Departure: {flight['departure']}")
            print(f"Arrival: {flight['arrival']}")
            print(f"Status: {flight['status']}")
            print(f"Capacity: {flight['capacity']} units")
        else:
            print(f"\n❌ Flight {flight_id} not found.")

def run_airline_scheduling_system():
    system = AirlineSchedulingExpertSystem()

    while True:
        print("\n=== Airline Scheduling & Cargo System ===")
        print("1. View Flight Info")
        print("2. Update Flight Status")
        print("3. Schedule Cargo")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            flight_id = input("Enter flight ID (e.g., FL001): ").strip().upper()
            system.show_flight_info(flight_id)
        elif choice == "2":
            flight_id = input("Enter flight ID: ").strip().upper()
            status = input("Enter new status (e.g., Delayed, Cancelled, Departed): ").strip()
            system.update_flight_status(flight_id, status)
        elif choice == "3":
            flight_id = input("Enter flight ID: ").strip().upper()
            try:
                weight = int(input("Enter cargo weight (units): "))
                system.schedule_cargo(flight_id, weight)
            except ValueError:
                print("❌ Invalid weight input.")
        elif choice == "4":
            print("Exiting Airline System. ✈️")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
run_airline_scheduling_system()
