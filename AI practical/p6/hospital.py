import time

class MedicalExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "flu": {"symptoms": ["fever", "headache", "chills"], "diagnosis": "Flu"},
            "common cold": {"symptoms": ["cough", "fever", "fatigue"], "diagnosis": "Common Cold"},
            "pneumonia": {"symptoms": ["shortness of breath", "chest pain", "fatigue"], "diagnosis": "Pneumonia"},
        }

    def ask_questions(self, symptoms):
        print("\nChecking symptoms...")
        time.sleep(2)
        found = False

        for condition, info in self.knowledge_base.items():
            if all(symptom.lower() in symptoms for symptom in info["symptoms"]):
                print(f"Diagnosis: {info['diagnosis']}")
                found = True
                break

        if not found:
            print("No matching diagnosis found. Please consult a doctor.")

    def receive_symptoms(self):
        print("\n--- Welcome to the Medical Expert System ---")
        symptoms = []

        while True:
            symptom = input("Enter a symptom (or type 'done' to finish): ").strip().lower()
            if symptom == 'done':
                break
            if symptom:
                symptoms.append(symptom)

        if symptoms:
            print(f"\nReceived symptoms: {symptoms}")
            self.ask_questions(symptoms)
        else:
            print("No symptoms provided.")

# Run the system
expert_system = MedicalExpertSystem()
expert_system.receive_symptoms()
