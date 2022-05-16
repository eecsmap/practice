# Binary Search Tree

## Properties

| Property | Description |
| ----------- | ----------- |
| Root | The only node does not have a parent. |
| Height | The number of edges from one node to its furthest decendent leave node. |
| Depth | The number of edges from one node to the root node. |
| Level | All the nodes with the same depth $x$ form the level of $x$. |


## Traverse

### Inorder

``` { .yaml .annotate }
# Code block content
```

``` { .py .annotate }
def inorder(node, visit):
    inorder(node.left)
    visit(node.value)
    inorder(node.right)
```

``` py title="bst_inorder.py" linenums="1" hl_lines="1 3 5"
def inorder(node, visit):
    inorder(node.left)
    # comment
    visit(node.value) # (1)
    inorder(node.right)
```

1. whatever

## Randomize a BST

A simple solution:

* Traverse the BST and put elements into an array.
* Create a new empty BST.
* Randomly insert the array elements into the new BST.

## Tree Sort

Use a BST to sort elements in a container.

* Create a BST.
* Put every element in the container into the BST. (deal with elements with same key to stablize the sort)
* Inorder traverse the BST and put the elements back into the container.
