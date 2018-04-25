import re


class Node:
    def __init__(self, full_name=None, number=None, next=None):
        self.full_name = full_name
        self.number = number
        self.next = next


class NodeT:
    def __init__(self, full_name=None, number=None, next=None, prev=None):
        self.full_name = full_name
        self.number = number
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, f, n):
        if self.first is None:
            self.first = NodeT(f, n, None, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = NodeT(f, n, None, self.first)
            self.first.next = self.last
        else:
            current = NodeT(f, n, None, self.last)
            self.last.next = current
            self.last = current

    def out1(self):
        if self.last:
            current = self.last
            out = "Список:\n"
            while current:
                out += current.full_name + " " + str(current.number) + "\n"
                current = current.prev
            return out
        else:
            return "Справочник пуст"

    def out(self):
        if self.first:
            current = self.first
            out = "Список отсортированных номеров:\n"
            while current:
                out += current.full_name + " " + str(current.number) + "\n"
                current = current.next
            return out
        else:
            return "Справочник пуст"

    def sorted_insert(self, f, n):
        if self.first is None:
            self.first = Node(f, n, self.last)
            return
        if self.first.full_name > f:
            self.first = Node(f, n, self.first)
            return
        old = curr = self.first
        while curr is not None:
            if curr.full_name > f:
                curr = Node(f, n, curr)
                old.next = curr
                return
            old = curr
            curr = curr.next
        curr = Node(f, n, None)
        old.next = curr


def build_list(drct, drct2):
    if drct.first is None:
        print("Справочник пуст.")
        return
    current = drct.last
    while current:
        if len(str(current.number)) == 7:
            drct2.sorted_insert(current.full_name, current.number)
        current = current.prev
    return


if __name__ == '__main__':
    directory = LinkedList()
    directory2 = LinkedList()
    file_dir = open("dir2.txt")
    for line in file_dir:
        directory.add(re.findall(r"^[^0-9]+", line)[0], int(re.findall(r"\d+$", line)[0]))
    print(directory.out1())
    build_list(directory, directory2)
    print(directory2.out())
