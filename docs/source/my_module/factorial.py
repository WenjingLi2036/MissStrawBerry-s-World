def factorial(n: int) -> int:
    """Function to calculate the factorial of *n*.

    Parameters
    ----------
    n : int
        Number to calculate the factorial

    Returns
    -------
    int
        The calculated factorial

    Examples
    --------
    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    out = 1
    for i in range(2, n + 1):
        out *= i
    return out
