# Importing functions from other modules
from str2matrix import string_to_matrix  # Converts a 32-hexit string to a 4x4 matrix
from matrix2str import matrix_to_string  # Converts a 4x4 matrix to a 32-hexit string
from aes_matrix_addition import add_matrices_mod_11b  # Adds two matrices together
from aes_matrix_multiplication import matrix_multiply_mod_11b_decrypt,matrix_a  # Multiplies matrices (mod 11b) and provides inverse_matrix
from permutation import circular_permute_matrix_decryption  # Applies inverse permutation to a matrix
from sbox_substitution import substitute_with_inverse_sbox  # Applies inverse S-box substitution

def decrypt(ciphertext, round_key):
    # Step 1: Convert ciphertext and round key to 4x4 matrices
    cipher_matrix = string_to_matrix(ciphertext)
    round_key_matrix = string_to_matrix(round_key)

    # Step 2: Add both matrices together (mod 11b)
    xyz_matrix = add_matrices_mod_11b(cipher_matrix, round_key_matrix)

    # Step 3: Multiply by the Inverse Matrix (fetched directly from aes_matrix_multiplication)
    pqr_matrix = matrix_multiply_mod_11b_decrypt(matrix_a,xyz_matrix)

    # Step 4: Apply the circular permutation
    permuted_matrix = circular_permute_matrix_decryption(pqr_matrix)

    # Step 5: Apply the inverse S-Box substitution
    final_matrix = substitute_with_inverse_sbox(permuted_matrix)

    # Step 6: Convert the final matrix to a 32-hexit string
    hex_result = matrix_to_string(final_matrix)

    # Step 7: Convert the 32-hexit string into an ASCII string
    ascii_string = ''.join(
        chr(int(hex_result[i:i+2], 16)) for i in range(0, len(hex_result), 2)
    )

    return hex_result, ascii_string


