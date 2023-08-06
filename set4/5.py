class Queue:
    def __init__(self):
        self.S1 = []
        self.S2 = []

    def push(self, value):
        self.S1.append(value)

    def pop(self):
        if len(self.S2) == 0:
            if len(self.S1) == 0:
                return "undefined"
            else:
                while len(self.S1) > 0:
                    x = self.S1.pop()
                    self.S2.append(x)
        return self.S2.pop()

    def front(self):
        if len(self.S2) == 0:
            if len(self.S1) == 0:
                return None
            else:
                while len(self.S1) > 0:
                    x = self.S1.pop()
                    self.S2.append(x)
        return self.S2[-1]

    def is_empty(self):
        return len(self.S2) == 0
