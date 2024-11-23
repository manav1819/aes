from poly_addition import xor_hex_mod_11b
from poly_multiplication import gf2_multiply_and_mod

# Define the two matrices in hexadecimal
matrix1 = [
    ['BA', 'BA', 'BA', 'BA'],
    ['DC', 'DC', 'DC', 'DC'],
    ['0D', '0D', '0D', '0D'],
    ['E2', 'E2', 'E2', 'E2']
]

matrix2 = [
    ['1B', '09', '0E', 'E3'],
    ['97', '4B', 'FA', 'CD'],
    ['0E', '45', 'C5', 'AC'],
    ['7D', '2E', 'BD', '7D']
]

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

# Perform the addition
final_matrix = add_matrices_mod_11b(matrix1, matrix2)

for row in final_matrix:
    print(row)