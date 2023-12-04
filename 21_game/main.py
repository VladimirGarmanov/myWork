from random import *
cards = [0,0,"валет", "дама","король", 5,6,7,8,9,10, "туз"]
def step(player):
    print(f"Ходит {player} игрок: ")
    ans = ""
    score = 0
    while ans!= "n" and score < 20:
        card = randint(2,len(cards)-1)
        score += card
        print(f"{cards[card]}-{score}")
        ans = input('Еще?(y/n) ')
    return score
def end_game(scores):
    value = scores[0]
    wins=[0]
    for i in range(len(scores)):
        if scores[i] < 22:
            if value < scores[i]:
                value = scores[i]
                wins.clear()
                wins.append(i)
        elif value == scores[i]:
            wins.append(i+1)
    print(wins)

print("START")
n = int(input('Количество игроков: '))
scores = []
for i in range(1, n+1):
    scores.append(step(i))
end_game(scores)