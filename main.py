# Andrejs Piroženoks, ap24069
# Program created: 2024/09/12

# B1. Given natural number n. Collect all such pairs of natural numbers (a,b)
# which are less or equal to n, and a equals the sum of all divisors of b (except
# b itself) and vice versa.


# /// @brief Calculates the sum of all divisors of num except num itself.
# ///
# /// Returns 0 if num <= 1. Complexity: O(sqrt(n)).
# /// @param num whose divisors will be
# /// @return Sum of divisors.

#     int res = 1;


#     int div;

#     // The loop only checks number in the range [2; sqrt(num),
#     // because given one divisor a in range [2; sqrt(num), we can find the
#     // corresponding divisor b in range (sqrt(num); num): a = num / b
#     for (div = 2; div * div < num; div++) {
#         if (num % div == 0) {
#             res += div;
#             res += num / div;
#         }
#     }

#     // Separate handling of case when num is a perfect square.
#     // Divisor that is a square root of a number only needs to be added once.
#     if (div * div == num) {
#         res += div;
#     }

#     return res;
# }


def get_divisor_sum(num: int) -> int:
    if num <= 1:
        return 0

    res = 1

    div = 2
    while div * div < num:
        if num % div == 0:
            res += div
            res += num // div
        div += 1

    if div * div == num:
        res += div

    return res


# /// @brief Finds all pairs of natural numbers (a, b) satisfying certain
# /// condition.
# ///
# /// Finds all pairs of natural numbers (a, b) satisfying the following
# /// conditions:
# /// - a <= n;
# /// - b <= n;
# /// - a is equal to sum of all divisors of b, except b itself;
# /// - b is equal to sum of all divisors of a, except a itself;
# /// @note Pairs (x, y) and (y, x) are considered different and returned
# /// separately.
# /// @param n largest value of a and b allowed
# /// @return Vector of pairs containing the solution. Result is sorted in
# /// ascending order by first pair key.
# PairVector find_pairs(int n) {
#     // if (n == 1) {
#     //     return {{1, 1}};
#     // }

#     PairVector result({{1, 1}});

#     for (int a = 1; a <= n; a++) {
#         int b = get_divisor_sum(a);

#         if (b > n) {
#             continue;
#         }

#         int a_sum = get_divisor_sum(b);

#         if (a_sum != a) {
#             continue;
#         }

#         result.push_back({a, b});
#     }

#     return result;
# }


def find_pairs(n: int) -> list[tuple(int, int)]:
    if n <= 0:
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


# /// @brief Utility that prints out a vector.
# /// @param vec vector to print out
# void print_vec(const PairVector& vec) {
#     std::cout << "[\n";
#     for (const auto& p : vec) {
#         std::cout << "\t(" << p.first << ", " << p.second << "),\n";
#     }
#     std::cout << "]\n";
# }


def pretty_print_list(l: list) -> None:
    # i am sorry, truly i am
    # we convert each element of l into a string, prepend "\t" and append ",\n"
    # then we collect all of elements into a single strings and add brackets on
    # either end
    print("[\n" + "".join(map(lambda x: f"\t{x},\n", l)) + "]\n")


# /// @brief Prompts user for a natural integer.
# /// @return Integer input by the user.
# int input_int() {
#     while (true) {
#         std::string input;
#         std::cin >> input;

#         int integer;
#         try {
#             integer = std::stoi(input);
#         } catch (std::out_of_range) {
#             std::cout << "Provided integer is out of range." << std::endl;
#             continue;
#         } catch (std::invalid_argument) {
#             std::cout << "Please enter a valid integer." << std::endl;
#             continue;
#         }

#         if (integer <= 0) {
#             std::cout << "Please enter a natural integer." << std::endl;
#             continue;
#         }

#         return integer;
#     }
# }


def input_int() -> int:
    while True:
        try:
            inp = int(input().strip())
        except ValueError:
            print("Please enter a valid integer")
            continue

        if inp <= 0:
            print("Please enter a natural integer")
            continue

        return inp


def input_bool() -> bool:
    while True:
        print("1 - yes; 2 - no")
        i = input_int()
        if i > 2:
            print("Invalid choice.")
            continue

        return i == 1


def calculation() -> None:
    print("Please enter number n.")
    n = input_int()
    data = find_pairs(n)
    print("Result:\n")
    pretty_print_list(data)


# /// @brief Wrapper around find_pairs with textual I/O.
# void calculation() {
#     std::cout << "Please enter number n." << std::endl;
#     int n = input_int();

#     PairVector data = find_pairs(n);
#     std::cout << "Result:\n";
#     print_vec(data);

#     // print_vec does not flush output stream, but this manual flush is still
#     // redundant, because right after prompt to repeat calculation will flush
#     // still, this flush is left here, just in case this function will be called
#     // separately.
#     flush(std::cout);
# }


def main() -> None:
    while True:
        calculation()
        print("Repeat?")
        if not input_bool():
            break
