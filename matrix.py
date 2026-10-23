import numpy as np
from random import randint 

N = int(input("Ведите число строк(N): "))
M = int(input("Ведите число столбцов(M): "))

bb = np.random.randint(0, 1_000_000, size=(N, M))

print(f'Исходная матрица {N}x{M}\n{bb}')
print('------------------------------------------------------------------------------------')
bb_transpose = bb.transpose()

print(f'Транспонированная матрица {bb_transpose}')

dt = np.linalg.det(bb)
dt_transpose = np.linalg.det(bb_transpose)

if dt == dt_transpose:
    print(f'Определитель обычной матрицы равен определителю транспонированной {dt} = {dt_transpose}')
elif dt > dt_transpose:
    print(f'Определитель обычной матрицы больше определителья транспонированной {dt} > {dt_transpose}')
else:
    print(f'Определитель обычной матрицы меньше определителья транспонированной {dt} < {dt_transpose}')

