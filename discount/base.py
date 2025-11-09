from abc import ABC, abstractmethod
# from menu import Menu

class Discount(ABC):
    @abstractmethod
    def accepteble(self, sub_total: int):
        """Cek apakah diskon dapat di terapkan"""
        pass

    @abstractmethod
    def calculate(self, sub_total: int):
        """hitung"""
        pass

    @abstractmethod
    def description(self):
        """membeikan deskripsi"""