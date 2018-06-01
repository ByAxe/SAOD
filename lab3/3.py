class Node:
    def __init__(self, name, priority, next):
        self.name = name
        self.priority = priority
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def sorted_insert(self, n, p):
        if self.first is None:
            self.first = Node(n, p, self.last)
            return
        if self.first.priority <= p:
            self.first = Node(n, p, self.first)
            return
        old = curr = self.first
        while curr is not None:
            if curr.priority <= p:
                curr = Node(n, p, curr)
                old.next = curr
                return
            old = curr
            curr = curr.next
        curr = Node(n, p, None)
        old.next = curr


def find_name(drct, name):
    if drct.first is None:
        print("Очередь пуста.")
        return
    current = drct.first
    while current:
        if current.name == name:
            return current.name + ":" + str(current.priority)
        current = current.next
    print("Такого имени нет в очереди.")


def d_del(drct, name):
    if (drct.first is None):
        print("Очередь пуста.")
        return
    old = curr = drct.first
    if drct.first.name == name:
        drct.first = drct.first.next
        return
    while curr:
        if curr.name == name:
            if curr.next == drct.last:
                drct.last = curr
                break
            else:
                old.next = curr.next
            break
        old = curr
        curr = curr.next


def prt(drct):
    if (drct.first is None):
        print("Очередь пуста.")
        return
    curr = drct.first
    while curr:
        print(curr.name + ":" + str(curr.priority))
        curr = curr.next


if __name__ == '__main__':
    directory = LinkedList()
    inp = ""
    while inp != "end":
        inp = input("Выберите действие (добавить(a), удалить(d), найти(f), вывести очередь(p): ")
        if inp == "a":
            directory.sorted_insert(input("Введите имя: "), input("Введите приоритет: "))
        if inp == "d":
            d_del(directory, input("Введите имя, которое хотите удалить: "))
        if inp == "f":
            n = find_name(directory, input("Введите имя, которое хотите найти: "))
            print(n)
        if inp == "p":
            prt(directory)
        inp = input()
