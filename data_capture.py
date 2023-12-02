from typing import List, Dict


class DataCapture:
    """Data Capture class"""

    def __init__(self) -> None:
        self.data: List[int] = []
        self.counter: Dict[str, int] = {
            'less': 0,
            'greater': 0,
            'equal': 0
        }

    def add(self, number: int) -> None:
        self.data.append(number)
        if number in self.counter:
            self.counter['equal'] += 1
        elif number < self.data[0]:
            self.counter['less'] += 1
        else:
            self.counter['greater'] += 1

    def build_stats(self) -> 'Stats':
        class Stats:
            def __init__(self, counter: Dict[str, int], data: List[int]) -> None:
                self.counter = counter
                self.data = data

            def less(self, value: int) -> int:
                if value in self.counter:
                    return self.counter['less']
                return len([num for num in self.data if num < value])

            def greater(self, value: int) -> int:
                if value in self.counter:
                    return self.counter['greater']
                return len([num for num in self.data if num > value])

            def between(self, low: int, high: int) -> int:
                less_than_low = self.less(low)
                greater_than_high = self.greater(high)
                return len(self.data) - less_than_low - greater_than_high

        return Stats(self.counter, self.data)

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()


#print(stats.less(4))
#print(stats.between(3, 6))
#print(stats.greater(4))
