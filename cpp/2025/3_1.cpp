#include <iostream>
#include <string>

using namespace std;

// We want the largest k possible for k*10 of the final digit
int first_battery(string bank) {
    int i = bank.size() - 3; // set index to third to last character
    int maxi = i+1;

    while (i >= 0) {
        // (I added this second condition after my first attempt lol. The test inputs didn't have this issue with the limited size)
        // second condition because if gives us more second batteries to choose from after
        // illustration: "96123911" we come across the first 9, largest jolt is then 91, unless we allow to move to the second one
        // Then the largest jolt is 96
        if (bank[i] > bank[maxi] || bank[maxi] == bank[i]) {
            maxi = i;
        }
        i--;
    }
    return maxi;
}

// We want the largest k that comes after fbi (after the first battery)
int second_battery(string bank, int fbi) {

    int maxi = fbi+1;

    for (int i = maxi+1; i < (int)bank.size(); i++) {
        if (bank[i] > bank[maxi]) {
            maxi = i;
        }
    }
    return maxi;
}

int main() {

    long total_jolt = 0;

    string bank;

    while (getline(cin, bank)) {
        int b1 = first_battery(bank);
        int b2 = second_battery(bank, b1);

        total_jolt += 10*(int)(bank[b1] - '0') + (int)(bank[b2] - '0');
    }

    cout << total_jolt << endl;

    return 0;
}