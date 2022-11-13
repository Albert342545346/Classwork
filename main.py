class LittleBell:
    def __init__(self):
        self.sound = "ding"


bell = LittleBell()
count = 1
for i in range(count):
    print(bell.sound)


class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def click_count(self):
        print(self.clicks)

    def reset(self):
        self.clicks = 0


class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, right):
        self.right += right

    def add_left(self, left):
        self.left += left

    def balance_result(self):
        if self.left == self.right:
            print('=')
        elif self.left > self.right:
            print('L')
        else:
            print('R')


class OddEvenSeperator:
    def __init__(self):
        self.odd = []
        self.even = []

    def add_number(self, number):
        if number % 2 == 0:
            self.odd.append(number)
        else:
            self.even.append(number)

    def even(self):
        return self.even

    def odd(self):
        return self.odd
