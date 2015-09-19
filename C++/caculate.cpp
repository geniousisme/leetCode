#include "include/common.h"

int main(void) {
    float sum = 1;
    for (int num = 365; num > 345; num--) {
        sum *= float(num) / 365;
    };
    cout << "sum: " << sum << endl;
};
