from util.cli import clearScreen
from util.user_input import input_int, input_float, ListOfChoice
from util.storage import Menu, Pesanan
from menu import Makanan, Minuman, Discout


class ManageMenus:
    def __init__(self, menu: Menu, pesanan: Pesanan) -> None:
        self.menu = menu
        self.pesanan = pesanan

    def manage_options(self):
        while True:
            ans = ListOfChoice(
                "[Kelola Menu] ",
                ["tambah makanan/minuman", "tambah diskon", "edit/hapus"],
                use_number=True,
                exiteable=True,
            ).show()

            if ans == 0:
                self.add_menu()
            elif ans == 1:
                self.add_discount()
            elif ans == 2:
                self.edit_page()
            elif ans is None:
                return

    def add_discount(self):
        while True:
            clearScreen()
            menu_name = input("Masukkan nama diskon:\n").strip()
            if self.menu.is_menu_exists(menu_name):
                print("Diskon dengan nama tersebut sudah ada!")
                input("Tekan enter untuk melanjutkan...")
                continue

            discount_percentage = input_int("Masukkan persentase diskon:\n")
            min_subtotal = input_float("Masukkan minimum pembayaran untuk diskon ini:\n")

            new_discount = Discout(
                menu_name, discount_percentage, min_subtotal
            )

            self.menu.add_menu(new_discount)
            return

    def add_menu(self):
        while True:
            clearScreen()
            menu_name = input("Masukkan nama:\n").strip()
            if self.menu.is_menu_exists(menu_name):
                print("Menu dengan nama tersebut sudah ada!")
                input("Tekan enter untuk melanjutkan...")
                continue

            menu_price = input_float("Masukkan harga:\n")

            jenis_idx = ListOfChoice(
                "Termasuk jenis?",
                ["makanan", "minuman",],
                use_number=True,
                exiteable=False,
            ).show()

            if jenis_idx == 0:
                new_menu = Makanan(menu_name, menu_price)
            else:
                new_menu = Minuman(menu_name, menu_price)   
            # Menu(
            #     menu_name, menu_price, [Kategori.Makanan, Kategori.Minuman][jenis_idx]
            # )

            self.menu.add_menu(new_menu)
            return

    def edit_page(self):
        def get_list_item():
            return [m.get_name() for m in self.menu.get_menu_list()]
        
        list_item = get_list_item() 
        menu_list = ListOfChoice(
            "[Edit Menu] pilih menu untuk di edit",
            list_item,
            use_number=True,
            exiteable=True,
        )

        while True:
            menu_list.update_choices(get_list_item())
            selected_item = menu_list.show()

            if selected_item is None:
                return

            menu = self.menu.get_by_index(selected_item)
            menu.tampilMenu()
            if menu.is_deleted():
                self.pesanan.remove_item_by_MenuItem(menu)
                self.menu.delete_menu(selected_item)
