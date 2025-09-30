def safe_divide(numerator, denominator):
    """
    Perform division with error handling.
    
    Args:
        numerator: The numerator (string, will be converted to float).
        denominator: The denominator (string, will be converted to float).
    
    Returns:
        str: Result of the division or error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
