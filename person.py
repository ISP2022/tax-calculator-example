"""Data class for a Person with immutable attributes."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    id: str
    first_name: str
    last_name: str

    # constructor with named parameters is auto-generated.

    def __str__(self):
        """Return the person's name."""
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        """Two Persons are equal if their id and last_name are the same."""
        if not isinstance(other, Person):
            return False
        return self.id == other.id and self.last_name == other.last_name
