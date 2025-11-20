# Style Guide
- Use [Black](https://github.com/psf/black) as formatter
- Files, functions, and variables shall have `lower_snake_case` names
- Constants shall have `UPPER_SNAKE_CASE` names
- Each component shall be annotated with `@gdsfactory.cell` and shall contain no unnamed cells
- Use math functions from `numpy` instead of `math`, when applicable
- Use degrees instead of radians, when applicable

- Function parameters and return values shall have type hints
```python
# bad
def some_function(a, b):
    return a + b

# good
def some_function(a: float, b: float) -> float:
    return a + b
```

- Explicitly type namespaces
```python
# bad
from gdsfactory.component import Component
c = Component()

# good
import gdsfactory as gf
c = gf.Component()
```

- Lists or parameters longer than 2 shall have a trailing comma for proper formatting
```python
# bad
my_list = [item1, item2, item3, item4]

def some_function(a: float, b: float, c: float) -> float:
    ...

# good
my_list = [
    item1,
    item2,
    item3,
    item4,
]

def some_function(
    a: float,
    b: float,
    c: float
) -> float:
    ...
```

- Function calls with more than 2 parameters shall have all parameter names explicitly typed
```python
# bad
result = some_function(i, j, k)

# good
result = some_function(
    a=i,
    b=j,
    c=k,
)
```

- Use the `<<` magic instead of `c.add_ref()`, explicitly cast unused reference to `_`
```python
# bad
my_component.add_ref(my_other_component).move((x, y))

# good
component_ref = my_component << my_other_component
component_ref.move((x, y))

_ = my_component << my_other_component
```
