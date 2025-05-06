import time

class EmployeePerformance:
    def __init__(self):
        self.performance_data = {}

    def evaluate_performance(self, employee_id, task_scores, customer_feedback):
        if not task_scores:
            print("No task scores provided.")
            return

        score = (sum(task_scores) / len(task_scores)) * 0.7 + customer_feedback * 0.3
        self.performance_data[employee_id] = {
            "task_scores": task_scores,
            "customer_feedback": customer_feedback,
            "performance_score": score,
        }

    def provide_feedback(self, employee_id):
        if employee_id not in self.performance_data:
            print("Employee not found.")
            return

        data = self.performance_data[employee_id]
        print(f"\nPerformance Report for Employee {employee_id}:")
        print(f"Task Scores: {data['task_scores']}")
        print(f"Customer Feedback: {data['customer_feedback']}")
        print(f"Overall Performance Score: {data['performance_score']:.2f}")
        
        if data["performance_score"] >= 8:
            print("Feedback: Excellent Performance!")
        elif 5 <= data["performance_score"] < 8:
            print("Feedback: Good Performance, but needs improvement.")
        else:
            print("Feedback: Poor Performance, consider training.")

# Interactive Menu
def run_performance_system():
    system = EmployeePerformance()

    while True:
        print("\n--- Employee Performance Evaluation System ---")
        print("1. Evaluate Performance")
        print("2. Show Feedback")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            try:
                num_tasks = int(input("Enter number of task scores: "))
                task_scores = []
                for i in range(num_tasks):
                    score = float(input(f"Enter score for task {i+1} (0–10): "))
                    task_scores.append(score)
                feedback = float(input("Enter customer feedback score (0–10): "))
                system.evaluate_performance(emp_id, task_scores, feedback)
                print("Performance evaluated successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "2":
            emp_id = input("Enter Employee ID to view report: ").strip()
            system.provide_feedback(emp_id)

        elif choice == "3":
            print("Exiting Employee Performance System.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the system
run_performance_system()
