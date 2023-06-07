from timeit import timeit


print(timeit("""
b, c = map(int, ["15", "14"])
"""))
print(timeit("""
a = ["15", "14"]
b, c = int(a[0]), int(a[1])
"""))
