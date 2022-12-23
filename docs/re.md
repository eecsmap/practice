Regular expression is a great tool to describe a computation structure **Finite Automata**.

## basic rule
### 1st try
- expression    :=  term ('|' term) *
- term          :=  factor (factor) *
- factor        :=  element | element '*'
- element       :=  literal | '(' expression ')'
- literal       :=  one of printables except '(' ')' '|' '*' '\' | escape
- escape        :=  '\' '(' | '\' ')' | '\' '|' | '\' '\'

The problem of 1st try is that it does not address $\epsilon$

## extensions
- expression := expression '|' term
              | term
- term := factor *
- factor := '(' expr ')'
-         | exp
- exp := literal '*'
- literal := one of '_abcdefghijklmnopqrstuvwxyz0123456789'
- 
## a
## b
## x