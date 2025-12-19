from util.user_input import ListOfChoice, input_int
from util.storage import Pesanan, Menu
from menu import Kategori, MenuItem
from .order_calculator import OrderCalculator

class Kasir:
    def __init__(self, menu: Menu, pesanan: Pesanan) -> None:
        self.display_category = Kategori.Makanan
        self.pesanan = pesanan
        self.menu = menu
        self.calculator = OrderCalculator(self.pesanan,self.menu, 0.10, 20000.0)
        pass

    def kasir_option(self):
        while True:
            answ = ListOfChoice("[Pemesanan]===================",
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
                self.calculator.display_struk()
            
    def keranjang_option(self): 
        keranjang_items = self.pesanan.get_keranjang()
        if len(keranjang_items) == 0:
            input("Keranjang kosong! tekan enter untuk kembali...")
            return
        
        def get_items():
            return [f"{item[0].get_price()} x {item[1]} = {item[0].get_price() * item[1]} \t{item[0].get_name()}" for item in keranjang_items]
        
        list_item = get_items()
        menu_list = ListOfChoice(
            "[Keranjang] pilih item untuk di edit\n"
            "\tharga \t\tnama",
            list_item,
            use_number=True,
            exiteable=True
        )
        while True:
            menu_list.update_choices(get_items())
            selected_item = menu_list.show()

            if selected_item is None:
                return

            self.open_item(self.pesanan.get_by_index(selected_item))

    def menus_display(self):
        list_item_and_idx = [(f"{m.get_price()} \t{m.get_name()}",i ) for i, m in enumerate(self.menu.get_menu_list()) if m.get_jenis() == self.display_category]
        list_item = [item[0] for item in list_item_and_idx]
        menu_list = ListOfChoice(
            f"[Kasir] pilih menu {self.display_category.value}"
            "\nharga \tnama",
            list_item,
            use_number=True,
            exiteable=True
        )
        while True:
            selected_item = menu_list.show()

            if selected_item is None:   
                return

            menu = self.menu.get_by_index(list_item_and_idx[selected_item][1])
            found = self.pesanan.get_menu_by_MenuItem(menu)

            if found is not None:
                self.open_item(found)
            else:
                jumlah = input_int("Masukkan jumlah\n")
                self.pesanan.add_to_keranjang(menu, jumlah)
                menu_list.msg = f"({menu.get_name()} + {jumlah}) \n-> "


    def open_item(self, item_on_keranjang: tuple[MenuItem, int]):
        # temporary value
        quantity = item_on_keranjang[1]
        while True:
            methode = ListOfChoice(
                f"[Kasir{item_on_keranjang[0].get_name()}] ===========\n"
                f"Harga:    {item_on_keranjang[0].get_price()}\n"
                f"Kategori: {item_on_keranjang[0].get_jenis().name}\n\n"
                f"Jumlah:   {quantity}",
                ["ubah jumlah", "hapus dari keranjang"],
                use_number=True,
                exiteable=True
            ).show()

            if methode == 0:
                new_quantity = input_int("Masukkan jumlah\n")
                quantity = new_quantity
                self.pesanan.update_item_keranjang(item_on_keranjang[0], quantity)
            elif methode == 1:
                confirm = ListOfChoice(
                        f"[Hapus Menu] ===========\n"
                        f"Yakin ingin menghapus {item_on_keranjang[0].get_name()} dari keranjang?",
                        ["Ya", "Tidak"],
                        use_number=False,
                        exiteable=False
                    ).show()
                if confirm == 0:
                    self.pesanan.remove_item_by_MenuItem(item_on_keranjang[0])
                    return
            elif methode is None:
                return
