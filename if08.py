def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a<100 and a>9:
        if a%2==0 :
            return "two-digit even number"
        return "two-digit odd number"
    elif a>100:
        if a%2==1:
            return "three-digit odd number"
        return "three-digit even number"