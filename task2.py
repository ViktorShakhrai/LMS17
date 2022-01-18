# Create your own implementation of a built-in function range,
# named in_range(), which takes three parameters: `start`, `end`,
# and optional step. Tips: See the documentation for `range` function

class InRange:
    def __init__(self, stop, start=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            n = self.start
            self.start += self.step
            return n

        else:
            raise StopIteration


for i in InRange(10):
    print(i)
