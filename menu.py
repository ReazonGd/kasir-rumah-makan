from enum import Enum
from abc import ABC, abstractmethod
from util.user_input import ListOfChoice, input_float, input_int

class Kategori(Enum):
    Makanan = "makanan"
    Minuman = "minuman"
    Discout = "discout"

class MenuItem(ABC):
    def __init__(self, name: str, price: float, jenis: Kategori) -> None:
        self.__name: str = name
        self.__price: float = price
        self.__jenis: Kategori = jenis
        self.__deleted: bool = False
        pass

    def get_name(self) -> str:
        return self.__name
    
    def get_price(self) -> float:
        return self.__price
    
    def get_jenis(self) -> Kategori:
        return self.__jenis

    def is_deleted(self) -> bool:
        return self.__deleted
    
    def update(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price

    def mark_deleted(self) -> None:
        self.__deleted = True

    # @classmethod
    @abstractmethod 
    def tampilMenu(self):
        pass
    
class Makanan(MenuItem):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, Kategori.Makanan)

    def tampilMenu(self):
        # temporary value
        new_name = self.get_name()
        new_price = self.get_price()

        while True:
            methode = ListOfChoice(
                f"[Edit Menu {new_name}] ===========\n"
                f"Harga: \t\t{new_price}\n"
                f"Kategori: \tMakanan",
                ["Ganti Nama", "Ganti Harga", "Hapus Menu"],
                use_number=True,
                exiteable=True,
            ).show()

            if methode is None:
                confirm = ListOfChoice(
                    f"[Konfirmasi {new_name}] ===========\n"
                    f"Harga: \t{new_price}\nKategori: \tMakanan\n\n"
                    "Keluar dan Simpan?",
                    ["Ya", "Tidak", "Batal"],
                    use_number=False,
                    exiteable=False,
                ).show()

                if confirm == 0:
                    self.update(new_name, new_price)
                    return
                elif confirm == 1:
                    break

            elif methode == 0:
                new_name = input("Masukkan nama baru:\n")
            elif methode == 1:
                new_price = input_float("Masukkan harga baru:\n")
            elif methode == 2:
                confirm = ListOfChoice(
                    f"[Hapus Menu {new_name}] ===========\n"
                    "Yakin ingin menghapus menu makanan ini?",
                    ["Ya", "Tidak"],
                    use_number=False,
                    exiteable=False,
                ).show()
                if confirm == 0:
                    self.mark_deleted()
                    break
        return

class Minuman(MenuItem):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, Kategori.Minuman)
    def tampilMenu(self):
        # temporary value
        new_name = self.get_name()
        new_price = self.get_price()

        while True:
            methode = ListOfChoice(
                f"[Edit Menu {new_name}] ===========\n"
                f"Harga: \t\t{new_price}\n"
                f"Kategori: \tMinuman",
                ["Ganti Nama", "Ganti Harga", "Hapus Menu"],
                use_number=True,
                exiteable=True,
            ).show()

            if methode is None:
                confirm = ListOfChoice(
                    f"[Konfirmasi {new_name}] ===========\n"
                    f"Harga: \t{new_price}\nKategori: \tMinuman\n\n"
                    "Keluar dan Simpan?",
                    ["Ya", "Tidak", "Batal"],
                    use_number=False,
                    exiteable=False,
                ).show()

                if confirm == 0:
                    self.update(new_name, new_price)
                    return
                elif confirm == 1:
                    break

            elif methode == 0:
                new_name = input("Masukkan nama baru:\n")
            elif methode == 1:
                new_price = input_float("Masukkan harga baru:\n")
            elif methode == 2:
                confirm = ListOfChoice(
                    f"[Hapus Menu {new_name}] ===========\n"
                    "Yakin ingin menghapus menu minuman ini?",
                    ["Ya", "Tidak"],
                    use_number=False,
                    exiteable=False,
                ).show()
                if confirm == 0:
                    self.mark_deleted()
                    break
        return

class Discout(MenuItem):
    def __init__(self, name: str, discount: float, min_subtotal: float) -> None:
        super().__init__(name, 0, Kategori.Discout)
        self.__discount = discount
        self.__min_subtotal = min_subtotal

    def get_discount(self) -> float:
        return self.__discount
    
    def get_min_subtotal(self) -> float:
        return self.__min_subtotal
    
    def upadate_dicount(self, name: str, discount: float, min_subtotal: float) -> None:
        self.update(name, 0)
        self.__discount = discount
        self.__min_subtotal = min_subtotal
    
    def is_accepteble(self, subtotal: float) -> bool:
        return subtotal >= self.__min_subtotal
    
    def calculate(self, subtotal: float) -> float:
        if self.is_accepteble(subtotal):
            return subtotal * (self.__discount / 100)
        return 0.0
    
    
    def tampilMenu(self):
        # temporary value
        new_name = self.get_name()
        new_discount = self.get_discount()
        new_min_subtotal = self.get_min_subtotal()

        while True:
            methode = ListOfChoice(
                f"[Edit Diskon {new_name}] ===========\n"
                f"Diskon: \t\t{new_discount}%\n"
                f"Minimum pembayaran: \t{new_min_subtotal}",
                ["Ganti Nama", "Ganti Persentase","Ganti minimum pembayaran", "Hapus Diskon"],
                use_number=True,
                exiteable=True,
            ).show()

            if methode is None:
                confirm = ListOfChoice(
                    f"[Konfirmasi {new_name}] ===========\n"
                    f"Diskon: \t{new_discount}%\nMinimum Pembayaran: \t{new_min_subtotal}\n\n"
                    "Keluar dan Simpan?",
                    ["Ya", "Tidak", "Batal"],
                    use_number=False,
                    exiteable=False,
                ).show()

                if confirm == 0:
                    self.upadate_dicount(new_name, new_discount, new_min_subtotal)
                    return
                elif confirm == 1:
                    break

            elif methode == 0:
                new_name = input("Masukkan nama baru:\n")
            elif methode == 1:
                new_discount = input_int("Masukkan persentase baru:\n")
            elif methode == 2:
                new_min_subtotal = input_float("Masukkan minimum pembayaran baru:\n")
            elif methode == 3:
                confirm = ListOfChoice(
                    f"[Hapus Menu {new_name}] ===========\n"
                    "Yakin ingin menghapus diskon ini?",
                    ["Ya", "Tidak"],
                    use_number=False,
                    exiteable=False,
                ).show()
                if confirm == 0:
                    self.mark_deleted()
                    break
        return