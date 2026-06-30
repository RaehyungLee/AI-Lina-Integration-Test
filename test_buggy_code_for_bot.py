"""Test file with intentional bugs for PR bot testing - Version 2."""

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

def new_buggy_function(password):
    """NEW BUG in v2: Hardcoded credentials and weak crypto."""
    secret_key = "admin123"  # Bug: Hardcoded credential
    import hashlib
    # Bug: MD5 is cryptographically broken
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed == secret_key

def unsafe_eval(user_input):
    """NEW BUG in v2: Code injection via eval."""
    # Bug: eval() on user input is extremely dangerous
    result = eval(user_input)
    return result
