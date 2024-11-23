def xor_hex_mod_11b(*hex_numbers):
    """
    XOR multiple two-hexit hexadecimal numbers, and reduce the result modulo 0x11B if necessary.

    Args:
        *hex_numbers (str): Variable number of two-hexit hexadecimal strings (e.g., '80', '0D').

    Returns:
        str: The result of XORing all the hex numbers, reduced modulo 0x11B if necessary, returned in hexadecimal.
    """
    def binary_poly_mod(product, mod_poly=0x11B):
        """Reduce a binary polynomial modulo 0x11B."""
        mod_degree = mod_poly.bit_length() - 1
        while product.bit_length() > mod_degree:
            shift = product.bit_length() - mod_degree - 1
            product ^= (mod_poly << shift)
        return product

    # Initialize the result with 0
    result = 0

    # Convert each hex number to an integer and XOR it with the result
    for hex_num in hex_numbers:
        result ^= int(hex_num, 16)

    # Reduce modulo 0x11B if the result exceeds 2 hexits (8 bits)
    if result > 0xFF:
        result = binary_poly_mod(result)

    # Convert the result back to hex and return (ensure 2 hexits with zfill)
    return hex(result)[2:].upper().zfill(2)


print(xor_hex_mod_11b('52','41','31','A0'))