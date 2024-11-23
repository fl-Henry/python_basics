# # # # # # mytuple = ("apple", "banana", "cherry")
# # # # # # myit = iter(mytuple)
# # # # # #
# # # # # # print(next(myit))
# # # # # # print(next(myit))
# # # # # # print(next(myit))
# # # # # #
# # # # # # # for i in mytuple:
# # # # # #     print(i)
# # # # #
# # # # # x = [i for i in range(5)]
# # # # # print(x)
# # # # # print(next(x))
# # # #
# # # #
# # # # DATE_FORMAT = '%m/%d/%Y'
# # # #
# # # #
# # # # def myfunc(a):
# # # #     def myfunc1(a):
# # # #         x = 300
# # # #         # print(x)
# # # #         # print(DATE_FORMAT)
# # # #         # print("2", a)
# # # #         a['key1'] = 'sdfsdf'
# # # #
# # # #     x = 300
# # # #     # print(x)
# # # #     # print(DATE_FORMAT)
# # # #     # print("2", a)
# # # #     a['key1'] = 'sdfsdf'
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # a = {'key1': 'value1', 'key2': 'value2'}
# # # # print("1", a)
# # # # myfunc(a.copy())
# # # # print("3", a)
# # # # # print(x)
# # #
# # # # import json
# # # # json.loads()
# # # from test_pack.file1 import func1
# # # # from test_pack import func1
# # #
# # # import cw_03 as c
# # # # from cw_03 import DATIME_FORMAT
# # # # from cw_03 import *
# # #
# # # # import pandas as pd
# # # # pd.DataFrame()
# # # # pandas.DataFrame()
# # #
# # # # print(cw_03.DATIME_FORMAT)
# # # print(c.DATIME_FORMAT)
# # # # print(DATIME_FORMAT)
# # #
# # #
# # # if __name__ == '__main__':
# # #     print('main_01.py is the main file')
# #
# #
# # # import datetime
# # from datetime import datetime, UTC
# # #
# # # x = datetime.now()
# # # print(x)
# # # print(type(x))
# # #
# # # print(x.year)
# # # print(x.month)
# # # print(x.day)
# # # print(x.weekday())
# # # print(x.hour)
# # # print(x.minute)
# #
# # sdate = '30/12/2019'
# # print(sdate)
# #
# # ddate = datetime.strptime(sdate, '%d/%m/%Y')
# # print(ddate)
# # print(type(ddate))
# # print(ddate.hour)
# #
# # sdate = ddate.strftime('%Y-%m-%d %H:%M:%S')
# # print(sdate)
# # print(type(sdate))
# a = []
# try:
#     # 1/0
#     # int("sdf")
#     # a[100]
#     pass
# except ValueError:
#     print("ERROR ValueError")
# except ZeroDivisionError:
#     print("ERROR ZeroDivisionError")
# except TypeError:
#     print("ERROR TypeError")
# except Exception:
#     print("ERROR")
# else:
#     print("There were no errors")
# finally:
#     try:
#         f.close()
#     except Exception as e:
#         print(f"ERROR while closing the file: {e}")
#
# # x = -1
# # if x < 0:
# #     raise ValueError("Sorry, no numbers below zero")
#
# print("The program was finished")


# file = open('input.txt', 'w')
# file.write("Some text")
# file.close()

# file = open('input.txt', 'r')
# print(file.read())
# print(repr(file.read()))

# print(repr(file.readline()))
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# file.close()

# file = open('input.txt', 'a')
# file.write("\nNew text")
# file.close()

# with open('input.txt', 'r') as file:
#     print(file.read())


