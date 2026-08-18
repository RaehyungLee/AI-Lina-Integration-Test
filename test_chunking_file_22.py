"""Test file 22 with intentional bugs for chunking test."""

import os
import hashlib
from typing import Optional

def authenticate_user_22(username: str, password: str) -> bool:
    """Bug: SQL injection and hardcoded credentials."""
    # Bug: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    # Bug: Hardcoded admin password
    admin_password = "admin123"

    if password == admin_password:
        return True

    # Bug: Using MD5 for password hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed == "5f4dcc3b5aa765d61d8327deb882cf99"

def process_user_input_22(user_input: str) -> any:
    """Bug: Code injection via eval."""
    # Bug: eval() on user input is extremely dangerous
    result = eval(user_input)
    return result

def divide_numbers_22(a: float, b: float) -> float:
    """Bug: Division by zero not handled."""
    # Bug: No check for b == 0
    return a / b

def get_config_value_22(key: str, config: dict) -> str:
    """Bug: Potential None dereference."""
    # Bug: No check if key exists or if value is None
    value = config.get(key)
    return value.upper()

class FileProcessor_22:
    """Bug: Resource leak - file never closed."""

    def __init__(self, filename: str):
        # Bug: File opened but never closed
        self.file = open(filename, 'r')
        self.data = self.file.read()

    def process(self) -> str:
        return self.data.upper()

def execute_command_22(cmd: str) -> str:
    """Bug: Command injection vulnerability."""
    import subprocess
    # Bug: Shell injection - user input directly in shell command
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout.decode()

def serialize_data_22(data: any) -> bytes:
    """Bug: Insecure deserialization."""
    import pickle
    # Bug: pickle is unsafe for untrusted data
    return pickle.dumps(data)

def log_sensitive_data_22(user_id: int, password: str, ssn: str):
    """Bug: Logging sensitive information."""
    # Bug: Logging passwords and SSN
    print(f"User {user_id} logged in with password: {password}, SSN: {ssn}")

def generate_token_22(user_id: int) -> str:
    """Bug: Weak random number generation for security."""
    import random
    # Bug: random is not cryptographically secure
    token = ''.join(str(random.randint(0, 9)) for _ in range(16))
    return token

def parse_xml_22(xml_string: str) -> any:
    """Bug: XML external entity (XXE) vulnerability."""
    import xml.etree.ElementTree as ET
    # Bug: No protection against XXE attacks
    root = ET.fromstring(xml_string)
    return root

# Add more code to increase file size
class DataManager_22:
    """Additional buggy class to increase file size."""

    def __init__(self):
        self.data = []

    def add_item(self, item: dict):
        """Bug: No validation of item structure."""
        # Bug: Assumes item has 'id' key without checking
        self.data.append(item['id'])

    def get_average(self) -> float:
        """Bug: Division by zero."""
        # Bug: No check if data is empty
        return sum(self.data) / len(self.data)

    def unsafe_update(self, sql: str):
        """Bug: SQL injection in update."""
        # Bug: String interpolation in SQL
        query = f"UPDATE items SET data = '{sql}'"
        return query

# More utility functions with bugs
def validate_input_22(data: str) -> bool:
    """Bug: ReDoS vulnerability with regex."""
    import re
    # Bug: Potentially vulnerable regex pattern
    pattern = r'^(a+)+$'
    return bool(re.match(pattern, data))

def create_temp_file_22(content: str) -> str:
    """Bug: Insecure temp file creation."""
    # Bug: Predictable temp file name
    filename = f"/tmp/data_{os.getpid()}.txt"
    with open(filename, 'w') as f:
        f.write(content)
    return filename

# Additional classes to bulk up file size
class SessionManager_22:
    """Bug: Session fixation vulnerability."""

    sessions = {}

    @classmethod
    def create_session(cls, user_id: int) -> str:
        """Bug: Predictable session IDs."""
        # Bug: Sequential session IDs
        session_id = str(len(cls.sessions) + 1)
        cls.sessions[session_id] = user_id
        return session_id

    @classmethod
    def get_user(cls, session_id: str) -> Optional[int]:
        """Bug: No session validation."""
        # Bug: No check if session is valid/expired
        return cls.sessions.get(session_id)

def encrypt_data_22(data: str, key: str) -> str:
    """Bug: Weak encryption - simple XOR."""
    # Bug: XOR is not secure encryption
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
    return encrypted
