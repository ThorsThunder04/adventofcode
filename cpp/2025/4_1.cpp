#include <iostream>
#include <vector>
#include <string>

using namespace std;


int hm_adj(vector<string> &grid, int r, int c) {
    int rows = (int)grid.size();
    int cols = (int)grid[0].size();

    int num_adj_rolls = 0;

    // just me complicating my life by not hardcoding this
    int ros = -1, cos = -1, roe = 1, coe = 1;

    if (r == 0) ros = 0;
    if (r == rows-1) roe = 0;
    if (c == 0) cos = 0;
    if (c == cols-1) coe = 0;

    for (int rr = r - ros; rr < r + roe; rr++) {
        for (int cc = c - cos; cc < c + coe; cc++) {
            cout << grid[rr][cc];
            if (rr != r && cc != c && grid[rr][cc] == '@') num_adj_rolls++;
        }
    }

    return num_adj_rolls;
}

int main() {

    vector<string> roll_grid;

    string line;
    while (getline(cin, line)) {
        roll_grid.push_back(line);
    }

    int num_accessible = 0;
    cout <<roll_grid.size() << " " << roll_grid[0].size() << endl;
    for (int r = 0; r < (int)roll_grid.size(); r++) {
        for (int c = 0; c < (int)roll_grid[r].size(); c++) {

            if (hm_adj(roll_grid, r, c) < 4) {
                num_accessible++;
            }
        }
    }

    cout << num_accessible << endl;

    return 0;
}