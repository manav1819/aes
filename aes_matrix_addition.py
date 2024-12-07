from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod

# Function to perform matrix addition using XOR in GF(2^8)
def add_matrices_mod_11b(matrix_a, matrix_b):
    """Add two matrices element-wise using XOR in GF(2^8)."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Use the xor_hex_mod_11b function to add elements
            row.append(xor_hex_mod_11b(matrix_a[i][j], matrix_b[i][j]))
        result.append(row)
    return result

