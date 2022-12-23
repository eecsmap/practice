#ifndef STACK_H
#define STACK_H

#include <stddef.h>
#include <stdbool.h>

/* 不透明指针 */
/* 不透露实现细节给客户程序 */
#define T cii_stack_t
typedef struct T *T;

T stack_new(void);
bool stack_empty(T stack);
void stack_push(T stack, void *x);
void *stack_pop(T stack);
void stack_free(T *stack);

#undef T

#endif
