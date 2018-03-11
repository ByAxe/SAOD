class Node:
    def __init__(self, power=None, constant=None, next=None):
        self.power = power
        self.constant = constant
        self.next = next


class Polynomial:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'Polynomial: ' + str(current.constant) + 'x^' + str(current.power)
            while current.next is not None:
                current = current.next
                out += ' + ' + str(current.constant) + 'x^' + str(current.power)
            return out
        return 'Polynomial is empty'

    def clear(self):
        self.__init__()

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = node
            self.head.next = self.tail
        else:
            current = node
            self.tail.next = current
            self.tail = current

    def search_with_power(self, item):
        power = item.power

        current = self.head
        found = False
        element = current

        while current and not found:
            if current.power == power:
                found = True
            else:
                current = current.next

        return element if found else False
