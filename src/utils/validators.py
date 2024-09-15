import re

def validate_service_name(service_name: str) -> bool:
    return bool(service_name and service_name.strip())

def validate_username(username: str) -> bool:
    return bool(username and username.strip())

def validate_password(password: str) -> bool:
    # Add your password strength requirements here
    return len(password) >= 8 and re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)