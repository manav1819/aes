# Importing functions from other modules
from str2matrix import string_to_matrix  # Converts a 32-hexit string to a 4x4 matrix
from matrix2str import matrix_to_string  # Converts a 4x4 matrix to a 32-hexit string
from aes_matrix_addition import add_matrices_mod_11b  # Adds two matrices together
from aes_matrix_multiplication import matrix_multiply_mod_11b_encrypt, matrix_b  # Multiplies matrices (mod 11b)
from permutation import circular_permute_matrix_encryption  # Applies encryption permutation to a matrix
from sbox_substitution import substitute_with_sbox  # Applies S-box substitution

def ascii_to_hex_string(ascii_string):
    """
    Convert an ASCII string to a hexadecimal string.

    Args:
        ascii_string (str): Input ASCII string.

    Returns:
        str: Hexadecimal representation of the ASCII string.
    """
    return ''.join(f"{ord(char):02X}" for char in ascii_string)

def encrypt(ascii_plaintext, round_key):
    # Step 0: Convert ASCII plaintext to hex string
    hex_plaintext = ascii_to_hex_string(ascii_plaintext)

    # Step 1: Convert plaintext and round key to 4x4 matrices
    plaintext_matrix = string_to_matrix(hex_plaintext)
    round_key_matrix = string_to_matrix(round_key)

    # Step 2: Apply the S-Box substitution
    substituted_matrix = substitute_with_sbox(plaintext_matrix)

    # Step 3: Apply the circular permutation
    permuted_matrix = circular_permute_matrix_encryption(substituted_matrix)

    # Step 4: Multiply by the Matrix_b
    multiplied_matrix = matrix_multiply_mod_11b_encrypt(matrix_b, permuted_matrix)

    # Step 5: Add both (round key matrix and result from step 4 matrix) matrices together
    final_matrix = add_matrices_mod_11b(multiplied_matrix, round_key_matrix)

    # Step 6: Convert the final matrix to a 32-hexit string
    hex_result = matrix_to_string(final_matrix)

    return hex_result
