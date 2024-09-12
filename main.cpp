#include <iostream>

void solve(int n) {
    int count = 0;

    for (int a = 1; a < n; a++) {
        int b = 1;
        // TODO: go until sqrt
        for (int div = 2; div < a; div++) {
            if (a % div == 0) {
                b += div;
            }
        }

        if (b > n) {
            continue;
        }

        int a_sum = 1;
        for (int div = 2; div < b; div++) {
            if (b % div == 0) {
                a_sum += div;
            }
        }

        if (a_sum != a) {
            continue;
        }

        count++;
        std::cout << a << " " << b << '\n';
    }

    std::cout << count << std::endl;
}

int main() { solve(10000); }