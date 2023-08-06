class Stack:
    def __init__(self):
        self.Q1 = []
        self.Q2 = []

    def push(self, value):
        self.Q2.append(value)
        while len(self.Q1) > 0:
            self.Q2.append(self.Q1.pop(0))
        self.Q1, self.Q2 = self.Q2, self.Q1

    def pop(self):
        if len(self.Q1) == 0:
            return "undefined"
        return self.Q1.pop(0)

    def top(self):
        if len(self.Q1) == 0:
            return "undefined"
        return self.Q1[0]

    def is_empty(self):
        return len(self.Q1) == 0
