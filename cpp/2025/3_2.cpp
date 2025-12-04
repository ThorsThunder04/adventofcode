#include <iostream>
#include <string>
#include <cmath>

using namespace std;


/*
 * Chooses the next largest battery jolt after the previous one, all while leaving
 * enough unchosen batteries after it for the remaining batteries
 *
 * @param (string) bank: the bank of batteries to choose from
 * @param (int) prev_i: the index of the previously chosen battery
 * @param (int) nbat_chosen: the number of batteries already chosen
 * @param (int) nbat: the total number of batteries we need to choose
 *
 * @returns the index of the next battery we should choose. So index of max(battery for battery within [prev_i, bank.size() - (nbat - nbat_chosen)])
 *
 */
int next_battery(string bank, int prev_i, int nbat_chosen, int nbat) {
    int bs = (int)bank.size();

    int maxi = prev_i + 1;

    for (int i = maxi; i < bs - (nbat - nbat_chosen - 1); i++) {
        if (bank[i] > bank[maxi])
            maxi = i;

    }

    return maxi;
}


int main() {

    long long total_joltage = 0;

    string bank;
    int joltage_size = 12;

    while (getline(cin, bank)) {
        char joltage[12] = {0};
        int j = -1;

        for (int i = 0; i < joltage_size; i++) {
            j = next_battery(bank, j, i, joltage_size);
            joltage[i] = bank[j];
        }

        for (int k = 0; k < joltage_size; k++) {
            total_joltage += (long long)pow(10, k)*(joltage[joltage_size - k - 1] - '0');
        }

    }

    cout << total_joltage << endl;

    return 0;
}