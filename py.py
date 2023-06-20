from timeit import timeit

print(timeit('''
a, b, c = 'a b c'.split()
a, b, c
'''))
print(timeit('''
a = 'a b c'.split()
a[0], a[1], a[2]
'''))
