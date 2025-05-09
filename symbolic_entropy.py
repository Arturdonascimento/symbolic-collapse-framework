# Pseudocode for calculating symbolic entropy H_C(n)
def positional_entropy(P_n):
    """
    P_n: list of all symbolic configurations at step n
    returns: H_C(n) = log2(len(P_n))
    """
    import math
    return math.log2(len(P_n)) if len(P_n) > 0 else 0
