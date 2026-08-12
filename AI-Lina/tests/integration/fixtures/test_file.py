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
        # Validate item before adding
        if not isinstance(item, (str, int, float, dict, list)):
            raise TypeError("Item must be a basic type")

        # Check if item already exists
        if item in self.data:
            return  # Skip duplicates

        # Validate dict items
        if isinstance(item, dict):
            required_keys = ["id", "value"]
            for key in required_keys:
                if key not in item:
                    raise KeyError(f"Missing required key: {key}")

            # Access nested value - BUG HERE
            nested_val = item["metadata"]["user_id"]  # KeyError if metadata missing

            # Validate nested value
            if not isinstance(nested_val, (str, int)):
                raise ValueError("user_id must be string or int")

        # Add validated item
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


class DataValidator:
    """Validates data structures for processing."""

    def __init__(self):
        self.rules: dict[str, Any] = {}
        self.errors: list[str] = []

    def add_rule(self, name: str, validator: callable) -> None:
        """Add a validation rule."""
        self.rules[name] = validator

    def validate(self, data: dict[str, Any]) -> bool:
        """Validate data against all rules."""
        self.errors = []
        for name, validator in self.rules.items():
            try:
                if not validator(data):
                    self.errors.append(f"Rule '{name}' failed")
            except Exception as e:
                self.errors.append(f"Rule '{name}' error: {e}")
        return len(self.errors) == 0

    def get_errors(self) -> list[str]:
        """Get validation errors."""
        return self.errors


class DataTransformer:
    """Transforms data between formats."""

    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.transformers: dict[str, callable] = {}

    def register(self, name: str, transformer: callable) -> None:
        """Register a transformer function."""
        self.transformers[name] = transformer

    def transform(self, data: Any, transformer_name: str) -> Any:
        """Transform data using specified transformer."""
        if transformer_name not in self.transformers:
            raise ValueError(f"Unknown transformer: {transformer_name}")

        transformer = self.transformers[transformer_name]
        return transformer(data)

    def chain_transform(self, data: Any, chain: list[str]) -> Any:
        """Apply multiple transformers in sequence."""
        result = data
        for transformer_name in chain:
            result = self.transform(result, transformer_name)
        return result


class DataAggregator:
    """Aggregates data from multiple sources."""

    def __init__(self):
        self.sources: dict[str, list[Any]] = {}
        self.cache: dict[str, Any] = {}

    def add_source(self, name: str, data: list[Any]) -> None:
        """Add a data source."""
        self.sources[name] = data

    def aggregate(self, source_names: list[str], strategy: str = "merge") -> list[Any]:
        """Aggregate data from multiple sources."""
        # BUG: Accessing cache key without checking
        config = self.cache["aggregation_config"]  # KeyError if not set

        result = []
        for source_name in source_names:
            if source_name in self.sources:
                result.extend(self.sources[source_name])

        if strategy == "dedupe":
            result = list(set(result))
        elif strategy == "sort":
            result = sorted(result)

        return result

    def clear_cache(self) -> None:
        """Clear the aggregation cache."""
        self.cache.clear()

    def get_source_count(self) -> int:
        """Get the number of data sources."""
        return len(self.sources)

    def get_total_items(self) -> int:
        """Get total number of items across all sources."""
        total = 0
        for data in self.sources.values():
            total += len(data)
        return total



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
