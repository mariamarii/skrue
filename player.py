class Player:
    def __init__(self, numbers):
        self.cards = []
        self.numbers = numbers

    def pick_numbers(self):
        self.cards = [self.numbers.pop() for _ in range(4)]
        return self.cards
