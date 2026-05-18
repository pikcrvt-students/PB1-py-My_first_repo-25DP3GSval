#include <iostream>

int main() {
    float x, y;
    x = -3.0;
    do {
        y = 2 * x - 1;
        std::cout << "x=" << x << "y=" << y << std::endl;
        x = x + 0.5;
    } while(x <= 1);

    return 0;
}