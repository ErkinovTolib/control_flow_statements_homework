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
    if a>0:
        s = "positive"
    if a<0:
        s = "negative"
    if a%2==0:
        s+=" even number"
    else:
        s+=" odd number"
    if a==0:
        return "the number is zero"
    return s

   