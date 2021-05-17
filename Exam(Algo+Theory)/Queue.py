class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __bool__(self):
        if self.first is None:
            return False
        return True

    def put(self, x):
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def get(self):
        if self.first is None:
            return None
        else:
            res = self.first.value
            if self.last == self.first:
                self.first = self.last = None
            else:
                self.first = self.first.next

            return res
