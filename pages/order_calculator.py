from menu import Menu
from discount.base import Discount
from util.storage import Storage
from util.cli import enterAlternateScreen, exitAlternateScreen

class OrderCalculator:
    def __init__(self, storage: Storage, tax_rate: float = 0.10, service_fee: float = 20000):
        self.tax_rate = tax_rate
        self.service_fee = service_fee
        self.storage = storage
        self.discounts: list[Discount] = []
    
    def add_discount(self, discount: Discount):
        self.discounts.append(discount)
    
    def calculate_total(self):
        keranjang_items = self.storage.get_keranjang()
        subtotal = sum(item.price * qty for (item, qty) in keranjang_items)
        discounts = [(d.calculate(subtotal), d.description()) for d in self.discounts]
        total_discount = sum(d[0] for d in discounts)
        taxable_amount = subtotal - total_discount
        tax = taxable_amount * self.tax_rate
        
        final_total = taxable_amount + tax + self.service_fee
        
        return {
            'subtotal': subtotal,
            'discounts': discounts,
            'total_discount': total_discount,
            'tax': tax,
            'service_fee': self.service_fee,
            'final_total': final_total
        }
    
    def display_struk(self):
        keranjang_items = self.storage.get_keranjang()
        if len(keranjang_items) == 0:
            input("Keranjang kosong! Tekan Enter untuk kembali...")
            return

        exitAlternateScreen()
        print("[Struk Pembayaran]===================")
        print()

        for item, qty in keranjang_items:
            item_total = item.price * qty
            print(f"{item.name}\n  {item.price} x {qty} = Rp {item_total}")

        print("\n------------------------------------")

        calculation = self.calculate_total()

        print(f"\nSubtotal       : Rp {calculation['subtotal']}")
        
        print()
        
        if calculation['total_discount'] > 0:
            for value, desc in calculation['discounts']:
                print(f"{desc}\n  -Rp {value}")
            print(f"Total Diskon   : -Rp {calculation['total_discount']}")
        
        print()

        print(f"Pajak (10%)    : Rp {calculation['tax']}")
        print(f"Pelayanan      : Rp {calculation['service_fee']}")
        
        print("------------------------------------")
        print(f"Total Bayar    : Rp {calculation['final_total']}")
        print("====================================")
        input("\nTekan Enter untuk menyelesaikan pembayaran...")

        enterAlternateScreen()
        self.storage.clear_keranjang()