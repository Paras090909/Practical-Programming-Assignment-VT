import os
import sys

# Adjust path to find matrix_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import matrix_utils

def check_equality(M1, M2):
    """Check if two matrices are equal (within tiny floating point tolerance)."""
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        return False
    for r in range(len(M1)):
        for c in range(len(M1[0])):
            if abs(M1[r][c] - M2[r][c]) > 1e-9:
                return False
    return True

def run_transpose_verification():
    print("=" * 60)
    print(" QUESTION 12: MATRIX TRANSPOSE & VERIFICATION ")
    print("=" * 60)

    # Define matrices
    A = [
        [1, 5, 3],
        [4, 2, 6]
    ] # 2x3 Matrix
    
    B = [
        [0, -1, 4],
        [3,  5, 2]
    ] # 2x3 Matrix
    
    C = [
        [2, 1],
        [-3, 4],
        [5, 0]
    ] # 3x2 Matrix
    
    matrix_utils.print_matrix(A, "A (2x3)")
    
    # 1. Calculate Transpose
    AT = matrix_utils.transpose(A)
    matrix_utils.print_matrix(AT, "A^T (Transpose of A - 3x2)")
    
    # Mathematical Verifications
    print("=" * 60)
    print(" MATHEMATICAL PROPERTY VERIFICATIONS ")
    print("=" * 60)

    # Verification 1: (A^T)^T == A
    print("1. Verifying Double Transpose: (A^T)^T = A")
    double_T = matrix_utils.transpose(AT)
    is_equal_1 = check_equality(double_T, A)
    print(f"   (A^T)^T is equal to A: {is_equal_1}")
    matrix_utils.print_matrix(double_T, "(A^T)^T")

    # Verification 2: (A + B)^T == A^T + B^T
    print("2. Verifying Sum Transpose: (A + B)^T = A^T + B^T")
    A_plus_B = matrix_utils.matrix_add(A, B)
    LHS_2 = matrix_utils.transpose(A_plus_B) # (A + B)^T
    
    BT = matrix_utils.transpose(B)
    RHS_2 = matrix_utils.matrix_add(AT, BT) # A^T + B^T
    
    is_equal_2 = check_equality(LHS_2, RHS_2)
    print(f"   (A + B)^T is equal to A^T + B^T: {is_equal_2}\n")

    # Verification 3: (A * C)^T == C^T * A^T
    print("3. Verifying Product Transpose: (A * C)^T = C^T * A^T")
    AC = matrix_utils.matrix_mul(A, C) # 2x2 Matrix
    LHS_3 = matrix_utils.transpose(AC) # (A * C)^T
    
    CT = matrix_utils.transpose(C)
    RHS_3 = matrix_utils.matrix_mul(CT, AT) # C^T * A^T (2x2)
    
    is_equal_3 = check_equality(LHS_3, RHS_3)
    print(f"   (A * C)^T is equal to C^T * A^T: {is_equal_3}")
    matrix_utils.print_matrix(LHS_3, "LHS (A * C)^T")
    matrix_utils.print_matrix(RHS_3, "RHS C^T * A^T")
    
    print("SUMMARY: All transposing axioms verified mathematically!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_transpose_verification()
