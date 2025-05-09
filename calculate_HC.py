import math

def calculate_HC(Pn):
    """Calculate positional entropy H_C(n) as log2 of number of configurations."""
    if Pn <= 0:
        raise ValueError("Number of configurations must be positive.")
    return math.log2(Pn)

# Example usage
if __name__ == "__main__":
    n_configurations = 128
    HC_n = calculate_HC(n_configurations)
    print(f"H_C(n) = {HC_n}")