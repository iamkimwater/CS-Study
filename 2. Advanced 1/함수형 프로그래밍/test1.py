# x를 어떻게 2로 만들까?
# x = 1
# x += 1
# print(x)

x = 1
def add_one(x):
    x += 1
    print(x)
add_one(x)
print(x)

y = []
def append_one(y):
    y.append(1)
append_one(y)
print(y)