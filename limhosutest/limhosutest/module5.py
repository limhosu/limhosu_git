def sum(a, b):
    result = a + b
    return result

print(sum(2,5))

def say():
    return 'Hi'
print(say())

myList = [1, 2, 3]
print(myList.pop(1))
print(myList)

a = [1, 3, 5, 7]
b = [1, 1]
def sum_many(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(sum_many(*b))
print(sum_many(2, 7))

def sum_mul(a, b):
    x = a + b
    y = a * b
    print(x)
    print(y)
sum_mul(5, 5)

def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.'% name)
    print('나의 나이는 %d 입니다.'% old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
say_myself('임호수', 54, man=False )

