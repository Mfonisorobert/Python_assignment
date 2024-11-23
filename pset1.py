# pset1.py

todos = [
    ("Monday", ["Buy groceries", "Complete project", "Exercise"]),
    ("Tuesday", ["Attend meeting", "Clean the house"]),
    ("Wednesday", ["Write blog post", "Go for a walk"]),
    ("Thursday", ["Work on coding tasks", "Read a book"]),
    ("Friday", ["Plan weekend", "Do laundry"]),
]

def get_todos_for_day(day):
    for todo in todos:
        if todo[0] == day:
            return todo[1]
    return "No todos found for this day."

def display_all_todos():
    for day, tasks in todos:
        print(f"{day}:")
        for task in tasks:
            print(f"  - {task}")

# Example of usage:
if __name__ == "__main__":
    print("Todos for Monday:", get_todos_for_day("Monday"))
    print("\nAll Todos:")
    display_all_todos()
