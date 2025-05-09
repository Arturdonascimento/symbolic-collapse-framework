def calculate_Fj(Rn):
    """Calculate symbolic resistance F_j(n) as the cardinality of the restorative set."""
    return len(Rn)

# Example usage
if __name__ == "__main__":
    restorative_transitions = [(1,2), (2,3), (3,4)]
    Fj_n = calculate_Fj(restorative_transitions)
    print(f"F_j(n) = {Fj_n}")