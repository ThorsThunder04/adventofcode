#include <iostream>

using namespace std;

int main() {

    int pointer = 50;
    long n0 = 0;

    char dir;
    long rot;

    while (cin >> dir) {
        cin >> rot;

        int sign = (dir == 'L') ? -1 : 1;
        pointer = (pointer + sign*rot) % 100;

        if (pointer == 0) n0++;
    }

    cout << n0 << endl;

    return 0;
}