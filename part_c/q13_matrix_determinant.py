import os
import sys

# Adjust path to find matrix_utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import matrix_utils

def show_determinant_explanation_2x2(M):
    a, b = M[0]
    c, d = M[1]
    print("Determinant formula for a 2x2 matrix:")
    print("  |A| = a*d - b*c")
    print(f"  |A| = ({a:.2f} * {d:.2f}) - ({b:.2f} * {c:.2f})")
    print(f"  |A| = {a*d:.4f} - {b*c:.4f}")
    print(f"  |A| = {a*d - b*c:.4f}\n")

def show_determinant_explanation_3x3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    
    term_a = a * (e*i - f*h)
    term_b = b * (d*i - f*g)
    term_c = c * (d*h - e*g)
    det = term_a - term_b + term_c
    
    print("Determinant formula for a 3x3 matrix (Cofactor Expansion along Row 1):")
    print("  |A| = a * det(2x2 sub-matrix A11) - b * det(2x2 sub-matrix A12) + c * det(2x2 sub-matrix A13)")
    print(f"  |A| = {a:.2f} * ({e:.2f}*{i:.2f} - {f:.2f}*{h:.2f}) - {b:.2f} * ({d:.2f}*{i:.2f} - {f:.2f}*{g:.2f}) + {c:.2f} * ({d:.2f}*{h:.2f} - {e:.2f}*{g:.2f})")
    print(f"  |A| = {a:.2f} * ({e*i:.2f} - {f*h:.2f}) - {b:.2f} * ({d*i:.2f} - {f*g:.2f}) + {c:.2f} * ({d*h:.2f} - {e*g:.2f})")
    print(f"  |A| = {a:.2f} * ({e*i - f*h:.4f}) - {b:.2f} * ({d*i - f*g:.4f}) + {c:.2f} * ({d*h - e*g:.4f})")
    print(f"  |A| = {term_a:.4f} - ({term_b:.4f}) + ({term_c:.4f})")
    print(f"  |A| = {det:.4f}\n")

def run_determinant_calculator():
    print("=" * 60)
    print(" QUESTION 13: MATRIX DETERMINANT CALCULATOR ")
    print("=" * 60)
    
    print("Choose matrix size:")
    print("1. 2x2 Matrix")
    print("2. 3x3 Matrix")
    choice = input("Enter choice (1 or 2, default is 1): ").strip()
    
    if choice == "2":
        # 3x3 Sample
        M = [
            [2, -3,  1],
            [2,  0, -1],
            [1,  4,  5]
        ]
        matrix_utils.print_matrix(M, "M (3x3)")
        det = matrix_utils.det_3x3(M)
        show_determinant_explanation_3x3(M)
    else:
        # 2x2 Sample
        M = [
            [4, 6],
            [3, 8]
        ]
        matrix_utils.print_matrix(M, "M (2x2)")
        det = matrix_utils.det_2x2(M)
        show_determinant_explanation_2x2(M)
        
if __name__ == "__main__":
    run_determinant_calculator()
