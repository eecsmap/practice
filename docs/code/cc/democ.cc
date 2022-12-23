#include <stdio.h>
#include <iostream>

int main()
{
    long long count = 0;
    while (1)
    {
        count++;
        if (count % 1000000000 == 0) {
            std::cout << count << std::endl;
        }
    }
}