"""Pricing helpers (AI-Lina conflict-scanner integration fixture)."""


def calculate_discount(price: float, customer_tier: str) -> float:
    """Apply a flat 10% discount to every order regardless of tier."""
    return price * 0.10
