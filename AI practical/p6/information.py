import time

class InformationManagementSystem:
    def __init__(self):
        # Initializing the knowledge base with sample data
        self.data_storage = {
            "employees": {
                101: {"name": "Alice", "role": "Manager", "department": "HR", "status": "Active"},
                102: {"name": "Bob", "role": "Developer", "department": "IT", "status": "Active"},
                103: {"name": "Charlie", "role": "Designer", "department": "Marketing", "status": "Inactive"},
            },
            "patients": {
                201: {"name": "John Doe", "age": 35, "diagnosis": "Flu", "status": "Under Treatment"},
                202: {"name": "Jane Smith", "age": 42, "diagnosis": "Diabetes", "status": "Stable"},
                203: {"name": "Alan Walker", "age": 58, "diagnosis": "Cancer", "status": "Critical"},
            },
            "documents": {
                "HR_POLICY": {"title": "HR Policy", "content": "Contains HR policies related to employees."},
                "MEDICAL_GUIDELINES": {"title": "Medical Guidelines", "content": "Contains guidelines for doctors."},
            }
        }

    def retrieve_data(self, category, search_criteria):
        # Retrieve specific data from the category based on search criteria (e.g., name, status)
        print(f"Retrieving {category} information...")
        time.sleep(2)
        if category not in self.data_storage:
            print(f"Category {category} not found.")
            return

        category_data = self.data_storage[category]
        results = []

        for key, value in category_data.items():
            if any(search_criteria.lower() in str(val).lower() for val in value.values()):
                results.append((key, value))

        if results:
            for result in results:
                print(f"ID: {result[0]}")
                for key, val in result[1].items():
                    print(f"{key.capitalize()}: {val}")
                print("-" * 30)
        else:
            print("No matching data found.")

    def add_data(self, category, data_id, data):
        # Add new data to a specific category
        if category not in self.data_storage:
            print(f"Category {category} not found.")
            return

        self.data_storage[category][data_id] = data
        print(f"Data added to {category} with ID {data_id}.")

    def update_data(self, category, data_id, new_data):
        # Update existing data in a category
        if category not in self.data_storage:
            print(f"Category {category} not found.")
            return

        if data_id in self.data_storage[category]:
            self.data_storage[category][data_id].update(new_data)
            print(f"Data updated for ID {data_id} in {category}.")
        else:
            print(f"ID {data_id} not found in {category}.")

    def delete_data(self, category, data_id):
        # Delete data from a specific category
        if category not in self.data_storage:
            print(f"Category {category} not found.")
            return

        if data_id in self.data_storage[category]:
            del self.data_storage[category][data_id]
            print(f"Data with ID {data_id} deleted from {category}.")
        else:
            print(f"ID {data_id} not found in {category}.")

    def start(self):
        while True:
            print("\n--- Information Management System ---")
            print("1. Retrieve Data")
            print("2. Add Data")
            print("3. Update Data")
            print("4. Delete Data")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                category = input("Enter category (employees, patients, documents): ")
                search_criteria = input("Enter search criteria: ")
                self.retrieve_data(category, search_criteria)

            elif choice == "2":
                category = input("Enter category (employees, patients, documents): ")
                data_id = int(input("Enter ID: "))
                if category == "employees":
                    name = input("Enter name: ")
                    role = input("Enter role: ")
                    department = input("Enter department: ")
                    status = input("Enter status (Active/Inactive): ")
                    data = {"name": name, "role": role, "department": department, "status": status}
                elif category == "patients":
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    diagnosis = input("Enter diagnosis: ")
                    status = input("Enter status (Under Treatment/Stable/Critical): ")
                    data = {"name": name, "age": age, "diagnosis": diagnosis, "status": status}
                elif category == "documents":
                    title = input("Enter title: ")
                    content = input("Enter content: ")
                    data = {"title": title, "content": content}
                else:
                    print("Invalid category.")
                    continue
                self.add_data(category, data_id, data)

            elif choice == "3":
                category = input("Enter category (employees, patients, documents): ")
                data_id = int(input("Enter ID: "))
                if category == "employees":
                    name = input("Enter name: ")
                    role = input("Enter role: ")
                    department = input("Enter department: ")
                    status = input("Enter status (Active/Inactive): ")
                    new_data = {"name": name, "role": role, "department": department, "status": status}
                elif category == "patients":
                    name = input("Enter name: ")
                    age = int(input("Enter age: "))
                    diagnosis = input("Enter diagnosis: ")
                    status = input("Enter status (Under Treatment/Stable/Critical): ")
                    new_data = {"name": name, "age": age, "diagnosis": diagnosis, "status": status}
                elif category == "documents":
                    title = input("Enter title: ")
                    content = input("Enter content: ")
                    new_data = {"title": title, "content": content}
                else:
                    print("Invalid category.")
                    continue
                self.update_data(category, data_id, new_data)

            elif choice == "4":
                category = input("Enter category (employees, patients, documents): ")
                data_id = int(input("Enter ID: "))
                self.delete_data(category, data_id)

            elif choice == "5":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

# Example usage
info_system = InformationManagementSystem()
info_system.start()
