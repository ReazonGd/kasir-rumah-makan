from util.cli import enterAlternateScreen, exitAlternateScreen, clearScreen
from util.user_input import input_int, MenuList
from util.storage import Storage
from menu import Menu, Kategori
from copy import copy

class ManageMenus:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def manage_options(self):
        while True:
            ans = MenuList("[Kelola Menu] ", ["tambah", "edit/hapus"], use_number=True, exiteable=True).show()

            if ans == 0:
                self.add_menu()
            elif ans == 1:
                self.edit_page()
            elif ans is None:
                return

    def add_menu(self):
        while True:
            clearScreen()
            menu_name = input("Masukkan nama:\n").strip()
            if self.storage.is_menu_exists(menu_name):
                print("Menu dengan nama tersebut sudah ada!")
                input("Tekan enter untuk melanjutkan...")
                continue
        
            menu_price = input_int("Masukkan harga:\n")

            jenis_idx = MenuList(
                "Termasuk jenis?",
                ["makanan", "minuman"],
                use_number=True,
                exiteable=False
            ).show()

            new_menu = Menu(
                menu_name,
                menu_price,
                [Kategori.Makanan, Kategori.Minuman][jenis_idx]
            )

            self.storage.add_menu(new_menu)
            return

    def edit_page(self):
        list_item = [m.name for m in self.storage.__menu__]
        menu_list = MenuList(
            "[Edit Menu] pilih menu untuk di edit",
            list_item,
            use_number=True,
            exiteable=True
        )

        while True:
            selected_item = menu_list.show()

            if selected_item is None:
                return

            menu = copy(self.storage.get_menu_detail(selected_item))

            while True:
                methode = MenuList(
                    f"[Edit Menu {menu.name}] ===========\n"
                    f"Harga: \t\t{menu.price}\n"
                    f"Kategori: \t{menu.jenis.name}",
                    ["Ganti Nama", "Ganti Harga", "Ganti Kategori", "Hapus Menu"],
                    use_number=True,
                    exiteable=True
                ).show()

                if methode is None:
                    confirm = MenuList(
                        f"[Konfirmasi {menu.name}] ===========\n"
                        f"Harga: \t{menu.price}\nKategori: \t{menu.jenis.name}\n\n"
                        "Keluar dan Simpan?",
                        ["Ya", "Tidak", "Batal"],
                        use_number=False,
                        exiteable=False
                    ).show()

                    if confirm == 0:
                        self.storage.update_menu(selected_item, menu)
                        return
                    elif confirm == 1:
                        break

                elif methode == 0:
                    menu.name = input("Masukkan nama baru:\n")
                elif methode == 1:
                    menu.price = input_int("Masukkan harga baru:\n")
                elif methode == 2:
                    jenis_idx = MenuList(
                        "Termasuk jenis?",
                        ["makanan", "minuman"],
                        use_number=True,
                        exiteable=False
                    ).show()
                    menu.jenis = [Kategori.Makanan, Kategori.Minuman][jenis_idx]
                elif methode == 3:
                    confirm = MenuList(
                        f"[Hapus Menu {menu.name}] ===========\n"
                        "Yakin ingin menghapus menu ini?",
                        ["Ya", "Tidak"],
                        use_number=False,
                        exiteable=False
                    ).show()
                    if confirm == 0:
                        self.storage.delete_menu(selected_item)
                        break

                
