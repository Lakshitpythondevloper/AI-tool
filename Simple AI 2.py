import time
import threading
import os
# Function to handle calculator operations
def calculator():
    try:
        print("\n--- Calculator ---")
        expression = input("Enter a mathematical expression (e.g., 2+2, 3*4): ")
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Function to set reminders
def set_reminder(message, delay):
    def remind():
        time.sleep(delay)
        os.system(f'say "{message}"')  # For macOS, on Windows/Linux you can use other notification methods
        print(f"\nReminder: {message}")

    # Run the reminder in a separate thread
    threading.Thread(target=remind).start()

# Main AI logic to interact with the user
def ai_assistant():
    print("Welcome to Simple AI Assistant")
    while True:
        print("\nOptions: ")
        print("1. Use calculator")
        print("2. Set a reminder")
        print("3. Exit")
        choice = input("\nChoose an option (1, 2, 3): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            message = input("Enter the reminder message: ")
            delay = int(input("Enter the time in seconds after which you want to be reminded: "))
            set_reminder(message, delay)
            print(f"Reminder set for {delay} seconds from now.")
        elif choice == '3':
            print("Exiting AI Assistant. Goodbye!")
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

# Run the AI Assistant
if __name__ == "__main__":
    ai_assistant()
