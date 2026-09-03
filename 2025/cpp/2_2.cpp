
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

int n_digits(long long n) {
    int m = 0;
    while (n > 0) {
        n /= 10;
        m++;
    }
    return m;
}


void decomp_range(string s, long long range[2]) {
    // turn given string into stream
    istringstream in;
    in.str(s);

    // iterate the two bounds of the range LOWER-UPPER
    // store them in the array
    int i = 0;
    for (string bound; getline(in, bound, '-');i++) {
        range[i] = stoll(bound);
    }
}

int main() {

    long long s = 0;
    long long range[2];

    for (string rstr; getline(cin, rstr, ',');) {
        decomp_range(rstr, range);

        while (range[0] <= range[1]) {
            int nd = n_digits(range[0]);

            bool found = false;
            int k = 1;
            while (!found && k <= nd/2) {
                if (nd % k == 0) {
                    long long num = range[0] % (long long)pow(10, k);

                    long long id = range[0];

                    bool invalid_for_k = true;
                    while (id > 0) {
                        invalid_for_k = (invalid_for_k && (id % (long long)pow(10, k) == num));
                        id /= (long long)pow(10, k);
                    }
                    found = invalid_for_k;
                }
                k++;
            }
            if (found) s += range[0];

            range[0]++;
        }
    }

    cout << s << endl;

    return 0;
}