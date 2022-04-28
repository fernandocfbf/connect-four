from src.classes.AutoPlayer import AutoPlayer
from src.classes.FourInRowPop import FourInRowPop
from src.classes.RandomPlayer import RandomPlayer
from src.classes.BarthPlayer import BarthPlayer

def main():
    FourInRowPop(AutoPlayer(), RandomPlayer()).game()

if __name__ == '__main__':
    main()