# Felipe’s Taqueria

Note that, as of [2023-10-25T11:59:00-04:00](https://time.cs50.io/20231025T115900-0400), the prices of Felipe’s have been updated!

![Felipe's Taqueria](https://cs50.harvard.edu/python/2022/psets/3/taqueria/felipes-logo.png)

One of the most popular places to eat in [Harvard Square](https://en.wikipedia.org/wiki/Harvard_Square) is [Felipe’s Taqueria](https://www.felipesboston.com/), which offers a [menu](https://www.felipesboston.com/menu) of entrees, per the `dict` below, wherein the value of each key is a price in dollars:

```python
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

In a file called `taqueria.py`, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be [titlecased](https://docs.python.org/3/library/stdtypes.html#str.title).

## Hints

- Note that you can detect when the user has inputted control-d by catching an [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) with code like:

  ```python
  try:
      item = input()
  except EOFError:
      ...
  ```

  You might want to print a new line so that the user’s cursor (and subsequent prompt) doesn’t remain on the same line as your program’s own prompt.

- Inputting control-d does not require inputting Enter as well, and so the user’s cursor (and subsequent prompt) might thus remain on the same line as your program’s own prompt. You can move the user’s cursor to a new line by printing `\n` yourself!
- Note that a `dict` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them `get`, and supports operations like:

  ```python
  d[key]
  ```

  and

  ```python
  if key in d:
      ...
  ```

  wherein `d` is a `dict` and `key` is a `str`.

- Be sure to avoid or catch any [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

## How to Test

Here’s how to test your code manually:

- Run your program with `python taqueria.py`. Type `Taco` and press Enter, then type `Taco` again and press Enter. Your program should output:

  ```
  Total: $6.00
  ```

  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Baja Taco` and press Enter, then type `Tortilla Salad` and press enter. Your program should output:

  ```
  Total: $12.25
  ```

  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Burger` and press Enter. Your program should reprompt the user.

Be sure to try other foods and vary the casing of your input. Your program should behave as expected, case-insensitively.
