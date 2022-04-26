from src.classes.AutoPlayer import AutoPlayer
from src.classes.FourInRow import FourInRow
from src.classes.RandomPlayer import RandomPlayer

def main():
    FourInRow(AutoPlayer(co=0), RandomPlayer()).game()

if __name__ == '__main__':
    main()