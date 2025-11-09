from .base import Discount
from menu import Menu, Kategori
from util.storage import Storage

class PercentageDiscount(Discount):
    def __init__(self, storage: Storage, min_subtotal: int, percentage: float):
        self.min_subtotal = min_subtotal
        self.percentage = percentage

    def accepteble(self, subtotal):
        return subtotal > self.min_subtotal
    
    def calculate(self, subtotal):
        if self.accepteble(subtotal):
            return subtotal * (self.percentage / 100)
        return 0.0
    
    def description(self):
        return f"diskon {self.percentage}% pembeilain minimum {self.min_subtotal}"
    
class BuyOneGetOneFreeDiscount(Discount):
    def __init__(self, storage: Storage, min_subtotal: float, menu: Menu,):
        self.min_subtotal = min_subtotal
        self.menu = menu
        self.storage = storage
    
    def accepteble(self, subtotal) -> bool:
        if subtotal <= self.min_subtotal:
            return False
        
        found = self.storage.get_keranjang_from_menu(self.menu)

        if found is None:
            return False
        elif found[1] < 2:
            return False
        return True
    
    def calculate(self, subtotal) -> float:
        if not self.accepteble(subtotal):
            return 0.0
        
        return self.menu.price
    
    def description(self):
        return f"beli 1 gratis 1 untuk pembelian {self.menu.name}"