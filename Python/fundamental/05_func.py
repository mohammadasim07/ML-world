def cal(a,b):
    sum = a+b
    print(a+b)
    return sum

a = cal(1,2)
print (a )

def avg(a,b,c):
    return (a+b+c)/3

print(avg(1,2,3))

cities = ["car","park","pune"]
def print_len(cities):
    print(len(cities))

print_len(cities)

def print_line(a):
    print(a)

print_line(cities)

def fact(a):
    # if(a <= 0):
    #     return 0
    return a+fact(a-1)
print(fact(10))
