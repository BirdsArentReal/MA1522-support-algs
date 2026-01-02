from fft import FFT, IFFT
from math import log2, ceil

def mult_poly(poly1_coeffs:list[complex], poly2_coeffs:list[complex]) -> list[complex]:
    final_deg = len(poly1_coeffs) + len(poly2_coeffs) - 2
    poly1_coeffs = pad_to_deg(poly1_coeffs, final_deg)
    poly2_coeffs = pad_to_deg(poly2_coeffs, final_deg)

    poly1_val = FFT(poly1_coeffs)
    poly2_val = FFT(poly2_coeffs)

    poly_val = hadamard_mult_1D(poly1_val, poly2_val)
    poly_coeffs = IFFT(poly_val)
    
    return display(poly_coeffs)

def pad_to_deg(poly:list[complex], deg:int):
    for _ in range(len(poly), deg + 2):
        poly.append(0)
    return pad_poly_coeffs(poly)

def pad_poly_coeffs(P:list[complex]):
    # constant all the way in front
    n = len(P)
    target = 2**(ceil(log2(n)))

    for i in range(n, target):
        P.append(0)
    
    return P


def hadamard_mult_1D(vec1: list[complex], vec2: list[complex]):
    if (len(vec1) != len(vec2)):
        print("Hadamard prod fail: different length")
        return [0]

    res = [0] * len(vec1)

    for i in range(len(vec1)):
        res[i] = vec1[i] * vec2[i]
    
    return res


def display(P:list[complex], n_digits = 3):
    return list(map(lambda x: complex(round(x.real, n_digits), round(x.imag, n_digits)), P))