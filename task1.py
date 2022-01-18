# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

class With_index:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < len(self.iterable):
            z = self.start, self.iterable[self.start]
            self.start += 1
            return z

        else:
            raise StopIteration


a = [1, 2, 3, 4, 5, 6]

for i in With_index(a):
    print(i)
