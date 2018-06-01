class Stack:
    def __init__(self):
        self.storage = []

    def take(self):
        return self.storage.pop()

    def add(self, value):
        self.storage.append(value)

    def watch(self):
        return self.storage[-1]

    def concat(self, arr):
        return self.storage.extend(arr)

    def __str__(self):
        return str(self.storage)

    def __len__(self):
        return len(self.storage)

    def isEmpty(self):
        return self.storage == []

    def peek(self):
        return self.storage[len(self.storage) - 1]


def reverse(str):
    return ("".join(reversed(str)))


def priority(operator):
    if operator == '+' or operator == '-':
        return 1

    elif operator == '*' or operator == '/' or operator == '%':
        return 2

    elif operator == '^':
        return 3

    else:
        return 0


def infixtoprefix(infixString):
    infixString = reverse(infixString)

    stack = Stack()
    prefixString = ""
    i = 0

    while i in range(0, len(infixString)):

        if infixString[i].isalpha():
            prefixString += infixString[i]

        elif infixString[i] == ')' or infixString[i] == ']' or infixString[i] == '}':
            stack.add(infixString[i])


        elif infixString[i] == '(' or infixString[i] == '[' or infixString[i] == '{':

            if infixString[i] == '(':
                while stack.watch() != ')':
                    prefixString += stack.take()
                stack.take()

            if infixString[i] == '[':
                while watch() != ']':
                    prefixString += stack.take()
                stack.take()

            if infixString[i] == '{':
                while stack.watch() != '}':
                    prefixString += stack.take()
                stack.take()

        else:

            if len(stack) == 0:
                stack.add(infixString[i])

            else:

                if priority(infixString[i]) >= priority(stack.watch()):
                    stack.concat(infixString[i])

                elif priority(infixString[i]) < priority(stack.watch()):
                    prefixString += stack.take()
                    position = len(stack) - 1

                    while position >= 0 and priority(stack[position]) > priority(infixString[i]):
                        prefixString += stack.take()
                        position -= 1
                        if position < 0:
                            break

                    stack.concat(infixString[i])

        i += 1

    while len(stack) != 0:
        prefixString += stack.take()

    prefixString = reverse(prefixString)

    return ' '.join(prefixString)


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = ' '.join(infixexpr).split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.add(token)
        elif token == ')':
            topToken = opStack.take()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.take()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.take())
            opStack.add(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.take())

    return " ".join(postfixList)


def infToPrefPostf(ext):
    print(ext)
    print(infixToPostfix(ext))
    print(infixtoprefix(ext))


if __name__ == '__main__':
    inp = ""
    while inp != "end":
        value = input('Введите выражение')
        infToPrefPostf(value)
        inp = input()
