
## General Rule

Note down exercises for EECS learning.

Practice to keep the cache hot.

## Feeling $\gt$ Understanding

### conclusion

* For $n$ node complete tree
  * the deeptest level is $\lfloor log(n) \rfloor$
  * the left bottom node split the tree nodes

- $\lceil log(n + 1) \rceil = \lfloor log(n) \rfloor + 1$

In a complete binary tree, for each node, let __depth__ be the number of edges on the simple path from such node to the root node. Such that the depth of root node is $0$. And its direct children has depth of $1$.

All the nodes of the same depth $x$, form the __level__ of $x$.

Let $L_i$ denote the number of nodes in level $i$. It follows that $L_0 = 1$, $L_1 = 2$, and easily we can prove $L_n = 2^n$.

Let $H_i$ denote the number of all the nodes at and above level $i$. So we have

$$H_k = \sum_{i = 0}^{k} L_i$$

Where $H_0 = L_0 = 1$, $H_1 = L_0 + L_1 = 3$. It is trivial to prove that

$$H_n = L_{n + 1} - 1$$

Some times we care about the property of a nearly complete binary tree with $n$ nodes. Say, how many levels it covers?

If we mark all the nodes using the topology order, top down, left to right. From $1$ to $n$.

Then we have the left bottom node $m = 2^L$ where $L$ is the deepest level of the tree.

Since $m = 2^L \leq n < 2^{L+1}$, it means $L \leq log(n) < L+1$.

So the lowest level is $L = \lfloor log(n) \rfloor$.

And total level number is $L + 1 = \lfloor log(n) \rfloor + 1$ since level index from $0$ to $L$.

Also, from

$$2^L \leq n < 2^{L+1}$$

we have

$$
\begin{array}{l}
2^L < n + 1 \leq 2^{L+1} \\
L < log(n + 1) \leq L+1 \\
\lceil log(n + 1) \rceil = L + 1
\end{array}
$$

So the total number of levels is

$$\lceil log(n + 1) \rceil = \lfloor log(n) \rfloor + 1$$


--8<--
included.md
--8<--
