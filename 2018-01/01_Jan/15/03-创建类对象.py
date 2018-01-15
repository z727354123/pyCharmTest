# tupleA = ()
def a (self):
    print(self.name)

Person = type("Person", (), {'name':'lisi', 'run':a})

p1 = Person()

p1.run()







