from dataclasses import dataclass
from typing import Optional, Annotated


@dataclass(slots=True, frozen=True)
class CreateUserDTO:
    first_name: str
    email: str
    password: str
    job_role: str
    usage_purpose: str
    terms: bool
    phone_number: Optional[str] = None
    last_name: Optional[str] = None
