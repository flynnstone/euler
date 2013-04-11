class SumMultiples(object):

    """docstring for SumMultiples"""
    def __init__(self, arg):
        super(SumMultiples, self).__init__()
        self.arg = arg
        self.x = self.arg[0]
        self.y = self.arg[1]
        self.n = self.arg[2]

    def findSum(self):
        sum = 0.
        for z in xrange(1, self.n):
            if z % self.x == 0. or z % self.y == 0.:
                sum += z
        return sum
