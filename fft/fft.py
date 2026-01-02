from math import e, pi, log2

def priv_FFT(P:list[complex], inverse = False):
    # where P is the input vector (either c or y)
    # we also assume n is a power of 2
    n = len(P)

    # We know that F_2n = 
    # [I D; I -D] [F_n 0; 0 F_n] [interleave even and odd]

    if (n == 1):
        # if n == 1, we have come full circle to root = 1
        # so we just need to return the remaining coefficient
        return P

    # [interleave even and odd]
    # even and odd splits
    P_even, P_odd = split_odd_even(P)

    # now apply [F_n 0; 0; F_n] to interleaved values
    # sample the values recursively
    O_even, O_odd = priv_FFT(P_even, inverse), priv_FFT(P_odd, inverse)

    # now we do [I D; I -D]
    # root of unity
    w = e**(2j * pi / n) if inverse == False else e**(-2j * pi / n)

    res = [-1] * n
    for i in range(n//2):
        d_i = w**i

        # [I D]
        res[i] = O_even[i] + d_i * O_odd[i]
        
        # -w**(i) = w**(i) * -1
        # -1 = w**(n//2)
        # [I -D]
        res[i + n//2] = O_even[i] - d_i * O_odd[i]
    return res

def split_odd_even(P:list[complex]) -> tuple[list[complex], list[complex]]:
    # n = len(P)
    # P_even = [-1] * n // 2
    # P_odd = [-1] * n // 2

    # for i in range(n//2):
    #     P_even[i] = P[2*i]
    #     P_odd[i] = P[2*i + 1]

    P_even = P[::2]
    P_odd = P[1::2]

    return P_even, P_odd

def FFT(P:list[complex]):
    if (log2(len(P))//1 != log2(len(P))):
        print("length of FFT input not power of 2")
        return [False]
    return priv_FFT(P)

def IFFT(P:list[complex]):
    if (log2(len(P))//1 != log2(len(P))):
        print("length of IFFT input not power of 2")
        return [False]
    return list(map(lambda x: x / len(P), priv_FFT(P, True)))
