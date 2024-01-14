# Just setting up my twttr

> just setting up my twttr
>
> — jack⚡️ (@jack) [March 21, 2006](https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw)

When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called _twttr_. In a file called `twttr.py`, implement a program that prompts the user for a `str` of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

## Hints

- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Much like a `list`, a `str` is “iterable,” which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:

  ```python
  for c in s:
      print(c, end="")
  ```

## How to Test

Here’s how to test your code manually:

- Run your program with `python twttr.py`. Type `Twitter` and press Enter. Your program should output:

  ```
  Twttr
  ```

- Run your program with `python twttr.py`. Type `What's your name?` and press Enter. Your program should output:

  ```
  Wht's yr nm?
  ```

- Run your program with `python twttr.py`. Type `CS50` and press Enter. Your program should output

  ```
  CS50
  ```
