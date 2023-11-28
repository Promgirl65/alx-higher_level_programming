#!/usr/bin/python3
"""Defines a function for indentation."""


def text_indentation(text):
    """Function prints text with 2 new lines after . , ?, : characters.

    Args:
        text (str): string to print.

    Raises:
        TypeError: If text is not of the str type.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
