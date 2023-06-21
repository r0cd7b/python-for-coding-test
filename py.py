from timeit import timeit

print(timeit('''
a = [int(s) for s in '0 1 2'.split()]
'''))
print(timeit('''
a = list(map(int, '0 1 2'.split()))
'''))
