import random

class dice(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.remainDices = list(range(6))
        random.shuffle(self.remainDices)
        self.remainDices[1:]

    def roll(self):
        # 0-3 normal (with color) dice, 4 black&white dice
        if not self.remainDices:
            raise IndexError

        color = self.remainDices.pop()

        flag = 1
        if color == 5:
            color = random.choice([5, 6])
            flag = -1

        return color, random.choice([1,2,3]) * flag