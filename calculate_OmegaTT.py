from calculate_HC import calculate_HC
from calculate_Fj import calculate_Fj

def calculate_Omega_TT(HC_n, Fj_n):
    """Calculate collapse ratio Omega_TT(n) = H_C(n) / F_j(n)"""
    if Fj_n == 0:
        raise ZeroDivisionError("F_j(n) must not be zero.")
    return HC_n / Fj_n

# Example usage
if __name__ == "__main__":
    HC_n = calculate_HC(128)
    Fj_n = calculate_Fj([(1,2), (2,3), (3,4)])
    omega = calculate_Omega_TT(HC_n, Fj_n)
    print(f"Omega_TT(n) = {omega}")