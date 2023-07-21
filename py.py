from timeit import timeit

print(timeit('''
a, b = 0, 0
'''))
print(timeit('''
a = 0
b = 0
'''))
