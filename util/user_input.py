from util.cli import clearScreen, clearLastLine

class ListOfChoice:
    def __init__(self, title: str, choices: list[str], use_number: bool = False, exiteable: bool = True):
        self.title = title
        self.choices = choices
        self.use_number = use_number
        self.exiteable = exiteable
        self.max_peritem = 5
        self.page = 0
        self.msg = "-> "

    def update_choices(self, new_choices: list[str]):
        self.choices = new_choices
        
        # check page overflow
        max_page = len(self.choices) // self.max_peritem
        if self.page > max_page:
            self.page = max_page
        

    def show(self):
        if len(self.choices) == 0:
            return None
        
        while True:
            clearScreen()
            print(self.title + "\n")

            start = self.page * self.max_peritem
            for i in range(self.max_peritem):
                if len(self.choices) <= start + i:
                    break
                label = f"({i+1}) " if self.use_number else ""
                print(f"{label}{self.choices[start + i]}")

            has_next = start + self.max_peritem < len(self.choices)

            if self.exiteable:
                print(f"{'(0) ' if self.use_number else ''}keluar")
            if self.page > 0:
                print(f"{f'({self.max_peritem+1}) ' if self.use_number else ''}sebelumnya (p)")
            if has_next:
                print(f"{f'({self.max_peritem+2}) ' if self.use_number else ''}selanjutnya (n)")

            print("\n\n")

            answ = input(self.msg).lower()
            self.msg = "-> "

            # keluar tanpa menjawab
            if (answ in ["keluar", "0", "exit"]) and self.exiteable:
                return None    
             
            if self.use_number:
                try:
                    answ = int(answ)
                    if answ == self.max_peritem + 1 and self.page > 0:
                        self.page -= 1
                    elif answ == self.max_peritem + 2 and has_next:
                        self.page += 1
                    elif  0 < answ <= self.max_peritem:
                        return answ - 1 + (self.page * self.max_peritem)
                    else:
                        self.msg = "(Tidak Ditemukan) ->"
                except ValueError:
                    self.msg = "(harus angka) ->"
                    continue

            else:
                # pagination
                if (answ in [self.max_peritem + 2, "selanjutnya", "n"]) and has_next:
                    self.page += 1
                elif (answ in ["sebelumnya", "p"]) and self.page > 0:
                    self.page -= 1
                elif answ in [menu.lower() for menu in self.choices]:
                    for idx, menu in enumerate(self.choices):
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
            clearLastLine()

def input_float(prompt: str) -> float: 
    while True:
        try:
            ans = float(input(prompt))
            if (ans < 0): 
                continue
            return ans 
        except:
            input("input gagal. selahkan masukkan ulang. (tekan enter untuk melanjutkan)")
            clearLastLine()