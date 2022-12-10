class Bounds:
    def __init__(self, bounds):
        self.five = {'bounds': bounds[: 2], 'marks': ['5+', '5', '5-']}
        self.four = {'bounds': [bounds[1] - 1e-5, bounds[2]], 'marks': ['4+', '4', '4-']}
        self.three = {'bounds': [bounds[2] - 1e-5, bounds[3]], 'marks': ['3+', '3', '3-']}

    @staticmethod
    def checkIn(mark, bound):
        return min(bound) <= mark <= max(bound)

    def determineMark(self, mark: float) -> str:
        mark = round(mark, 0)
        if self.checkIn(mark, self.five['bounds']):
            marks = self.five['marks']
            bounds = self.five['bounds']
        elif self.checkIn(mark, self.four['bounds']):
            marks = self.four['marks']
            bounds = self.four['bounds']
        elif self.checkIn(mark, self.three['bounds']):
            marks = self.three['marks']
            bounds = self.three['bounds']
        else:
            return '2'
        delta = (max(bounds) - min(bounds)) / 3
        if self.checkIn(mark, [max(bounds), max(bounds) - delta]):
            return marks[0]
        elif self.checkIn(mark, [max(bounds) - delta, max(bounds) - 2 * delta]):
            return marks[1]
        else:
            return marks[2]

