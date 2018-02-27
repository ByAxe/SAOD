class Polynomial:
    def __init__(self):
        self.head = None

    def add(self, item):
        item.set_next(self.head)
        self.head = item

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current == item:
                found = True
            else:
                current = current.get_next()

        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()

        return count

    def meaning(self, x):
        if self.size == 0:
            return 0

        current = self.head
        result = 0
        while current:
            result += current.constant * (x ** current.power)
            current = current.getNext()

        return result

    def __str__(self):
        print(self.head)

    def __eq__(self, other):
        size = other.size()
        head = other.head

        if self.size() != size:
            return False

        for i in range(size + 1):
            found = self.search(head)

            if not found:
                return False
            else:
                head = head.get_next()

        return True


class Node:

    def __init__(self, power=0, constant=0, sign='x'):
        self.next = None
        self.power = power
        self.constant = constant
        self.sign = sign

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __self_string__(self):
        return '(' + str(self.constant) + self.sign + '^' + str(self.power) + ')'

    def __str__(self):
        return self.__self_string__() + ' + ' + self.next

    def __eq__(self, other):
        return self.constant == other.constant and self.power == other.power
