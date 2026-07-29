"""Test file with intentional bugs for PR bot testing."""

def unsafe_sql_query(user_id):
    """Bug: SQL injection vulnerability."""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def process_data(data):
    """Bug: Unhandled exception and potential None dereference."""
    result = data.get("value")
    # Bug: No check if result is None
    return result.upper()

def calculate_total(items):
    """Bug: Division by zero risk."""
    total = sum(items)
    average = total / len(items)  # Bug: len(items) could be 0
    return average

class DataProcessor:
    """Bug: Resource leak."""

    def __init__(self, filename):
        self.file = open(filename, 'r')  # Bug: File never closed
        self.data = self.file.read()

    def process(self):
        return self.data.upper()
