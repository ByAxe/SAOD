import copy


class Node:
    def __init__(self, power=None, base=None, next=None):
        self.power = power
        self.base = base
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.var = 'x^'

    def __str__(self):
        if self.first:
            current = self.first
            out = 'Polynomial ' + str(current.base) + self.var + str(current.power)
            while current.next:
                current = current.next
                out += ' + ' + str(current.base) + self.var + str(current.power)
            return out
        return 'Polynomial is empty!'

    def add(self, a, x):
        if self.first is None:
            self.first = Node(x, a, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, a, None)
            self.first.next = self.last
        else:
            current = Node(x, a, None)
            self.last.next = current
            self.last = current

    def mean(self, x):
        sum_ = 0
        if self.first is None:
            return sum_
        current = self.first
        while current is not None:
            sum_ += current.base * (x ** current.power)
            current = current.next
        return sum_


def equality(p1, p2, x):
    if p1.mean(x) == p2.mean(x):
        print('Polynomials are equal')
    else:
        print('Polynomials are not equal')


def add(p1, p2) -> LinkedList:
    p3 = copy.deepcopy(p1)
    current1 = p2.first
    while current1 is not None:
        current2 = p3.first
        flag = False
        while current2 is not None:
            if current1.power == current2.power:
                current2.base += current1.base
                flag = True
                break
            current2 = current2.next
        if not flag:
            p3.add(current1.power, current1.base)
        current1 = current1.next
    return p3


if __name__ == '__main__':
    poly1, poly2, poly3 = LinkedList(), LinkedList(), LinkedList()
    input_ = None

    print('Now you are entering a first polynomial')
    print('If you want to finish with this fist one -> enter \'end\' (without quotes)')

    while input_ != 'end':
        poly1.add(int(input('Enter a base of number: ')), int(input('Enter a power of number: ')))
        print('(To go to the next number -> press Enter on your keyboard)')
        input_ = input()

    print(poly1, '\n')
    input_ = None

    print('Now you are entering a second polynomial')
    print('If you want to finish with this second one -> enter \'end\' (without quotes)')

    while input_ != 'end':
        poly2.add(int(input('Enter a base of number: ')), int(input('Enter a power of number: ')))
        print('(To go to the next number -> press Enter on your keyboard)')
        input_ = input()

    print(poly2)

    equality(poly1, poly2, 2)

    x = int(input('Enter x: '))

    print(poly1.mean(x))
    print(poly2.mean(x))

    poly3 = add(poly1, poly2)

    print(poly3)
