# Fuel Gauge

![fuel gauge](https://m.media-amazon.com/images/I/51PB9hrjJ3L._SX342_.jpg)  
Source: [amazon.com/dp/B09C4FL56G](https://www.amazon.com/dp/B09C4FL56G)

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, output `F` instead to indicate that the tank is essentially full.

If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, instead prompt the user again. (It is not necessary for `Y` to be `4`.) Be sure to catch any exceptions like [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) or [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

Hints

- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`.
- Note that you can handle two exceptions separately with code like:

  ```python
  try:
      ...
  except ValueError:
      ...
  except ZeroDivisionError:
      ...
  ```

  Or you can handle two exceptions together with code like:

  ```python
  try:
      ...
  except (ValueError, ZeroDivisionError):
      ...
  ```

## How to Test

Here’s how to test your code manually:

- Run your program with `python fuel.py`. Type `3/4` and press Enter. Your program should output:

  ```
  75%
  ```

- Run your program with `python fuel.py`. Type `1/4` and press Enter. Your program should output:

  ```
  25%
  ```

- Run your program with `python fuel.py`. Type `4/4` and press Enter. Your program should output:

  ```
  F
  ```

- Run your program with `python fuel.py`. Type `0/4` and press Enter. Your program should output:

  ```
  E
  ```

- Run your program with `python fuel.py`. Type `4/0` and press Enter. Your program should handle a [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) and prompt the user again.
- Run your program with `python fuel.py`. Type `three/four` and press Enter. Your program should handle a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) and prompt the user again.
- Run your program with `python fuel.py`. Type `1.5/3` and press Enter. Your program should handle a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) and prompt the user again.
- Run your program with `python fuel.py`. Type `5/4` and press Enter. Your program should prompt the user again.
