DATIME_FORMAT = '%d/%m/%Y'
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

def myfunc(a):
    a['key1'] = 19723124


if __name__ == '__main__':
    print('cw_03.py is the main file')

    a = {'key1': 'value1', 'key2': 'value2'}
    print(a)
    myfunc(a)
    print(a)

    b = 4
