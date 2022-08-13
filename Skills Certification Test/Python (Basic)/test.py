import functools

st='bacdf'
res = functools.reduce(lambda x, y: x + y, sorted(st))
print(sorted(st))
print(res)