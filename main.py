# Nama: Khafid Rosidi
# NIM: 202453071

from util.user_input import MenuList
from util.storage import Storage
from util.cli import enterAlternateScreen, exitAlternateScreen, clearScreen

from pages.manage_menu import ManageMenus
from pages.pesan import Kasir

class Main:
    def __init__(self) -> None:
        try:
            enterAlternateScreen()
            clearScreen()

            self.storage = Storage()
            self.kasir = Kasir(self.storage)
            self.menus_manager = ManageMenus(self.storage)
            
            self.main_display()
        finally:
            exitAlternateScreen()
            print("Bye")
        pass

    def main_display(self):
        while True:
            ans = MenuList(
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