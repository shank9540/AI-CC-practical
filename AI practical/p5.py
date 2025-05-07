import random
import re
from datetime import datetime

class BookstoreBot:
    def __init__(self):
        self.book_catalog = {
            "fiction": ["The Great Adventure", "Mystery Manor", "Love in Paris"],
            "non-fiction": ["Science Today", "History of Time", "Cook's Guide"],
            "children": ["Magic School", "Animal Tales", "Space Journey"]
        }
        
        self.responses = {
            "greeting": [
                "Welcome to BookWorld! How can I help you today?",
                "Hello! I'm your BookWorld assistant. What can I do for you?",
                "Hi there! Looking for some great books?"
            ],
            "farewell": [
                "Thank you for visiting BookWorld! Have a great day!",
                "Hope I could help! Come back soon!",
                "Goodbye! Happy reading!"
            ],
            "unknown": [
                "I'm not sure I understand. Could you rephrase that?",
                "I'm still learning! Could you try asking in a different way?",
                "I didn't quite catch that. Could you be more specific?"
            ]
        }

    def get_current_time(self):
        """Returns current time for order tracking simulation"""
        return datetime.now().strftime("%H:%M:%S")

    def search_books(self, category):
        """Search for books in a specific category"""
        if category is None:
            return "Please specify a book category (fiction/non-fiction/children)"
            
        category = category.lower()
        if category in self.book_catalog:
            return f"Here are our {category} books: {', '.join(self.book_catalog[category])}"
        return f"Sorry, we don't have the category '{category}'. Our categories are: {', '.join(self.book_catalog.keys())}"

    def handle_order_status(self, order_id):
        """Simulate order status checking"""
        if not order_id.isdigit():
            return "Please provide a valid order number (digits only)."
        status_options = ["processing", "shipped", "delivered"]
        random_status = random.choice(status_options)
        return f"Order #{order_id} is currently {random_status} (as of {self.get_current_time()})"

    def process_input(self, user_input):
        """Process user input and return appropriate response"""
        user_input = user_input.lower()

        # Check for greetings
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["greeting"])

        # Check for goodbyes
        if any(word in user_input for word in ["bye", "goodbye", "thank you", "thanks"]):
            return random.choice(self.responses["farewell"])

        # Check for book category inquiries
        # Fixed pattern matching for categories
        for category in self.book_catalog.keys():
            if category in user_input:
                return self.search_books(category)
            
        if any(word in user_input for word in ["show", "list", "books"]):
            # If they're asking about books but didn't specify a category
            return "Which category would you like to see? We have: " + ", ".join(self.book_catalog.keys())

        # Check for order status inquiries
        order_match = re.search(r"order.*?(\d+)", user_input)
        if "order" in user_input and "status" in user_input and order_match:
            return self.handle_order_status(order_match.group(1))

        # Handle help request
        if "help" in user_input:
            return """
I can help you with:
1. Showing books in different categories (fiction/non-fiction/children)
2. Checking order status (provide order number)
3. General information about our bookstore
Just let me know what you need!
"""

        # Default response for unknown queries
        return random.choice(self.responses["unknown"])

def main():
    """Main function to run the chatbot"""
    bot = BookstoreBot()
    print("BookWorld Bot: Welcome to BookWorld! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("BookWorld Bot:", random.choice(bot.responses["farewell"]))
            break
            
        response = bot.process_input(user_input)
        print("BookWorld Bot:", response)

if __name__ == "__main__":
    main()