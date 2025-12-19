def enterAlternateScreen():
    print("\033[?1049h", end="")


def exitAlternateScreen():
    print("\033[?1049l", end="")


def clearScreen():
    print("\033[2J\033[H", end="")

def clearLastLine():
    print("\033[F\033[K", end="")