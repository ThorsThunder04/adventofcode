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

bool rep_num(long long n) {
    int m = n_digits(n) / 2;

    // check if first half is equal to second half
    //* is there a bitwise op to figure this out easier ?
    return ((n % (int)pow(10, m)) == (n / (int)pow(10, m)));
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
            if (rep_num(range[0])) s += range[0];
            range[0]++;
        }

    }

    cout << s << endl;


    return 0;
}