class Person:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5, 6, 7, 8]

    def __setitem__(self, key, value):
        print("set", key, value)
        self.items[key] = value

    def __getitem__(self, key):
        print(key)
        return self.items[key]

p = Person()

p.items.append(9)
p.items.append(10)
p.items.append(11)
p[0:5:2] = ["One", "Two", 'Three']

print(p.items)

