def gf2_multiply_and_mod(hex1, hex2, mod_hex='11B'):
    """
    Multiply two hexadecimal numbers in GF(2^8) and reduce modulo the given polynomial.
    
    Args:
        hex1 (str): First hex number as a string (e.g., '80').
        hex2 (str): Second hex number as a string (e.g., '0D').
        mod_hex (str): Modulus hex polynomial as a string (default is '11B').
    
    Returns:
        str: The result in hexadecimal.
    """
    def hex_to_bin_poly(hex_val):
        """Convert a hex value to a binary polynomial (as a string of bits)."""
        return bin(int(hex_val, 16))[2:]
    
    def binary_poly_multiply(a, b):
        """Multiply two binary polynomials represented as integers."""
        result = 0
        while b > 0:
            if b & 1:  # If the lowest bit of b is 1, add a to the result
                result ^= a
            a <<= 1  # Shift a to the left (multiply by x)
            b >>= 1  # Shift b to the right (divide by x)
        return result

    def binary_poly_mod(product, mod_poly):
        """Reduce a binary polynomial modulo another polynomial."""
        mod_degree = mod_poly.bit_length() - 1
        while product.bit_length() > mod_degree:
            shift = product.bit_length() - mod_degree - 1
            product ^= (mod_poly << shift)
        return product

    # Convert hex inputs to binary polynomials (integers)
    num1 = int(hex_to_bin_poly(hex1), 2)
    num2 = int(hex_to_bin_poly(hex2), 2)
    mod_poly = int(hex_to_bin_poly(mod_hex), 2)

    # Step 1: Multiply
    product = binary_poly_multiply(num1, num2)

    # Step 2: Reduce modulo the given polynomial
    result = binary_poly_mod(product, mod_poly)

    # Convert result to hex and return
    return hex(result)[2:].upper()

print(gf2_multiply_and_mod('b3','0B'))
print(gf2_multiply_and_mod('97','0D'))
print(gf2_multiply_and_mod('48','09'))
print(gf2_multiply_and_mod('cc','0E'))

