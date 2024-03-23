#include <sys/stat.h>
#include <stddef.h>
#include <stdio.h>
#include <assert.h>

int main()
{
    off_t a = -1LL;
    size_t size = a;
    assert(sizeof size == sizeof a);
    if (a < 0) {
        printf("size_t is not large enough to hold off_t\n");
        return 1;
    }
    return 0;
}