from src.classes.FourInRowPop import FourInRowPop
from src.classes.RandomPlayer import RandomPlayer
from src.classes.AutoPlayer import AutoPlayer

players = [
    RandomPlayer(),
    AutoPlayer()]
    
points = {}
for p in players:
    points[p.name()] = 0

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[i].name() + " vs "+players[j].name())
        winner = FourInRowPop(players[i], players[j]).game()
        points[winner] += 1 

for i in range(0,len(players)):
    for j in range(i+1, len(players)):
        print(players[j].name() + " vs "+players[i].name())
        winner = FourInRowPop(players[j], players[i]).game()
        points[winner] += 1

print('Results:')
print('\n')
print(points)
