# Home Federal Savings Bank

In [season 7, episode 24](https://en.wikipedia.org/wiki/The_Invitations) of [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

## About Problem

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

## Hints

- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods).
- Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

## How to Test

Here’s how to test your code manually:

- Run your program with `python bank.py`. Type `Hello` and press Enter. Your program should output:

  ```
  $0
  ```

- Run your program with `python bank.py`. Type `Hello, Newman` and press Enter. Your program should output:

  ```
  $0
  ```

- Run your program with `python bank.py`. Type `How you doing?` and press Enter. Your program should output

  ```
  $20
  ```

- Run your program with `python bank.py`. Type `What's happening?` and press Enter. Your program should output

  ```
  $100
  ```
