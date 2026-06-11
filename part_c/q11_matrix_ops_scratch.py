import os
import sys

# Adjust path to find matrix_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import matrix_utils

def explain_multiplication(A, B, result):
    """Print step-by-step dot product calculations."""
    print("Multiplication Step-by-Step Details:")
    print("-" * 50)
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    for r in range(rows_A):
        for c in range(cols_B):
            terms = [f"({A[r][k]:.1f} * {B[k][c]:.1f})" for k in range(cols_A)]
            equation = " + ".join(terms)
            val = result[r][c]
            print(f"Cell ({r},{c}): RowA[{r}] • ColB[{c}] = {equation} = {val:.3f}")
    print("-" * 50 + "\n")

def run_matrix_ops():
    print("=" * 60)
    print(" QUESTION 11: MATRIX OPERATIONS FROM SCRATCH ")
    print("=" * 60)
    
    print("Using pre-defined matrices to demonstrate operations:")
    
    # 2x3 Matrix A
    A = [
        [3, 8, 2],
        [5, 1, 9]
    ]
    
    # 2x3 Matrix B (for Addition and Subtraction)
    B = [
        [1, -2, 5],
        [4,  6, -3]
    ]
    
    # 3x2 Matrix C (for Multiplication: A * C)
    C = [
        [2,  7],
        [6,  0],
        [-1, 4]
    ]
    
    matrix_utils.print_matrix(A, "A (2x3)")
    matrix_utils.print_matrix(B, "B (2x3)")
    matrix_utils.print_matrix(C, "C (3x2)")
    
    print("=" * 60)
    print("1. MATRIX ADDITION (A + B)")
    print("=" * 60)
    try:
        add_res = matrix_utils.matrix_add(A, B)
        matrix_utils.print_matrix(add_res, "A + B")
    except Exception as e:
        print(f"Error: {e}")
        
    print("=" * 60)
    print("2. MATRIX SUBTRACTION (A - B)")
    print("=" * 60)
    try:
        sub_res = matrix_utils.matrix_sub(A, B)
        matrix_utils.print_matrix(sub_res, "A - B")
    except Exception as e:
        print(f"Error: {e}")
        
    print("=" * 60)
    print("3. MATRIX MULTIPLICATION (A * C)")
    print("=" * 60)
    try:
        mul_res = matrix_utils.matrix_mul(A, C)
        matrix_utils.print_matrix(mul_res, "A * C (2x2)")
        explain_multiplication(A, C, mul_res)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_matrix_ops()
