class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')
        return 'Done'


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
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


wizard1 = Wizard('StarVJ', 257, 'thewizardofcr@gmail.com')
archer = Archer('Winner', 87)
print(wizard1.email)
# print(dir(wizard1)) for Object introspection
# print(archer.attack())

# print(isinstance(wizard1, Wizard))

# # polymorphism


# def attack(char):
#     char.attack()
#     return 'Done'


# print(attack(wizard1))
# print(attack(archer))
