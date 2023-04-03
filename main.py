class MyIterable:
def __init__(self, start, end):
self.start = start
self.end = end
def __iter__(self):
for i in range(self.start, self.end):
yield i
# Используем наш итерируемый объект for i in MyIterable(0, 5): print(i)