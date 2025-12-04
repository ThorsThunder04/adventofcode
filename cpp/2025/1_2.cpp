
#include <iostream>

using namespace std;

/*
 * Don't ask, I was sick this day. It works.
 */
int main() {

    int pointer = 50;
    long n0 = 0;

    char dir;
    long rot;

    while (cin >> dir) {
        cin >> rot;
        if (dir == 'L') rot *= -1;

        if (rot < 0) {
            while (rot < 0) {
                pointer = (pointer - 1) % 100;
                rot++;
                if (pointer == 0) n0++;
            }
        } else if (rot > 0) {
            while (rot > 0) {
                pointer = (pointer  + 1) % 100;
                rot--;
                if (pointer == 0) n0++;
            }
        }
    }

    cout << n0 << endl;

    return 0;
}