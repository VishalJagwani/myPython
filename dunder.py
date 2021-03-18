# special functions
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'StarVJ',
            'has_pets': False
        }

    # Don't do this; Only for special cases
    # def __str__(self):
    #     return f'{self.color}'
    # def __len__(self):
    #     return 5
    # def __call__(self):
    #     print('Yes??')
    # def __getitem__(self, i):
    #     return self.my_dict[i]


action_figure = Toy('Red', 0)
# Below two are same
print(action_figure.__str__())
print(str(action_figure))
# print(len(action_figure)) for len dunder
# print(action_figure()) for call dunder
# print(action_figure['name'])
