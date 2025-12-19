from menu import Kategori, MenuItem, Makanan, Minuman, Discout

# class untuk menyimpan menu 
class Menu:
    def __init__(self) -> None:
        self.__menu: list[MenuItem] = []
        pass

    def add_menu(self, menu: MenuItem):
        self.__menu.append(menu)

    def is_menu_exists(self, name: str) -> bool:
        if self.get_menu_by_name(name) is not None:
            return True
        return False

    def default_menu(self):
        self.__menu = [
            Makanan("Nasi Goreng", 25000.0),
            Makanan("Mie Ayam", 20000.0),
            Makanan("Ayam Bakar", 30000.0),
            Makanan("Soto Ayam", 22000.0),
            Minuman("Es Teh Manis", 8000.0),
            Minuman("Jus Alpukat", 15000.0),
            Minuman("Kopi Hitam", 10000.0),
            Minuman("Air Mineral", 5000.0),
            Minuman("Es Jeruk", 12000.0),
            Makanan("Nasi Uduk", 18000.0),
            Makanan("Bakso", 25000.0),
            Makanan("Ayam Geprek", 28000.0),
            Discout("Diskon 10%", 10.0, 50000.0),
            Discout("Diskon 15%", 15.0, 75000.0),
            Discout("Diskon 20%", 20.0, 100000.0),
        ]

    def get_menu_list(self):
        return self.__menu
    
    def get_makanan_list(self):
        return [menu for menu in self.__menu if menu.get_jenis() == Kategori.Makanan]
    def get_minuman_list(self):
        return [menu for menu in self.__menu if menu.get_jenis() == Kategori.Minuman]
    def get_discout_list(self) -> list[Discout]:
        return [menu for menu in self.__menu if menu.get_jenis() == Kategori.Discout]  # type: ignore
    
    def get_menu_by_name(self, name: str):
        for menu in self.__menu:
            if menu.get_name() == name:
                return menu
        return None
    def get_menu_detail(self, index):
       return self.__menu[index]
    
    def delete_menu(self, index):
        del self.__menu[index]
    
    
#  class untuk menyimpan pesanan
class Pesanan:
    def __init__(self) -> None:
        self.__keranjang__: list[tuple[MenuItem, int]] = []
        pass

    def add_to_keranjang(self, menu: MenuItem, quantity: int) -> int:
        self.__keranjang__.append((menu, quantity))
        return len(self.__keranjang__) - 1

    def get_keranjang(self):
        return self.__keranjang__
    
    def clear_keranjang(self):
        self.__keranjang__ = []

    def remove_item_by_MenuItem(self, menu: MenuItem):
        item = self.get_menu_by_MenuItem(menu)
        if item is not None:
            self.__keranjang__.remove(item)
    
    def update_item_keranjang(self, menu, quantity: int):
        item = self.get_menu_by_MenuItem(menu)
        if item is not None:
            idx = self.__keranjang__.index(item)
            self.__keranjang__[idx] = (item[0], quantity)

    def get_menu_by_MenuItem(self, menu: MenuItem):
        for item in self.get_keranjang():
            if item[0].get_name() == menu.get_name():
                return item
        return None
    
    def keranjang_size(self):
        return len(self.__keranjang__)