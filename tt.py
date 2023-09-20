


def test (a, b, foo):
    return foo(a, b)


d = test(3, 2, lambda x, y : x*y)
print (d)

d = test(3, 2, lambda x, y : x+y)
print (d)

d = test(3, 2, lambda x, y : x-y)
print (d)

d = test(2, 2, lambda x, y : x==y)
print (d)