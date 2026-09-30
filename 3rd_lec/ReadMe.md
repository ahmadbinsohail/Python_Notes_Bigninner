# Lesson 3: Python Basics

This file is a guide to [`3rd_lec.py`](3rd_lec.py). The script is a set of beginner exercises covering loops, collections, dictionaries, and functions. It runs from top to bottom, printing results and asking for input along the way.

## Topics Covered

1. **`for` loops and `range`**: Prints values from `range(10)`, `range(3, 6)`, and `range(2, 20, 5)`. The stop value in `range` is not included.
2. **Accumulating a total**: Adds the shopping-cart prices into `totall` and prints the total.
3. **Nested loops**: Uses the values in `list_f` to print rows of `X` characters, demonstrating a loop inside another loop.
4. **Lists and finding a maximum**: Creates a list of names, then checks each number to find and print the greatest value. A counter is also printed during the loop.
5. **Nested lists (a matrix)**: Reads an item from a 2D list using two indexes, then loops over every row and item.
6. **List methods**: Demonstrates `append`, `insert`, `extend`, `pop`, `remove`, `copy`, `clear`, `index`, `count`, `sort`, and `reverse`.
7. **Removing duplicates**: Copies the original numbers for iteration and removes extra occurrences from the working list, then sorts and prints the unique values.
8. **Tuples and unpacking**: Stores coordinates in a tuple and assigns its four values to four variables. Tuples cannot be changed after creation.
9. **Dictionaries**: Stores manager details and looks up values with `get`, including a default result for a missing key. The phone-number exercise maps each digit character to a word.
10. **Functions and arguments**: Defines `salam` with two parameters and calls it using positional and keyword arguments.
11. **Return values**: Defines `square`, which returns the square of a number.
12. **Emoji conversion**: Splits a message into words and replaces recognized words such as `happy` or `sad` with emoji.

## Input Prompts

When you run the script, provide these inputs in order:

1. A phone number made of digits for the digit-to-word exercise.
2. Your first name.
3. Your last name.
4. A number to square. It must be valid input for `int`.
5. A message containing words to convert, such as `I am happy`.

## Run the Script

From this folder, run:

```powershell
python 3rd_lec.py
```

Use `python3 3rd_lec.py` instead if that is the Python command configured on your system.

## Notes

- List indexes start at `0`; for example, `matrix[1][2]` is `6`.
- `manager.get("Name", "Not Found")` uses a capital `N`, but the dictionary key is lowercase `name`. Dictionary keys are case-sensitive, so the fallback is returned.
- The phone dictionary uses string keys such as `"0"`; it processes the input one character at a time and prints `?` for characters that are not mapped.
- Emoji replacements match exact, lowercase words. Punctuation stays attached to a word, so `happy!` is not the same key as `happy` and will not be replaced.
- The maximum-number exercise initializes its result to `0`. That works for the numbers currently in the file, but a list containing only negative values would need a different starting value (for example, the first list item).
- The `numbers.index(54)` call demonstrates the method, but its result is not printed. `index` and `remove` raise an error if the requested value is not present.
