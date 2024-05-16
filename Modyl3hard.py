data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

count = 0

def calc(param):
    global count
    if isinstance(param,int):
        count +=param
    elif isinstance(param, str):
        count += len(param)
    elif isinstance(param,dict):
        for key, value in param.items():
            calc(key)
            calc(value)
    elif isinstance(param, (list, tuple, set)):
        for i in param:
            calc(i)


for i in data_structure:
    calc(i)

print(count)