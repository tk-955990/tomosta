class Items(object):
    def __init__(self) -> None:
        self._items = ['いちご', 'りんご', 'もも', 'キウイ']
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._items):
            raise StopIteration()

        item = self._items[self._i]
        self._i += 1
        return ' ◆ ' + item


my_items = Items()

for item in my_items:
    print(item)


# items = ['いちご', 'りんご', 'もも', 'メロン']

# i = 0
# while (i < 3):
#     print(items[i])
#     i += 1

# print("****************")

# for item in items:
#     print(item)
