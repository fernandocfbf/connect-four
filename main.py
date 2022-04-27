from src.classes.AutoPlayer import AutoPlayer
from src.classes.FourInRow import FourInRow
from src.classes.RandomPlayer import RandomPlayer
from src.classes.BarthPlayer import BarthPlayer

def main():
    FourInRow(AutoPlayer(), RandomPlayer()).game()

if __name__ == '__main__':
    main()