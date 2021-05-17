class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def __bool__(self):
        if self.last is None:
            return False
        return True

    def put(self, x):
        if self.last is None:
            self.last = Node(x, None)
        else:
            self.last = Node(x, self.last)

    def get(self):
        if self.last is None:
            return None
        else:
            res = self.last.value
            self.last = self.last.next

            return res
