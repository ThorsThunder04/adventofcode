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

            // if the new range is completely included in an already existing range (don't insert the final calculated range)
            bool eaten = false;
            // iterate backwards because we will possibly be removing elements from the vector
            for (int i = (int)ranges.size() - 1; i >= 0 && !eaten; i--) {

                if (ranges[i][0] <= range[0] && range[1] <= ranges[i][0]) {
                    eaten = true;
                } else if (range[0] < ranges[i][0] && ranges[i][1] < range[1]) {// if there is a range completely encapsulated in the newly read one, just remove it (new one will be insterted later)
                    ranges.erase(ranges.begin() + i);
                } else if (range[0] < ranges[i][0] && range[1] <= ranges[i][1]) { // if the ranges intersect, delete old one, and replace `range` with their union
                    range[1] = ranges[i][1];
                    ranges.erase(ranges.begin() + i);
                } else if (ranges[i][0] <= range[0] && ranges[i][1] < range[1]) { // same as previous, but intersection at other end of the range
                    range[0] = ranges[i][0];
                    ranges.erase(ranges.begin() + i);
                }
                // cout << range[0] << ' ' << range[1] << endl;
            }
            if (!eaten) {
                ranges.push_back(range);
            }
            n++;
        }
        cin >> ws;

        int n_fresh = 0;

        // cout << "test";
        // cout << ranges.size();

        while (getline(cin, line)) {
            ull id = stoull(line);

            if (id_in_ranges(ranges, id)) n_fresh++;
        }

        cout << "OLD RES: " << n_fresh << endl;

        ull totdiff = 0;
        for (int i = 0; i < (int)ranges.size(); i++) {
            totdiff += ranges[i][1] - ranges[i][0];
        }

        cout << "NEW RES: " << totdiff << endl;





        return 0;
}
