#include <stdio.h>

int main()
{
    long long count = 0;
    while (1)
    {
        count++;
        if (count % 1000000000 == 0) {
            printf("\r%010lld", count);
        }
    }
}