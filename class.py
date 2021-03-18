# OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if (self.membership):
            self.name = name   # attributes
            self.age = age

    def run(self):
        print('Run')
        return 'Done'

    @classmethod
    def adding_num(cls, num1, num2):
        return cls('Tim', num1 + num2)

    @staticmethod
    def addding2(num1, num2):
        return num1 + num2


# now we can create instance using method
player3 = PlayerCharacter.adding_num(12, 9)
print(player3.age)

# without instantiation we can use method to add
# print(PlayerCharacter.adding_num(2, 3))
# Instantiation means creating instances
player1 = PlayerCharacter('StarVJ', 30)
player2 = PlayerCharacter('Wizard', 100)

print(player1.name)
print(player1.age)
print(player1.run())
print(player2.name)
print(player2.age)
