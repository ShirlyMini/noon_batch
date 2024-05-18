def func1():
    yield True
    yield 500
    yield 0

print(func1())
print(list(func1()))

for i in func1():
    print(i)