def naive_mult_poly(poly1_coeffs:list[complex], poly2_coeffs:list[complex]) -> list[complex]:
    final_deg = len(poly1_coeffs) + len(poly2_coeffs) - 2
    res = [False] * (final_deg + 1)
    for i in range(final_deg + 1):
        res[i] = cross_mult(poly1_coeffs, poly2_coeffs, i)
    
    return res

def cross_mult(vec1:list[complex], vec2:list[complex], deg:int) -> complex:
    output = 0
    for i in range(deg + 1):
        if (i >= len(vec1) or (deg - i) >= len(vec2)):
            continue
        output += vec1[i] * vec2[deg - i]
    
    return output