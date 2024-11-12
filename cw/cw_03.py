#
#
# # def sum(a, b):
# #     a += 5
# #     # print(x + 10)
# #     return a + b
#
#
# # a = 3
# # b = 5
# # x = 10
# # print(a, b)
# # sum(a, b)
# # print(a, b)
#
#
# def power(x, pw=2):
#     # print(x ** pw)
#     if x == 2:
#         aa = x ** pw
#         return aa
#
#     aa = x * pw
#     return aa
#
#
# def change_dict(init_dict):
#     init_dict.update({'a': 3, 'b': 4})
#
#
# # dd = {
# #     "a": 1,
# #     "b": 2,
# # }
# # print(dd)
# # change_dict(dd.copy())
# # print(dd)
#
# def sum_all(*args, **kwargs):
#     print(args)
#     print(type(args))
#     print(kwargs)
#     print(type(kwargs))
#     print("name is {}".format(kwargs['name']))
#     return sum(args)
#
#
# print(sum_all(1, 2, 3, 4, 5, 6, name=3, aa=2354))
#
#
#
# # result = power(2)
# # print(result)
# # result = power(result, 3)
# # print(result)
# # power(pw=3, x=2)
#
#

def x(a):
    return a + 10


print(x(5))

x = lambda a: a + 10
print(x(10))
