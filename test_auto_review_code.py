"""Test file with bugs for auto-review testing."""

def unsafe_query(user_input):
    """SQL injection vulnerability."""
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query

def divide(a, b):
    """Division by zero risk."""
    return a / b  # No check for b == 0
