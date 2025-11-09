from util.cli import clearScreen

class MenuList:
    def __init__(self, title: str, menus: list[str], use_number: bool = False, exiteable: bool = True):
        self.title = title
        self.menus = menus
        self.use_number = use_number
        self.exiteable = exiteable
        self.max_peritem = 5
        self.page = 0
        self.msg = "-> "

    def show(self):
        while True:
            clearScreen()
            print(self.title + "\n")

            start = self.page * self.max_peritem
            for i in range(self.max_peritem):
                if len(self.menus) <= start + i:
                    break
                label = f"({i+1}) " if self.use_number else ""
                print(f"{label}{self.menus[start + i]}")

            has_next = start + self.max_peritem < len(self.menus)

            if self.exiteable:
                print(f"{'(0) ' if self.use_number else ''}keluar")
            if self.page > 0:
                print(f"{f'({self.max_peritem+1}) ' if self.use_number else ''}sebelumnya (p)")
            if has_next:
                print(f"{f'({self.max_peritem+2}) ' if self.use_number else ''}selanjutnya (n)")

            print("\n\n")

            answ = input(self.msg).lower()
            self.msg = "-> "

            if self.use_number:
                try:
                    answ = int(answ)
                except ValueError:
                    self.msg = "(harus angka) ->"
                    continue

            if (answ in ["keluar", 0, "exit"]) and self.exiteable:
                return None
            
            elif (answ in [self.max_peritem + 2, "selanjutnya", "n"]) and has_next:
                self.page += 1
            elif (answ in ["sebelumnya", "p", self.max_peritem + 1]) and self.page > 0:
                self.page -= 1
            
            elif self.use_number and 0 < answ <= self.max_peritem:
                return answ - 1 + (self.page * self.max_peritem)
            elif answ in [menu.lower() for menu in self.menus]:
                for idx, menu in enumerate(self.menus):
                    if menu.lower() == answ:
                        return idx
            else:
                self.msg = "(Tidak Ditemukan) ->"


def input_int(prompt: str) -> int: 
    while True:
        try:
            ans = int(input(prompt))
            if (ans < 0): 
                continue
            return ans 
        except:
            input("input gagal. selahkan masukkan ulang. (tekan enter untuk melanjutkan)")