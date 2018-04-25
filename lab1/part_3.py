import re


class Node:
    def __init__(self, full_name=None, number=None, next=None):
        self.full_name = full_name
        self.number = number
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

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


def find_surname(drct, num):
    if drct.first is None:
        print("Dictionary is empty.")
        return
    current = drct.first
    while current:
        if current.number == num:
            return re.findall(r"^\w+", current.full_name)[0]
        current = current.next
    print("There is no such number in dictionary.")


def find_numbers(drct, surname):
    numbers = []
    if drct.first is None:
        print("Dictionary is empty.")
        return
    current = drct.first
    while current:
        if re.findall(r"^\w+", current.full_name)[0] == surname:
            numbers.append(current.number)
        current = current.next
    if not numbers:
        print("There is no such last name in dictionary")
    return numbers


if __name__ == '__main__':
    directory = LinkedList()
    file_dir = open("dir.txt")
    for line in file_dir:
        directory.sorted_insert(re.findall(r"^\w+ \w+ \w+", line)[0], int(re.findall(r"\d{7}$", line)[0]))
    f_surname = find_surname(directory, int(input("Enter a number for searching a last name of the candidate: ")))
    if f_surname:
        print(f_surname)
    f_numbers = find_numbers(directory, input("Enter the last name for searching a number of the candidate: "))
    if f_numbers:
        print(f_numbers)
