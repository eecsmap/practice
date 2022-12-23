#include "stack.h"

#include <stdio.h>

#define T cii_stack_t

int main()
{
    T stack = stack_new();
    stack_push(stack, (void *)1);
    stack_push(stack, (void *)2);
    while (!stack_empty(stack))
    {
        printf("%d\n", (int)stack_pop(stack));
    }
}