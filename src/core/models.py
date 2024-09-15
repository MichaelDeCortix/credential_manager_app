from dataclasses import dataclass

@dataclass
class Credential:
    service_name: str
    username: str
    password: str