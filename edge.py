class Edge:

    def __init__(self):
        """nothing to initialize, assume set gets called right after"""

    def print_state(self):
        print "edge:", "[", self.i, self.j, "] -> c:", self.c, " f: ", self.f

    def set(self, i, j, c=0, f=0):
        self.i = i
        self.j = j
        self.c = c
        self.f = 0
