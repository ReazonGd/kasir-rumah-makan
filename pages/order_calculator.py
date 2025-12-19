from menu import MenuItem, Discout
from util.storage import Menu, Pesanan
from util.cli import enterAlternateScreen, exitAlternateScreen
from util.user_input import ListOfChoice

class OrderCalculator:
    def __init__(self, pesanan: Pesanan, menu: Menu, tax_rate: float = 0.10, service_fee: float = 20000):
        self.tax_rate = tax_rate
        self.service_fee = service_fee
        self.menu = menu
        self.pesanan = pesanan
    
    def calculate_total(self, discount: Discout|None = None):
        keranjang_items = self.pesanan.get_keranjang()
        subtotal = sum(item.get_price() * qty for (item, qty) in keranjang_items)
        total_discount = 0.0
        if discount is not None and discount.is_accepteble(subtotal):
            disc_value = discount.calculate(subtotal)
            total_discount += disc_value
        
        taxable_amount = subtotal - total_discount
        tax = taxable_amount * self.tax_rate
        
        final_total = taxable_amount + tax + self.service_fee
        
        return {
            'subtotal': subtotal,
            'discount': discount.get_name() if discount else None,
            'total_discount': total_discount,
            'tax': tax,
            'service_fee': self.service_fee,
            'final_total': final_total
        }
    
    def confirm_payemt(self, total_amount: float) -> bool:
        while True:
            try:
                entered_amount = float(input(f"Total yang harus dibayar: Rp {total_amount}\nMasukkan jumlah pembayaran:\n"))
                if entered_amount < total_amount:
                    print("Jumlah pembayaran tidak cukup. Silakan coba lagi.")
                    continue
                return True
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")
    
    def select_discount(self, subtotal: float) -> Discout|None:
        discouts = [item for item in self.menu.get_discout_list() if item.is_accepteble(subtotal)]

        if len(discouts) == 0:
            return None

        disc_list = [f"{disc.get_name()} - {disc.get_discount()}% off (Min. Rp {disc.get_min_subtotal()})" for disc in discouts]
        disc_choice = ListOfChoice(
            "[Pilih Diskon] Pilih diskon yang ingin diterapkan (keluar untuk tidak memilih) :",
            disc_list,
            use_number=True,
            exiteable=True
        ).show()

        if disc_choice is None:
            return None
        
        return discouts[disc_choice]
    def display_struk(self):
        if self.pesanan.keranjang_size() == 0:
            input("Keranjang kosong! Tekan Enter untuk kembali...")
            return
                
        calculation = self.calculate_total()

        # confirm payment
        confirm = ListOfChoice(
                f"[Chekout] ===========\n"
                f"Total yang harus dibayar: Rp {calculation['final_total']}\n"
                "Lanjutkan ke pembayaran?",
                ["Ya", "Tidak"],
                use_number=False,
                exiteable=False
            ).show()
        if confirm == 1:
            return

        # print struk
        exitAlternateScreen()
        print("[Struk Pembayaran]===================")
        print()

        for item, qty in self.pesanan.get_keranjang():
            item_total = item.get_price() * qty
            print(f"{item.get_name()}\n  {item.get_price()} x {qty} = Rp {item_total}")

        print("\n------------------------------------")

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
        # input("\nTekan Enter untuk menyelesaikan pembayaran...")
        acc = ListOfChoice(
            "[Selesaikan Pesanan] Yakin ingin menyelesaikan pesanan?",
            ["Selesai", "Tidak"],
            use_number=False,
            exiteable=False
        ).show()
        if acc == 0:
            self.pesanan.clear_keranjang()

        enterAlternateScreen()