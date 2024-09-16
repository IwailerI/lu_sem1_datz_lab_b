# Andrejs Piroženoks, ap24069
# Program created: 2024/09/12

# B1. Given natural number n. Collect all such pairs of natural numbers (a,b)
# which are less or equal to n, and a equals the sum of all divisors of b (except
# b itself) and vice versa.


def get_divisor_sum(num: int) -> int:
    """Calculates the sum of all divisors of num except num itself.
    Returns 0 if num <= 1. Complexity: O(sqrt(n)).

    :param num: number whose divisors will be
    :type num: int
    :return: Sum of divisors.
    :rtype: int
    """

    # Any number is divisible by 1, so we start with it.
    # (Degenerate case of num==1 is handled earlier)
    if num <= 1:
        return 0

    # The loop only checks number in the range [2; sqrt(num),
    # because given one divisor a in range [2; sqrt(num), we can find the
    # corresponding divisor b in range (sqrt(num); num): a = num / b
    res = 1
    div = 2
    while div * div < num:
        if num % div == 0:
            res += div
            res += num // div
        div += 1

    # Separate handling of the case when num is a perfect square.
    # Divisor that is a square root of a number only needs to be added once.
    if num > 1 and div * div == num:
        res += div

    return res


def find_pairs(n: int) -> list[tuple[int, int]]:
    """Finds all pairs of natural numbers (a, b) satisfying certain condition.

    Finds all pairs of natural numbers (a, b) satisfying the following
    conditions:
    - 1 <= a <= n;
    - 1 <= b <= n;
    - a is equal to sum of all divisors of b, except b itself;
    - b is equal to sum of all divisors of a, except a itself;

    Note: pairs (x, y) and (y, x) are considered different and returned
    separately.

    :param n: largest value of a and b allowed
    :type n: int
    :return: List of pairs containing the solution. Result is sorted in
    ascending order by first elements of tuples.
    :rtype: list[tuple(int, int)]
    """

    if n <= 1:
        return []

    result = []
    for a in range(1, n + 1):
        b = get_divisor_sum(a)
        if b > n:
            continue

        a_sum = get_divisor_sum(b)
        if a_sum != a:
            continue

        result.append((a, b))

    return result


def pretty_print_list(l: list) -> None:
    """Utility that prints out a list nicely.

    :param l: list of printable elements
    :type l: list
    """

    # i am sorry, truly i am
    # we convert each element of l into a string, prepend "\t" and append ",\n"
    # then we collect all of elements into a single strings and add brackets on
    # either end
    print("[\n" + "".join(map(lambda x: f"\t{x},\n", l)) + "]\n")


def input_int() -> int:
    """Prompts user for a natural number.

    :return: value provided by the user
    :rtype: int
    """

    while True:
        string = input()

        try:
            integer = int(string)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if integer <= 0:
            print("Please enter a natural number.")
            continue

        return integer


def input_bool() -> bool:
    """Prompts user for a boolean answer.

    :return: value provided by the user
    :rtype: bool
    """

    while True:
        print("1 - yes; 2 - no")
        i = input_int()
        if i > 2:
            print("Invalid choice.")
            continue

        return i == 1


def calculation() -> None:
    """Wrapper around find_pairs with textual I/O."""

    print("Please enter number n.")
    n = input_int()

    data = find_pairs(n)
    print("Result:")
    pretty_print_list(data)


def main() -> None:
    """Wrapper around calculation that repeats it multiple times."""
    while True:
        calculation()
        print("Repeat?")
        if not input_bool():
            break


if __name__ == "__main__":
    main()
