import random

print("Blackjack")
print("I am bored.")
print("Visit my github please: https://github.com/J3ldo")

possible_cards = [
    ["2", 2],
    ["3", 3],
    ["4", 4],
    ["5", 5],
    ["6", 6],
    ["7", 7],
    ["8", 8],
    ["9", 9],
    ["J", 10],
    ["K", 10],
    ["Q", 10],
    ["A", 1],
]


class Player:
    def __init__(self):
        self.possible_cards = possible_cards
        self.deck = {"player": [], "dealer": []}
        self.lost = False

        for i in range(2):
            self.deck["player"].append(random.choice(possible_cards))
        for i in range(2):
            self.deck["dealer"].append(random.choice(possible_cards))

        self.ppoint = 0
        for i in range(len(self.deck["player"])):
            self.ppoint += self.deck["player"][i][1]

        self.dpoint = 0
        for i in range(len(self.deck["dealer"])):
            self.dpoint += self.deck["dealer"][i][1]

    def playergetcard(self):
        self.deck["player"].append(random.choice(possible_cards))

        self.ppoint = 0
        for i in range(len(self.deck["player"])):
            self.ppoint += self.deck["player"][i][1]

        if self.ppoint > 21:
            print(f"You've lost :(. Points: {self.ppoint}")
            self.lost = True

        elif self.ppoint == 21:
            print(f"You've won. Points: {self.ppoint}")
            self.lost = True

    def dealergetcard(self):
        while self.dpoint < 16:
            self.deck["dealer"].append(random.choice(possible_cards))

            self.dpoint = 0
            for i in range(len(self.deck["dealer"])):
                self.dpoint += self.deck["dealer"][i][1]

        if self.dpoint > 21 or self.dpoint < self.ppoint:
            print(f"You've won! Dealers points: {self.dpoint}")
            self.lost = True

        elif self.dpoint > self.ppoint:
            print(f"You've lost :( Dealers points: {self.dpoint}")
            self.lost = True

        else:
            print(f"You have tied. Points: {self.ppoint}")
            self.lost = True


def main():
    while True:
        print("\n\nStarting new game")
        player = Player()

        while not player.lost:
            playerdeck = ""
            for i in player.deck["player"]: playerdeck += f"{i[0]}, "
            playerdeck = playerdeck[:-2]
            print("Your deck:", playerdeck, "Total:", player.ppoint)
            print("Your choice: Hit (H) or Stand (S)")
            choice = input("> ")

            if choice.lower() == "hit" or choice.lower() == "h":
                player.playergetcard()

            elif choice.lower() == "stand" or choice.lower() == "s":
                player.dealergetcard()

            else:
                print("Put in a valid choice!")


if __name__ == '__main__':
    main()
