from mult_poly import mult_poly, display
from naive_mult_poly import naive_mult_poly
from fft import FFT, IFFT
from perf import timeit
from copy import deepcopy as clone
from random import randint


deg1 = 10**3
deg2 = 10**4
f = lambda: randint(0, 100)

# constants first
poly1 = [f() for _ in range(deg1)]
poly2 = [f() for _ in range(deg2)]

ans1, _ = timeit(lambda: mult_poly(clone(poly1), clone(poly2)), 5)
ans2, _ = timeit(lambda: naive_mult_poly(clone(poly1), clone(poly2)), 5)

# checking well-known periodic waves to make sure it works
n = 2**3
square_wave = [-1] * n + [1] * n
square_pulse = [0] * (n//2) + [1] * n + [0] * (n//2)

sine_x = [0, -1, 0, 1]
sine_2x = [0, -1, 0, 1, 0, -1, 0, 1]
cos_8x = [1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0]

ans_sq_wave, _ = timeit(lambda: FFT(square_wave))
ans_sq_pulse, _ = timeit(lambda: FFT(square_pulse))

ans_sine, _ = timeit(lambda: IFFT(FFT(sine_x)))

ans_sine2, _ = timeit(lambda: FFT(IFFT(sine_2x)))
ans_cos3, _ = timeit(lambda: FFT(cos_8x))

print(display(ans_sine))
print(display(ans_sine2))
print(display(ans_cos3))
