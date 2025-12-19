# Nama: Khafid Rosidi
# NIM: 202453071

from util.user_input import ListOfChoice
from util.storage import Menu, Pesanan
from util.cli import enterAlternateScreen, exitAlternateScreen, clearScreen

from pages.manage_menu import ManageMenus
from pages.pesan import Kasir

class Main:
    def __init__(self) -> None:
        try:
            enterAlternateScreen()
            clearScreen()

            self.menu = Menu()
            self.pesanan = Pesanan()
            self.kasir = Kasir(self.menu, self.pesanan)
            self.menus_manager = ManageMenus(self.menu, self.pesanan)
            
            self.main_display()
        except KeyboardInterrupt:
            print("Program exit by user")

        finally:
            exitAlternateScreen()
            print("Bye")
        pass

    def main_display(self):
        while True:
            ans = ListOfChoice(
                "[Main Menu] Restoran Ku V.1.0",
                ["kelola menu", "kasir"],
                use_number=True,
                exiteable=True
            ).show()

            if ans == 0:
                self.menus_manager.manage_options()
            elif ans == 1:
                self.kasir.kasir_option()
            elif ans == None:
                return

        


if __name__ == "__main__":    
    Main()