from menu import Menu, Kategori
import copy

class Storage:
    __menu__: list[Menu] = []
    __keranjang__: list[tuple[Menu, int]] = []

    def __init__(self):
        self.add_default_menu()
        pass


    def add_default_menu(self):
        self.__menu__ = [
            Menu("Nasi Goreng", 25000, Kategori.Makanan),
            Menu("Mie Ayam", 20000, Kategori.Makanan),
            Menu("Ayam Bakar", 30000, Kategori.Makanan),
            Menu("Soto Ayam", 22000, Kategori.Makanan),
            Menu("Es Teh Manis", 8000, Kategori.Minuman),
            Menu("Jus Alpukat", 15000, Kategori.Minuman),
            Menu("Kopi Hitam", 10000, Kategori.Minuman),
            Menu("Air Mineral", 5000, Kategori.Minuman),
            Menu("Es Jeruk", 12000, Kategori.Minuman),
            Menu("Nasi Uduk", 18000, Kategori.Makanan),
            Menu("Bakso", 25000, Kategori.Makanan),
            Menu("Ayam Geprek", 28000, Kategori.Makanan),
        ]

    def add_menu(self, menu: Menu):
        self.__menu__.append(menu)

    def get_menu_by_name(self, name: str):
        for menu in self.__menu__:
            if menu.name == name:
                return menu
        return None
    
    def get_menu_detail(self, index):
       return self.__menu__[index]
    
    def update_menu(self, index, menu: Menu):
        self.__menu__[index].name = menu.name
        self.__menu__[index].price = menu.price
        self.__menu__[index].jenis = menu.jenis

    def delete_menu(self, index):
        has_ordered = self.get_keranjang_from_menu(self.__menu__[index])
        if has_ordered is not None:
            self.delete_item_keranjang(self.__menu__[index])

        del self.__menu__[index]


    def get_menu_list(self):
        return self.__menu__
    
    def is_menu_exists(self, name: str) -> bool:
        for menu in self.__menu__:
            if menu.name.lower() == name.lower():
                return True
        return False

    def add_to_keranjang(self, menu: Menu, quantity: int) -> int:
        self.__keranjang__.append((menu, quantity))
        return len(self.__keranjang__) - 1

    def get_keranjang(self):
        return self.__keranjang__
    
    def clear_keranjang(self):
        self.__keranjang__ = []

    def delete_item_keranjang(self, menu: Menu):
        item = self.get_keranjang_from_menu(menu)
        if item is not None:
            self.__keranjang__.remove(item)
    
    def update_item_keranjang(self, menu, quantity: int):
        item = self.get_keranjang_from_menu(menu)
        if item is not None:
            idx = self.__keranjang__.index(item)
            self.__keranjang__[idx] = (item[0], quantity)

    def get_keranjang_from_menu(self, menu: Menu):
        for item in self.get_keranjang():
            if item[0].name == menu.name:
                return item
        return None
    
    def keranjang_size(self):
        return len(self.__keranjang__)
    

