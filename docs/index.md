## C语言接口与实现

## 特斯拉，读书与对话

## 编译，思维，理解，表达

## 

## 
## {0, 1}
The simplest set represents the difference.

0, 1 are just symbols in the alphabet of size 2.
Let 1-bit variable, hold either 0 or 1.

## Operations on the variable(s)
- unary:
  - NOT: represents a change, either from 0 to 1, or from 1 to 0.
- binary:
  - The simplest relationship involves two variables. Let's care about the symmetrical relaitonships only.

| input | Gnd | NOR | XOR | NAND | AND | XNOR | OR | Vcc |
| ----- | - | - | - | - | - | - | - | - |
|    00 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 01/10 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
|    11 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
 
With the help of NOT, we can reduce the operations into three:

- AND
- OR
- XOR: $F_{SOP} = A\cdot\bar{B} + \bar{A}\cdot B$; $F_{POS} = (A+B)\cdot(\bar{A} + \bar{B})$

These operations are communitive and associative, so they can apply to multiple variables to form relationship:

- ALL
- ANY

## Truth Table


| $I_{n-1}$ | ... | $I_1$ | $I_0$ |-| $O_{m-1}$ | ... | $O_1$ | $O_0$ |
| --------- | --- | ----- | ----- |-| --------- | --- | ----- | ----- |
|         0 | ... |     0 |     0 |-|         1 | ... |     0 |     1 |
|         0 | ... |     0 |     1 |-|         0 | ... |     1 |     1 |
|       ... | ... |   ... |   ... |-|       ... | ... |   ... |   ... |
|         1 | ... |     1 |     1 |-|         1 | ... |     1 |     0 |

Every $O_j$ for $j \in \{0, 1, \cdots, m-1\}$, is a function of $\{I_{0},I_{1},\cdots,I_{n-1}\}$,
which can be represented as POS or SOP.

- Think SOP as `any of the possible 1 filters work`
- Think POS as `all the 0 filters failed`

## 
LISP揭示了程序语言的本质，LISP程序本身就是一个AST。非叶子结点代表操作符，其叶子结点代表操作数。
