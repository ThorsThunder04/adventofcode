#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <stdio.h>

#define ull unsigned long long

using namespace std;

bool id_in_ranges(vector<array<ull,2>> &ranges, ull id) {

    for (int i = 0; i < (int)ranges.size(); i++) {

        if (id >= ranges[i][0] && id <= ranges[i][1]) {
            return true;
        }
    }
    return false;
}


/*
 * Bad because O(n) lookup for each ID
 *
 * Minimum optimisation to do: unify the ranges when they overlap / are sub-ranges (must be done anyway to do part 2)
 */
int main() {

        vector<array<ull, 2>> ranges;

        string line;
        int n = 0;

        while (getline(cin, line) && !line.empty()) {
                array<ull, 2> range;

                sscanf(line.c_str(), "%llu-%llu", &(range[0]), &(range[1]));

                ranges.push_back(range);
                n++;
        }
        cin >> ws;

        int n_fresh = 0;

        while (getline(cin, line)) {
            ull id = stoull(line);

            if (id_in_ranges(ranges, id)) n_fresh++;

        }

        cout << n_fresh << endl;


        return 0;
}
