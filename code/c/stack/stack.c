#include "stack.h"

#include <assert.h>
#include <stdlib.h>

#define T cii_stack_t
struct T {
    int count; // 比用size要妥当一些。
    struct node_s {
        void *data;
        struct node_s *next;
    } *head;
};

T stack_new(void)
{
    T stack = malloc(sizeof(*stack));
    assert(stack);
    stack->head = NULL;
    stack->count = 0;
    return stack;
}

bool stack_empty(T stack)
{
    assert(stack);
    return stack->count == 0;
}

void stack_push(T stack, void *x)
{
    struct node_s *t;

    assert(stack);
    t = malloc(sizeof(*t));
    assert(t);
    t->data = x;
    t->next = stack->head;
    stack->head = t;
    stack->count++;
}

void *stack_pop(T stack)
{
    void *x;
    struct node_s *t;

    assert(stack);
    assert(stack->count > 0);
    t = stack->head;
    stack->head = t->next;
    stack->count--;
    x = t->data;
    free(t);
    return x;
}
