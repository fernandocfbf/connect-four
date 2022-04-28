from src.classes.FourInRow import FourInRow
from src.classes.RandomPlayer import RandomPlayer
from src.classes.BarthPlayer import BarthPlayer
from src.classes.AutoPlayer import AutoPlayer
from src.classes.ManualPlayer import ManualPlayer

players = [
    RandomPlayer(),
    AutoPlayer()]
    
points = {}
for p in players:
    points[p.name()] = 0

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = FourInRow(players[i], players[j]).game()
        points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = FourInRow(players[j], players[i]).game()
        points[winner] += 1

print('Results:')
print('\n')
print(points)
