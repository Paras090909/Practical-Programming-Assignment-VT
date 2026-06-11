import numpy as np

def print_augmented_matrix(A, b, step_label=None):
    """Print the augmented matrix [A|b] in a clean, readable format."""
    n = len(A)
    if step_label:
        print(f"--- {step_label} ---")
    for i in range(n):
        row_str = "  [" + " ".join(f"{x:7.3f}".strip() for x in A[i]) + " | " + f"{b[i]:7.3f}".strip() + "]"
        print(row_str)
    print()

def solve_system_step_by_step():
    print("=" * 60)
    print(" QUESTION 15: LINEAR SYSTEM SOLVER (GAUSSIAN ELIMINATION) ")
    print("=" * 60)
    
    # We will solve:
    # 3x + 2y - z = 1
    # 2x - 2y + 4z = -2
    # -x + 0.5y - z = 0
    #
    # Matrix A:
    # [ 3.0,  2.0, -1.0 ]
    # [ 2.0, -2.0,  4.0 ]
    # [-1.0,  0.5, -1.0 ]
    #
    # Vector b:
    # [  1.0 ]
    # [ -2.0 ]
    # [  0.0 ]
    
    A = [
        [3.0,  2.0, -1.0],
        [2.0, -2.0,  4.0],
        [-1.0, 0.5, -1.0]
    ]
    
    b = [1.0, -2.0, 0.0]
    
    n = len(A)
    # Work with copies to keep inputs clean
    M_A = [row[:] for row in A]
    M_b = b[:]

    print("Solving the system Ax = b:")
    print("  Equation 0:  3x + 2y -  z =  1")
    print("  Equation 1:  2x - 2y + 4z = -2")
    print("  Equation 2:  -x + 0.5y - z =  0\n")
    
    print_augmented_matrix(M_A, M_b, "Initial Augmented Matrix [A|b]")

    # Gaussian Elimination with Partial Pivoting
    for i in range(n):
        # 1. Partial Pivoting (find the max element in column i, rows >= i)
        max_row = i
        for r in range(i + 1, n):
            if abs(M_A[r][i]) > abs(M_A[max_row][i]):
                max_row = r
                
        # Swap current row with max_row if needed
        if max_row != i:
            M_A[i], M_A[max_row] = M_A[max_row], M_A[i]
            M_b[i], M_b[max_row] = M_b[max_row], M_b[i]
            print_augmented_matrix(M_A, M_b, f"Pivot Step: Swapped row {i} and row {max_row}")

        # Check for singularity
        if abs(M_A[i][i]) < 1e-9:
            print("Error: Matrix is singular or nearly singular. Division by zero will occur.")
            return

        # 2. Row operations: Eliminate column i from rows > i
        for r in range(i + 1, n):
            factor = M_A[r][i] / M_A[i][i]
            print(f"Row Operation: R{r} = R{r} - ({factor:.3f}) * R{i}")
            # Update row r of A
            for c in range(i, n):
                M_A[r][c] -= factor * M_A[i][c]
            # Update row r of b
            M_b[r] -= factor * M_b[i]
            
        print_augmented_matrix(M_A, M_b, f"After eliminating column {i} below diagonal")

    # 3. Back Substitution
    print("=" * 40)
    print(" BACK SUBSTITUTION ")
    print("=" * 40)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_terms = sum(M_A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M_b[i] - sum_terms) / M_A[i][i]
        
        # Explain step
        equation_desc = f"x[{i}] = ({M_b[i]:.3f}"
        for j in range(i + 1, n):
            sign = "+" if M_A[i][j] * x[j] < 0 else "-"
            val = abs(M_A[i][j] * x[j])
            equation_desc += f" {sign} {val:.3f}"
        equation_desc += f") / {M_A[i][i]:.3f} = {x[i]:.3f}"
        print(f"Solving for Variable {i}: {equation_desc}")

    # Solve result
    variables = ["x", "y", "z"]
    print("\nFinal Solution:")
    for name, val in zip(variables, x):
        print(f"  {name} = {val:8.4f}")
    
    # Mathematical verification: Ax == b
    print("\nVerification (Ax = b check):")
    verify_b = np.dot(A, x)
    for i in range(n):
        diff = abs(verify_b[i] - b[i])
        print(f"  Row {i}: LHS (Ax) = {verify_b[i]:8.4f} | RHS (b) = {b[i]:8.4f} | Diff = {diff:.1e}")

    print("=" * 60 + "\n")

if __name__ == "__main__":
    solve_system_step_by_step()
