# Stack code from class lectures
class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Empty stack, nothing to pop")
            return
        else:
            self.size -= 1
            return self.items.pop()

    def top(self):
        if self.is_empty():
            print("Empty stack, nothing on top")
            return
        else:
            return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def __str__(self):
        return "[" + ",".join(str(item) for item in self.items) + "]"
