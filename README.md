Run `monitors.py`. It outputs a list of connected monitors. Then enter a configuration.

Allowed operations:
- `a=b` mirrors a and b
- `a>b` extends a to the right onto b, `a<b` goes left
- `a^b` extends a upwards onto b, `aVb` goes downwards

Operations can be transitive:
- `a=b=c` mirrors a, b, and c
- `a>b>c` extends a rightwards onto b, and then onto c

Separate statements with space.

Complex example:
```
    +---+
    | D |
+---+---+---+
| A | B | C |
+---+---+---+
```
could be `a>b>c b^d`.
