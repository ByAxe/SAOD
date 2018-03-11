import copy

from lab1 import Polynomial, Node


def meaning(poly, variable):
    result = 0

    if poly.head is None:
        return result

    current = poly.head

    while current:
        result += current.constant * (variable ** current.power)
        current = current.next

    return result


def equality(poly1, poly2, variable):
    return meaning(poly1, variable) == meaning(poly2, variable)


def add(poly1: Polynomial, poly2: Polynomial):
    result = copy.deepcopy(poly1)
    current_p2 = poly2.head

    while current_p2:
        found = result.search_with_power(current_p2)
        if not found:
            result.add(current_p2)
        else:
            found.constant += current_p2.constant

        current_p2 = current_p2.next

    return result

def p() -> Polynomial:
    result = Polynomial()

    result.add(Node(constant=2, power=0))
    result.add(Node(constant=-1, power=1))
    result.add(Node(constant=3, power=2))
    result.add(Node(constant=7, power=4))

    return result


def q() -> Polynomial:
    result = Polynomial()

    result.add(Node(constant=-6, power=0))
    result.add(Node(constant=1, power=1))
    result.add(Node(constant=2, power=3))
    result.add(Node(constant=-2, power=5))

    return result


if __name__ == '__main__':
    p = p()
    print('P(x) =', str(p))

    q = q()
    print('Q(x) =', str(q))

    print('\nMust be true:', str(equality(p, p, 10)))
    print('Must be false:', str(equality(p, p, 10)))

    r = add(p, q)

    print('\nP(x) + Q(x) =', str(r))
