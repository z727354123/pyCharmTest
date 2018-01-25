# item
class Person:
    def __init__(self):
        self.cache = {}

    def __setitem__(self, key, val):
        print('set', key, val)
        self.cache[key] = val

    def __getitem__(self, key):
        print('get', key)
        return self.cache[key]

    def __delitem__(self, key):
        print('del', key)
        del self.cache[key]

p = Person()
p['name'] = 'Lisi'
print('print', p['name'])
print(p.cache)
del p['name']

# p[1:2:] = 123
