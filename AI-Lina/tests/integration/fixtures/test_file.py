"""Test fixture file for PR bot integration testing.

This file should be committed to the repo. Integration tests will add code
to this file to create test PRs.
"""

from typing import Any


class DataProcessor:
    """A safe data processing class."""

    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.data: list[Any] = []

    def add_item(self, item: Any) -> None:
        """Add an item to the processor."""
        if item is not None:
            self.data.append(item)

    def get_count(self) -> int:
        """Get the count of items."""
        return len(self.data)

    def clear(self) -> None:
        """Clear all data."""
        self.data.clear()


class Calculator:
    """A safe calculator class."""

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float | None:
        """Divide a by b safely."""
        if b == 0:
            return None
        return a / b


class StringProcessor:
    """A safe string processing class."""

    def uppercase(self, text: str) -> str:
        """Convert text to uppercase."""
        return text.upper()

    def lowercase(self, text: str) -> str:
        """Convert text to lowercase."""
        return text.lower()

    def reverse(self, text: str) -> str:
        """Reverse the text."""
        return text[::-1]


class ListProcessor:
    """A safe list processing class."""

    def sort_list(self, items: list[Any]) -> list[Any]:
        """Sort a list."""
        return sorted(items)

    def filter_none(self, items: list[Any]) -> list[Any]:
        """Filter out None values."""
        return [item for item in items if item is not None]

    def deduplicate(self, items: list[Any]) -> list[Any]:
        """Remove duplicates from list."""
        return list(set(items))


# This is where test code will be inserted (after line 89)
# Tests will add 96 lines of buggy code here


class ConfigManager:
    """A safe configuration management class."""

    def __init__(self):
        self.config: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value."""
        self.config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.config.get(key, default)


class CacheManager:
    """A safe cache management class."""

    def __init__(self, max_size: int = 100):
        self.cache: dict[str, Any] = {}
        self.max_size = max_size

    def get(self, key: str) -> Any | None:
        """Get a value from cache."""
        return self.cache.get(key)

    def set(self, key: str, value: Any) -> None:
        """Set a value in cache."""
        if len(self.cache) >= self.max_size:
            # Remove oldest item
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[key] = value


class Logger:
    """A safe logging class."""

    def log(self, message: str) -> None:
        """Log a message."""
        print(f"[LOG] {message}")

    def error(self, message: str) -> None:
        """Log an error message."""
        import sys

        print(f"[ERROR] {message}", file=sys.stderr)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        print(f"[WARNING] {message}")


def safe_function_end():
    """Final safe function."""
    return "safe"
