# C Interfaces and Implementations

决定来美国时，随身带了几本书，这本书是其中之一。

成都的一位同事，推荐过这本书，可惜我买来后，因为总总缘故没能看进去。但想着也许有一天会理解这本书的价值，于是携带了来。

时至今日，过了快十年，我总算慢慢开始理解它。

```c
#ifndef STACK_H
#define STACK_H

/* 不透明指针 */
/* 不透露实现细节给客户程序 */
typedef struct stack_s *stack_t;

stack_t stack_new(void);
bool stack_empty(stack_t stack);
void stack_push(stack_t stack, void *x);
void *stack_pop(stack_t stack);
void stack_free(stack_t *stack);

#endif
```

```c



```

## list

看起来一样的结构，其实对链表结构的不同描述（头，剩下的链表），以及（当前节点值，下一个节点）

```c
struct list
{
    void *head;
    struct list *tail;
};

struct node
{
    void *value;
    struct node *next;
}
```
