#include <stdio.h>
#include <iostream>
#include <string>
#include <list>
#include <vector>

using namespace std;

void collect_data(vector<int> & numbers, vector<char> & operators) {

    // get all the numbers
    int n;
    while (cin >> n) {
        numbers.push_back(n);
        cin >> ws;
    }

    // get all the operators
    char c;
    while ((c = fgetc(stdin)) != EOF) { // was not working with (cin >> c) for some reason
        if (c == '*' || c == '+') {
            operators.push_back(c);
        }
    }

}

int main() {

    vector<int> numbers;
    vector<char> operators;

    collect_data(numbers, operators);

    // initialize the result values for each column
    // this must be done since if the initial value of a product is 0, then the next multiplied value to that will also be 0
    int n = operators.size();
    long long results[n] = {0};
    for (int i = 0; i < operators.size(); i++) {
        if (operators[i] == '*') results[i] = 1;
    }

    // calculate the results of each column
    for (int i = 0; i < numbers.size(); i++) {

        int column = i % n;
        char op = operators[column];

        if (op == '*') results[column] *= numbers[i];
        else results[column] += numbers[i];

    }

    long long sol{0};
    for (int i = 0; i < n; i++) {
        sol += results[i];
    }


    cout << sol << endl;

    return 0;
}
