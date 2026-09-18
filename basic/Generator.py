def my_function():
    yield 1
    yield 2
    yield 3

for value in my_function():
    print(value)

def count_function(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for value in count_function(5):
    print(value)