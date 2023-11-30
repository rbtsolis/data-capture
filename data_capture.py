
class DataCapture:
  def __init__(self):
    self.data: list = []
    self.counter: dict = {
      'less': 0,
      'greater': 0,
      'equal': 0
    }

  def add(self, number):
    self.data.append(number)
    if number in self.counter:
      self.counter['equal'] += 1
    elif number < self.data[0]:
      self.counter['less'] += 1
    else:
      self.counter['greater'] += 1

  def build_stats(self):
    class Stats:
      def __init__(self, counter, data):
        self.counter = counter
        self.data = data

      def less(self, value):
        if value in self.counter:
          return self.counter['less']
        return len([num for num in self.data if num < value])

      def greater(self, value):
        if value in self.counter:
          return self.counter['greater']
        return len([num for num in self.data if num > value])

      def between(self, low, high):
        less_than_low = self.less(low)
        greater_than_high = self.greater(high)
        return len(self.data) - less_than_low - greater_than_high

    return Stats(self.counter, self.data)