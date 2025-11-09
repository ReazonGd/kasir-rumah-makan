from enum import Enum

class Kategori(Enum):
    Makanan = "makanan"
    Minuman = "minuman"

class Menu:
    def __init__(self, name: str, price: int, jenis: Kategori) -> None:
        self.name: str = name
        self.price: int = price
        self.jenis: Kategori = jenis
        pass

