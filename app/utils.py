import requests

def has_internet() -> bool:
    """Check for internet connectivity."""
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except Exception:
        return False
