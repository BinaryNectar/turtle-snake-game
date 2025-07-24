from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def sync(self) -> None:
        """Synchronize GUI with logic"""
        ...
