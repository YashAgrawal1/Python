# print(3+7)

# def yash(a: int) -> str:
#     print('yash', a)
#     return 10

# print(yash(1))

# def sum(n1:int = 2, n2: int = 5) -> int:
#     print(n1+n2)

# print(sum(3,4))

# def sum1(n1,n2):
#     l1 = [n1,n2,n1+n2]
#     return l1

# print(sum1(3,4))
# l1 = sum1(3,4)
# print(l1)

# def sum2(*args, **kwargs):
#     res = 1
#     for x in args:
#         res *= x
#     print(args)
#     print(kwargs)
#     return res

# print(sum2(1,2,3, [1,2], a=1))

# lambda_f1 = lambda x: x+3
# print(lambda_f1(4))

# one_to_10 = range(1,11)

# print(tuple(map(lambda x: x*2, one_to_10)))


def f1(a1, a2):
    print(a1)


def f2():
    print('hello')

f1(f2(),2)