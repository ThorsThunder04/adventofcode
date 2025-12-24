#include <iostream>
#include <vector>
#include <string>

using namespace std;


int hm_adj(vector<string> &grid, int r, int c) {
    int rows = (int)grid.size();
    int cols = (int)grid[0].size();
    char tc = '@';

    int num_adj_rolls = 0;

    // I decided to hard code this just cuz I know that it will defo work like this
    // My iterative version felt a little overcomplicated anyway tbh

    if (r > 0) {
        if (c > 0 && grid[r-1][c-1] == tc) num_adj_rolls++;
        if (c < cols-1 && grid[r-1][c+1] == tc) num_adj_rolls++;
        if (grid[r-1][c] == tc) num_adj_rolls++;
    }

    if (c > 0 && grid[r][c-1] == tc) num_adj_rolls++;

    if (r < rows-1) {
        if (c > 0 && grid[r+1][c-1] == tc) num_adj_rolls++;
        if (c < cols-1 && grid[r+1][c+1] == tc) num_adj_rolls++;
        if (grid[r+1][c] == tc) num_adj_rolls++;
    }

    if (c < cols-1 && grid[r][c+1] == tc) num_adj_rolls++;

    return num_adj_rolls;
}

int main() {

    vector<string> roll_grid;

    string line;
    while (getline(cin, line)) {
        roll_grid.push_back(line);
    }

    int num_accessible = 0;
    for (int r = 0; r < (int)roll_grid.size(); r++) {
        for (int c = 0; c < (int)roll_grid[r].size(); c++) {

            if (roll_grid[r][c] == '@' && hm_adj(roll_grid, r, c) < 4) {

                num_accessible++;
            }
        }
    }

    cout << num_accessible << endl;

    return 0;
}