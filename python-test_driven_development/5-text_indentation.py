#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """indented text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    output = ""
    for char in text:
        output += char
        if char in ".:?":
            output += "\n\n"

    lines = output.splitlines()
    indented_text = "\n".join(line.strip() for line in lines)
    print(indented_text, end="")
