def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s = ""
    if(a > 0):
        s += "positive "
    else:
        s += "negative "
    if(a % 2!=0):
        s += "odd "
    else:
        s += "even "
    s += "number"
    if(a == 0):
        return "zero"
    return s