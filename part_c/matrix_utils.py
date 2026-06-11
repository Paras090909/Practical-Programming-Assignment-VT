def print_matrix(matrix, name=None):
    """Print matrix in a clean, readable format."""
    if name:
        print(f"Matrix {name}:")
    for row in matrix:
        print("  [" + ", ".join(f"{x:8.3f}".strip() for x in row) + "]")
    print()

def matrix_add(A, B):
    """Perform Matrix Addition (A + B)."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have identical dimensions for addition.")
        
    rows = len(A)
    cols = len(A[0])
    result = [[A[r][c] + B[r][c] for c in range(cols)] for r in range(rows)]
    return result

def matrix_sub(A, B):
    """Perform Matrix Subtraction (A - B)."""
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have identical dimensions for subtraction.")
        
    rows = len(A)
    cols = len(A[0])
    result = [[A[r][c] - B[r][c] for c in range(cols)] for r in range(rows)]
    return result

def matrix_mul(A, B):
    """Perform Matrix Multiplication (A * B)."""
    if len(A[0]) != len(B):
        raise ValueError(f"Dimensional mismatch: columns of A ({len(A[0])}) must match rows of B ({len(B)}).")
        
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    # Initialize result matrix with zeros
    result = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for r in range(rows_A):
        for c in range(cols_B):
            dot_product = sum(A[r][k] * B[k][c] for k in range(cols_A))
            result[r][c] = dot_product
            
    return result

def transpose(matrix):
    """Calculate the Transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
    return result

def det_2x2(matrix):
    """Calculate the determinant of a 2x2 matrix."""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2.")
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c

def det_3x3(matrix):
    """Calculate the determinant of a 3x3 matrix using cofactor expansion."""
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Matrix must be 3x3.")
        
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    # Cofactor expansion along the first row
    det_a = a * (e * i - f * h)
    det_b = b * (d * i - f * g)
    det_c = c * (d * h - e * g)
    
    return det_a - det_b + det_c
