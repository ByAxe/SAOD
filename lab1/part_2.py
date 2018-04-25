class Node:
    def __init__(self, number=None, next=None):
        self.number = number
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add_e(self, n):
        if self.first is None:
            self.first = Node(n, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(n, None)
            self.first.next = self.last
        else:
            current = Node(n, None)
            self.last.next = current
            self.last = current

    def del_e(self, mono):
        if self.first is None:
            return
        old = curr = self.first
        if self.first == mono:
            self.first = self.first.next
            return
        while curr is not None:
            if curr == mono:
                if curr.next == self.last:
                    old.next = self.last
                    break
                else:
                    old.next = curr.next
                break
            old = curr
            curr = curr.next

    def length_l(self):
        self.length = 0
        if self.first is not None:
            self.length += 1
            current = self.first
            while current.next is not None:
                current = current.next
                self.length += 1
        return self.length

    def clear(self):
        self.__init__()

    def fill_circle(self, count):
        number = 1
        while count > 0:
            self.add_e(number)
            count -= 1
            number += 1

    def counted(self, k):
        sequence = []
        remaining = []
        current_number = 1
        while self.length_l() > 1:
            current = self.first
            while current is not None:
                if current_number == k:
                    sequence.append(current.number)
                    next = current.next
                    self.del_e(current)
                    current_number = 1
                    current = next
                    continue
                current = current.next
                current_number += 1
        curr = self.first
        while curr is not None:
            remaining.append(curr.number)
            curr = curr.next
        return sequence, remaining


if __name__ == '__main__':
    p = LinkedList()
    p.fill_circle(int(input("Enter (N)umber of people: ")))
    print(str(p.counted(int(input("Enter k: ")))))
    kg = int(input("Enter k for N so that 1 <= N <= 64: "))
    print("If k = " + str(kg) + " for N  from 1 to 64:")
    i = 1
    while i <= 64:
        p.clear()
        p.fill_circle(i)
        seq, rem = p.counted(kg)
        print(str(i) + ": " + str(rem))
        i += 1
