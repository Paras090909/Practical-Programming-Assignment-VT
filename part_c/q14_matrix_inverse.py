import numpy as np
import os
import sys

def run_inverse_calculator():
    print("=" * 60)
    print(" QUESTION 14: MATRIX INVERSE CALCULATOR (USING NUMPY) ")
    print("=" * 60)
    
    # Define a 3x3 square matrix
    # Note: Determinant must not be zero (non-singular matrix)
    A = np.array([
        [1,  2,  3],
        [0,  1,  4],
        [5,  6,  0]
    ], dtype=float)

    print("Original Matrix A:")
    print(A)
    print()

    # Calculate Determinant to ensure it is invertible
    det_A = np.linalg.det(A)
    print(f"Determinant of A: {det_A:.4f}")
    if np.abs(det_A) < 1e-9:
        print("Error: The matrix is singular (determinant is 0) and cannot be inverted. Exiting.")
        return

    # Calculate Inverse
    A_inv = np.linalg.inv(A)
    print("\nCalculated Inverse Matrix A⁻¹ (via NumPy np.linalg.inv):")
    print(A_inv)
    print()

    # Verify correctness by multiplication: A * A^-1
    print("=" * 60)
    print(" VERIFICATION BY MATRIX MULTIPLICATION ")
    print("=" * 60)
    
    # Check A * A^-1
    product_right = np.dot(A, A_inv)
    print("1. Right Multiplication: A × A⁻¹ =")
    print(product_right)
    print()

    # Check A^-1 * A
    product_left = np.dot(A_inv, A)
    print("2. Left Multiplication: A⁻¹ × A =")
    print(product_left)
    print()

    # Identity Matrix for comparison
    I = np.eye(3)
    
    # Verify with tolerances
    right_ok = np.allclose(product_right, I, atol=1e-9)
    left_ok = np.allclose(product_left, I, atol=1e-9)
    
    print("Comparison results against Identity Matrix I:")
    print(f"- A × A⁻¹ ≈ I: {right_ok}")
    print(f"- A⁻¹ × A ≈ I: {left_ok}")
    
    if right_ok and left_ok:
        print("\nSUCCESS: Verification complete! A × A⁻¹ yields the Identity matrix within numerical tolerance.")
    else:
        print("\nWARNING: Verification failed. Numerical error occurred.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_inverse_calculator()
