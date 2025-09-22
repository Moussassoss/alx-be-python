#!/usr/bin/env python3
"""Module to perform basic arithmetic operations."""


def perform_operation(num1, num2, operation):
    """
    Perform an arithmetic operation on two numbers.

    Args:
        num1: First number.
        num2: Second number.
        operation: 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        Result of the operation, or an error message.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
