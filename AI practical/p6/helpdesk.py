import time

class HelpDeskExpertSystem:
    def __init__(self):
        self.ticket_db = {}
        self.ticket_id = 0

    def categorize_ticket(self, description):
        categories = {
            "Software": ["install", "bug", "crash", "update"],
            "Hardware": ["broken", "repair", "damage", "failure"],
            "Network": ["slow", "connectivity", "wifi", "router"]
        }

        ticket_category = "General Inquiry"
        for category, keywords in categories.items():
            if any(keyword in description.lower() for keyword in keywords):
                ticket_category = category
                break
        return ticket_category

    def create_ticket(self, description):
        self.ticket_id += 1
        category = self.categorize_ticket(description)
        self.ticket_db[self.ticket_id] = {
            "description": description,
            "category": category,
            "status": "Open"
        }
        print(f"\nTicket #{self.ticket_id} created under category '{category}'.")

    def resolve_ticket(self, ticket_id):
        if ticket_id in self.ticket_db:
            self.ticket_db[ticket_id]["status"] = "Resolved"
            print(f"Ticket #{ticket_id} has been resolved.")
        else:
            print("Ticket not found.")

    def show_ticket_info(self, ticket_id):
        if ticket_id in self.ticket_db:
            ticket = self.ticket_db[ticket_id]
            print(f"\nTicket #{ticket_id}")
            print(f"Description: {ticket['description']}")
            print(f"Category: {ticket['category']}")
            print(f"Status: {ticket['status']}")
        else:
            print("Ticket not found.")

# Interactive menu
def run_helpdesk():
    system = HelpDeskExpertSystem()

    while True:
        print("\n--- Help Desk Expert System ---")
        print("1. Create Ticket")
        print("2. View Ticket")
        print("3. Resolve Ticket")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            desc = input("Enter issue description: ")
            system.create_ticket(desc)

        elif choice == "2":
            try:
                tid = int(input("Enter ticket ID to view: "))
                system.show_ticket_info(tid)
            except ValueError:
                print("Invalid ticket ID.")

        elif choice == "3":
            try:
                tid = int(input("Enter ticket ID to resolve: "))
                system.resolve_ticket(tid)
            except ValueError:
                print("Invalid ticket ID.")

        elif choice == "4":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid choice. Try again.")

# Start the system
run_helpdesk()
