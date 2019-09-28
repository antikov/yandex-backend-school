x = [1, 2, 3]
y = [5, 10, 15]
answer = [(ix, iy, ix * iy) for ix in x for iy in y if ix * iy % 2 == 0]
