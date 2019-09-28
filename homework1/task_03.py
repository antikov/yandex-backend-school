x = [1, 2, 3]
y = [5, 10, 15]
answer = [(ix, [ix * iy for iy in y]) for ix in x]
