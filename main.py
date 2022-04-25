from src.classes.AutoPlayer import AutoPlayer
from src.classes.FourInRow import FourInRow

def main():
    FourInRow(AutoPlayer(), AutoPlayer()).game()

if __name__ == '__main__':
    main()