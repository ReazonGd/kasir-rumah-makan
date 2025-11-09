from util.user_input import MenuList, input_int
from util.storage import Storage
from menu import Kategori
from .order_calculator import OrderCalculator
from discount.discounts import BuyOneGetOneFreeDiscount, PercentageDiscount

class Kasir:
    def __init__(self, storage: Storage) -> None:
        self.storage: Storage = storage
        self.display_category = Kategori.Makanan
        self.calculator = OrderCalculator(self.storage, 10, 20000)
        self._setup_discount()
        pass

    def _setup_discount(self):
        self.calculator.add_discount(PercentageDiscount(min_subtotal=100000, percentage=10, storage=self.storage))
        buy1get1_item = self.storage.get_menu_by_name("Jus Alpukat")
        self.calculator.add_discount(BuyOneGetOneFreeDiscount(min_subtotal=50000, menu=buy1get1_item, storage=self.storage))
    
    def kasir_option(self):
        while True:
            answ = MenuList("[Pemesanan]===================",
                ["Lihat Menu Makanan", "Lihat Menu Minuman", "keranjang", "Selesaikan Pesanan"],
                exiteable=True,
                use_number=True
            ).show()

            if answ == None:
                return
            elif answ == 0:
                self.display_category = Kategori.Makanan
                self.menus_display()
            elif answ == 1:
                self.display_category = Kategori.Minuman
                self.menus_display()
            elif answ == 2:
                self.keranjang_option()
            elif answ == 3:
                acc = MenuList(
                    "[Selesaikan Pesanan] Yakin ingin menyelesaikan pesanan?",
                    ["Selesai", "Tidak"],
                    use_number=False,
                    exiteable=False
                ).show()
                if acc == 0:
                    self.calculator.display_struk()
            
    def keranjang_option(self):
        keranjang_items = self.storage.get_keranjang()
        if len(keranjang_items) == 0:
            input("Keranjang kosong! tekan enter untuk kembali...")
            return

        list_item = [f"{item[0].price} x {item[1]} = {item[0].price * item[1]} \t{item[0].name}" for item in keranjang_items]
        menu_list = MenuList(
            "[Keranjang] pilih item untuk di edit\n"
            "\tharga \t\tnama",
            list_item,
            use_number=True,
            exiteable=True
        )
        while True:

            selected_item = menu_list.show()

            if selected_item is None:
                return

            self.open_item(selected_item)

    def menus_display(self):
        list_item_and_idx = [(f"{m.price} \t{m.name}",i ) for i, m in enumerate(self.storage.get_menu_list()) if m.jenis == self.display_category]
        list_item = [item[0] for item in list_item_and_idx]
        menu_list = MenuList(
            f"[Kasir] pilih menu {self.display_category.value}"
            "\n\tharga \tnama",
            list_item,
            use_number=True,
            exiteable=True
        )
        while True:
            selected_item = menu_list.show()

            if selected_item is None:   
                return

            menu = self.storage.get_menu_detail(list_item_and_idx[selected_item][1])
            found = self.storage.get_keranjang_from_menu(menu)

            if found is not None:
                self.open_item(found)
            else:
                jumlah = input_int("Masukkan jumlah\n")
                self.storage.add_to_keranjang(menu, jumlah)
                menu_list.msg = f"({menu.name} + {jumlah}) \n-> "


    def open_item(self, item_on_keranjang):
        while True:
            methode = MenuList(
                f"[Kasir{item_on_keranjang[0].name}] ===========\n"
                f"Harga:    {item_on_keranjang[0].price}\n"
                f"Kategori: {item_on_keranjang[0].jenis.value}\n\n"
                f"Jumlah:   {item_on_keranjang[1]}",
                ["ubah jumlah", "hapus dari keranjang"],
                use_number=True,
                exiteable=True
            ).show()

            if methode == 0:
                quantity = input_int("Masukkan jumlah\n")
                self.storage.update_item_keranjang(item_on_keranjang[0], quantity)
                item_on_keranjang[1] = quantity # update local reference
            elif methode == 1:
                confirm = MenuList(
                        f"[Hapus Menu] ===========\n"
                        f"Yakin ingin menghapus {item_on_keranjang[0].name} dari keranjang?",
                        ["Ya", "Tidak"],
                        use_number=False,
                        exiteable=False
                    ).show()
                if confirm == 0:
                    self.storage.delete_item_keranjang(item_on_keranjang[0])
                    return
            elif methode is None:
                return
