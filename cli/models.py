from dataclasses import dataclass, asdict


@dataclass
class expense:
    amount: float
    category: str
    note: str
    date: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'expense':
        return cls(**data)

    def __str__(self) -> str:
        return f"{self.date} - {self.category} - {self.note}"