"""Pricing helpers (AI-Lina conflict-scanner integration fixture)."""


def calculate_discount(price: float, customer_tier: str) -> float:
    """Apply a tier-based discount (conflicts with the flat-rate version)."""
    rates = {"gold": 0.25, "silver": 0.15, "bronze": 0.05}
    return price * rates.get(customer_tier, 0.0)
