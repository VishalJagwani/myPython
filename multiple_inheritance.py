class User:
    def sign_in(self):
        print('Logged in')
        return 'Done'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')
        return 'Done'


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: Arrows left- {self.num_arrows}')
        return 'Done'

    def check_arrows(self):
        return f'{self.num_arrows} Remaining'

    def run(self):
        print('Ran really fast')


class MagicArcher(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


ma1 = MagicArcher('Sparky', 50, 100)
print(ma1.sign_in())
